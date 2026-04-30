from nltk.stem import PorterStemmer

class EnglishStemmer:
    porter = PorterStemmer()

    @staticmethod
    def stem(text: str) -> str:
        return ' '.join(EnglishStemmer.porter.stem(w) for w in text.split())