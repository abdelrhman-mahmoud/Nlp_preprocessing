import re

class LetterRepetitionNormalizer:
    """يدرسوووون → يدرسون | Helloooo → Hello"""
    PATTERN = re.compile(r'(.)\1{2,}')

    @staticmethod
    def normalize(text: str, max_repeat: int = 1) -> str:
        return LetterRepetitionNormalizer.PATTERN.sub(r'\1' * max_repeat, text)