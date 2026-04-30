import re
from bs4 import BeautifulSoup

class HTMLRemover:
    @staticmethod
    def remove(text: str) -> str:
        text = BeautifulSoup(text, "html.parser").get_text()
        return re.sub(r'&[a-z]+;', ' ', text)