import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json["status"] == "ok"


def test_detect_language_en(client):
    r = client.post("/api/detect-language", json={"text": "Hello world"})
    assert r.json["language"] == "en"


def test_detect_language_ar(client):
    r = client.post("/api/detect-language", json={"text": "مرحبا بالعالم"})
    assert r.json["language"] == "ar"


def test_list_functions_en(client):
    r = client.get("/api/functions/en")
    assert r.status_code == 200
    assert "lemmatize" in r.json["functions"]


def test_preprocess_english(client):
    r = client.post("/api/preprocess", json={
        "text":     "I'm sooo happy! Visit https://test.com",
        "language": "en",
        "steps":    ["remove_urls", "expand_contractions",
                     "lowercase", "normalize_repetition",
                     "normalize_whitespace"],
    })
    assert r.status_code == 200
    assert "output" in r.json
    assert "https" not in r.json["output"]


def test_preprocess_arabic(client):
    r = client.post("/api/preprocess", json={
        "text":     "يَدْرُسُ الطُلّابُ راااائع",
        "language": "ar",
        "steps":    ["remove_tashkeel", "normalize_repetition",
                     "normalize_camel", "lemmatize_msa_camel"],
    })
    assert r.status_code == 200
    output = r.json["output"]
    # Output should be clean (no diacritics)
    assert "َ" not in output  # fatha
    assert "ُ" not in output  # damma