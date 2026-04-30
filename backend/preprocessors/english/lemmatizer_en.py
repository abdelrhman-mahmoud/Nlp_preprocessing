import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag

for pkg in ['wordnet', 'averaged_perceptron_tagger',
            'averaged_perceptron_tagger_eng', 'omw-1.4', 'punkt']:
    try:
        nltk.data.find(pkg)
    except LookupError:
        nltk.download(pkg, quiet=True)


class EnglishLemmatizer:
    lem = WordNetLemmatizer()

    @staticmethod
    def _pos(tag):
        return {'J': wordnet.ADJ, 'V': wordnet.VERB,
                'N': wordnet.NOUN, 'R': wordnet.ADV}.get(tag[0], wordnet.NOUN)

    @staticmethod
    def lemmatize(text: str) -> str:
        tokens = text.split()
        tagged = pos_tag(tokens)
        return ' '.join(
            EnglishLemmatizer.lem.lemmatize(w, EnglishLemmatizer._pos(t))
            for w, t in tagged
        )