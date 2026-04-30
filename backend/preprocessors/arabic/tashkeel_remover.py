import pyarabic.araby as araby

class TashkeelRemover:
    @staticmethod
    def remove(text: str) -> str:
        return araby.strip_tashkeel(text)