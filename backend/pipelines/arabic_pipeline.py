from pipelines.base_pipeline import BasePipeline
from preprocessors.common import (
    URLRemover, HTMLRemover, DigitRemover, EmojiHandler,
    PunctuationRemover, WhitespaceNormalizer, LetterRepetitionNormalizer,
)
from preprocessors.arabic import (
    TashkeelRemover, TatweelRemover, ArabicNormalizer, CamelNormalizer,
    ArabicStopwordRemover, ArabicStemmer, ArabicLemmatizer,
    get_msa_processor, get_egy_processor,
)


class ArabicPipeline(BasePipeline):
    def __init__(self):
        msa_proc = get_msa_processor()
        egy_proc = get_egy_processor()

        super().__init__({
            "remove_html":           HTMLRemover.remove,
            "remove_urls":           URLRemover.remove,
            "remove_emoji":          EmojiHandler.remove,
            "remove_tashkeel":       TashkeelRemover.remove,
            "remove_tatweel":        TatweelRemover.remove,
            "normalize_repetition":  LetterRepetitionNormalizer.normalize,
            "normalize_basic":       ArabicNormalizer.normalize,
            "normalize_camel":       CamelNormalizer.normalize,
            "remove_digits":         DigitRemover.remove,
            "remove_punctuation":    PunctuationRemover.remove,
            "remove_stopwords":      ArabicStopwordRemover.remove,
            "stem_isri":             ArabicStemmer.stem_isri,
            "stem_light":            ArabicStemmer.stem_light,
            "lemmatize_qalsadi":     ArabicLemmatizer.lemmatize,
            "lemmatize_msa_camel":   msa_proc.lemmatize,
            "lemmatize_egy_camel":   egy_proc.lemmatize,
            "normalize_whitespace":  WhitespaceNormalizer.normalize,
        })