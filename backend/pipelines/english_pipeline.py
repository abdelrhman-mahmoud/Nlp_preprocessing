from pipelines.base_pipeline import BasePipeline
from preprocessors.common import (
    URLRemover, HTMLRemover, DigitRemover, EmojiHandler,
    PunctuationRemover, WhitespaceNormalizer, LetterRepetitionNormalizer,
)
from preprocessors.english import (
    LowerCaser, ContractionExpander, EnglishStopwordRemover,
    EnglishStemmer, EnglishLemmatizer, EnglishSpellChecker,
)


class EnglishPipeline(BasePipeline):
    def __init__(self):
        super().__init__({
            "remove_html":           HTMLRemover.remove,
            "remove_urls":           URLRemover.remove,
            "remove_emoji":          EmojiHandler.remove,
            "emoji_to_text":         EmojiHandler.to_text,
            "expand_contractions":   ContractionExpander.expand,
            "lowercase":             LowerCaser.apply,
            "remove_digits":         DigitRemover.remove,
            "remove_punctuation":    PunctuationRemover.remove,
            "normalize_repetition":  LetterRepetitionNormalizer.normalize,
            "spell_correct":         EnglishSpellChecker.correct,
            "remove_stopwords":      EnglishStopwordRemover.remove,
            "stem":                  EnglishStemmer.stem,
            "lemmatize":             EnglishLemmatizer.lemmatize,
            "normalize_whitespace":  WhitespaceNormalizer.normalize,
        })