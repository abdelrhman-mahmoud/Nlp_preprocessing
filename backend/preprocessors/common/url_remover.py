import re

class URLRemover:
    PATTERN = re.compile(r'http[s]?://\S+|www\.\S+')

    @staticmethod
    def remove(text: str) -> str:
        return URLRemover.PATTERN.sub('', text)