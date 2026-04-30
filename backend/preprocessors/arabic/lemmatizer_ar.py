import qalsadi.lemmatizer as qlemma


class ArabicLemmatizer:
    lem = qlemma.Lemmatizer()

    @staticmethod
    def lemmatize(text: str) -> str:
        return str(ArabicLemmatizer.lem.lemmatize_text(text, return_pos=False))