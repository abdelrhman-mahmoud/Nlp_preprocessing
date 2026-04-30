from .tashkeel_remover import TashkeelRemover
from .tatweel_remover import TatweelRemover
from .normalizer_ar import ArabicNormalizer
from .camel_normalizer import CamelNormalizer
from .stopwords_ar import ArabicStopwordRemover
from .stemmer_ar import ArabicStemmer
from .lemmatizer_ar import ArabicLemmatizer
from .camel_processor import (
    DialectalArabicProcessor,
    get_msa_processor,
    get_egy_processor,
)