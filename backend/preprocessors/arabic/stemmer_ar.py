from nltk.stem.isri import ISRIStemmer
from tashaphyne.stemming import ArabicLightStemmer


class ArabicStemmer:
    isri  = ISRIStemmer()
    light = ArabicLightStemmer()

    @staticmethod
    def stem_isri(text: str) -> str:
        return ' '.join(ArabicStemmer.isri.stem(w) for w in text.split())

    @staticmethod
    def stem_light(text: str) -> str:
        return ' '.join(ArabicStemmer.light.light_stem(w) for w in text.split())