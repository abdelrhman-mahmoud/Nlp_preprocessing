import re

class DigitRemover:
    PATTERN = re.compile(r'[0-9\u0660-\u0669\u06F0-\u06F9]')

    @staticmethod
    def remove(text: str) -> str:
        return DigitRemover.PATTERN.sub('', text)