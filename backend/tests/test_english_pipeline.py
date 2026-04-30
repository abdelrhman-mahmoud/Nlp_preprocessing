import pytest
from pipelines import EnglishPipeline


@pytest.fixture
def pipeline():
    return EnglishPipeline()


def test_remove_urls(pipeline):
    text = "Visit https://test.com today"
    result = pipeline.run(text, ["remove_urls"])
    assert "https" not in result["output"]


def test_lowercase(pipeline):
    result = pipeline.run("HELLO WORLD", ["lowercase"])
    assert result["output"] == "hello world"


def test_repetition_normalization(pipeline):
    result = pipeline.run("Helloooo worldddd", ["normalize_repetition"])
    assert "Helloooo" not in result["output"]


def test_full_pipeline(pipeline):
    text = "I'm sooo happy! Visit https://test.com 😄"
    steps = [
        "remove_urls", "remove_emoji", "expand_contractions",
        "lowercase", "remove_punctuation", "normalize_repetition",
        "remove_stopwords", "lemmatize", "normalize_whitespace",
    ]
    result = pipeline.run(text, steps)
    output = result["output"]

    assert "https" not in output
    assert "😄" not in output
    assert "I'm" not in output
    assert output == output.lower()


def test_auto_order(pipeline):
    """Steps should be reordered regardless of user input order."""
    text = "Hello WORLD!"
    # User puts steps in wrong order
    user_steps = ["remove_stopwords", "remove_punctuation", "lowercase"]
    result = pipeline.run(text, user_steps, auto_order=True)

    # Verify execution order
    expected = ["remove_punctuation", "lowercase", "remove_stopwords"]
    assert result["order"] == expected


def test_unknown_step_skipped(pipeline):
    result = pipeline.run("hello", ["nonexistent_step", "lowercase"])
    assert "nonexistent_step" in result["skipped"]
    assert "lowercase" in result["applied"]