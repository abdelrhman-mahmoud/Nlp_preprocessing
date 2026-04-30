import re

class WhitespaceNormalizer:
    @staticmethod
    def normalize(text: str) -> str:
        return re.sub(r'\s+', ' ', text).strip()