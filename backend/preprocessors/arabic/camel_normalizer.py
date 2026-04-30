from camel_tools.utils.normalize import (
    normalize_unicode,
    normalize_alef_ar,
    normalize_alef_maksura_ar,
    normalize_teh_marbuta_ar,
)
from camel_tools.utils.dediac import dediac_ar


class CamelNormalizer:
    """Advanced normalization using CAMeL Tools."""

    @staticmethod
    def normalize(text: str) -> str:
        text = normalize_unicode(text)
        text = dediac_ar(text)
        text = normalize_alef_ar(text)
        text = normalize_alef_maksura_ar(text)
        text = normalize_teh_marbuta_ar(text)
        return text