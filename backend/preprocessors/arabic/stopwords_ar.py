import nltk
from nltk.corpus import stopwords
from config import Config
from utils.file_loader import load_text_file

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)


class ArabicStopwordRemover:
    SW = set(stopwords.words('arabic'))
    SW |= load_text_file(Config.AR_MODELS / "stopwords_custom.txt")

    @staticmethod
    def remove(text: str) -> str:
        return ' '.join(w for w in text.split()
                        if w not in ArabicStopwordRemover.SW)