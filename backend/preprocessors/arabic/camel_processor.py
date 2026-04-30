"""CAMeL morphological disambiguator (MSA & Egyptian)."""
from camel_tools.tokenizers.word import simple_word_tokenize
from camel_tools.disambig.mle import MLEDisambiguator
from camel_tools.utils.dediac import dediac_ar
from config import Config
from utils.logger import app_logger


class DialectalArabicProcessor:
    """Returns lemmas without diacritics by default."""

    def __init__(self, dialect: str = "msa"):
        self.dialect = dialect.lower()
        db = Config.CAMEL_EGY_DB if self.dialect == "egy" else Config.CAMEL_MSA_DB
        app_logger.info(f"Loading CAMeL DB: {db}")
        self.mle = MLEDisambiguator.pretrained(db)

    def analyze(self, text: str):
        tokens   = simple_word_tokenize(text)
        disambig = self.mle.disambiguate(tokens)
        results  = []
        for d in disambig:
            if d.analyses:
                top = d.analyses[0].analysis
                results.append({
                    "word":  d.word,
                    "lemma": top.get("lex", d.word).split('_')[0],
                    "pos":   top.get("pos", "UNK"),
                    "diac":  top.get("diac", d.word),
                })
            else:
                results.append({"word": d.word, "lemma": d.word,
                                "pos": "UNK", "diac": d.word})
        return results

    def lemmatize(self, text: str, dediac: bool = True) -> str:
        result = ' '.join(a["lemma"] for a in self.analyze(text))
        if dediac:
            result = dediac_ar(result)
        return result


# Singleton instances (loaded once)
_msa_proc = None
_egy_proc = None


def get_msa_processor() -> DialectalArabicProcessor:
    global _msa_proc
    if _msa_proc is None:
        _msa_proc = DialectalArabicProcessor("msa")
    return _msa_proc


def get_egy_processor() -> DialectalArabicProcessor:
    global _egy_proc
    if _egy_proc is None:
        _egy_proc = DialectalArabicProcessor("egy")
    return _egy_proc