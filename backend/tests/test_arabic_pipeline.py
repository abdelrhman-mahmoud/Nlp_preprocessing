import pytest
from pipelines import ArabicPipeline


@pytest.fixture(scope="module")
def pipeline():
    return ArabicPipeline()


def test_remove_tashkeel(pipeline):
    result = pipeline.run("يَدْرُسُ", ["remove_tashkeel"])
    assert result["output"] == "يدرس"


def test_remove_tatweel(pipeline):
    result = pipeline.run("الطـــلاب", ["remove_tatweel"])
    assert "ـ" not in result["output"]


def test_repetition(pipeline):
    result = pipeline.run("يدرسوووون", ["normalize_repetition"])
    assert result["output"] == "يدرسون"


def test_camel_normalize(pipeline):
    result = pipeline.run("الجامعة", ["normalize_camel"])
    # ة → ه
    assert "ه" in result["output"]
    assert "ة" not in result["output"]


def test_lemma_no_diacritics(pipeline):
    """التأكد إن lemmatizer مش بيرجع تشكيل."""
    text = "يدرس الطلاب في الجامعة"
    result = pipeline.run(text, ["lemmatize_msa_camel"])
    output = result["output"]

    # Make sure no diacritics in output
    diacritics = ['َ', 'ُ', 'ِ', 'ْ', 'ّ', 'ً', 'ٌ', 'ٍ']
    for d in diacritics:
        assert d not in output, f"Found diacritic {d} in output: {output}"


def test_user_picks_random_order(pipeline):
    """اليوزر يختار خطوات بترتيب عشوائي → الـ pipeline ترتبها."""
    text = "يَدْرُسُ الطُلّابُ راااائع 📚 https://test.com"
    user_steps = [
        "lemmatize_msa_camel",       # اليوزر حطها فوق
        "remove_tashkeel",
        "remove_urls",
        "remove_emoji",
        "normalize_repetition",
        "normalize_camel",
    ]
    result = pipeline.run(text, user_steps, auto_order=True)

    # remove_urls يفترض يتنفذ قبل lemmatize
    assert result["order"].index("remove_urls") < \
           result["order"].index("lemmatize_msa_camel")

    # الـ output نظيف
    assert "https" not in result["output"]
    assert "📚" not in result["output"]


def test_full_egyptian_pipeline(pipeline):
    text = "ازيك يا صاحبي عامل ايه النهاردة؟ 😄"
    steps = [
        "remove_emoji", "remove_punctuation",
        "remove_tashkeel", "normalize_repetition",
        "normalize_camel", "remove_stopwords",
        "lemmatize_egy_camel", "normalize_whitespace",
    ]
    result = pipeline.run(text, steps)
    assert "😄" not in result["output"]
    assert "؟" not in result["output"]
    assert len(result["output"]) > 0