import pyarabic.araby as araby

class TatweelRemover:
    @staticmethod
    def remove(text: str) -> str:
        return araby.strip_tatweel(text)