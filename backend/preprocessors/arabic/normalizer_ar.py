import re

class ArabicNormalizer:
    @staticmethod
    def normalize(text: str) -> str:
        text = re.sub(r'[إأآا]', 'ا', text)
        text = re.sub(r'ى', 'ي', text)
        text = re.sub(r'ة', 'ه', text)
        text = re.sub(r'[ؤئء]', 'ء', text)
        return text