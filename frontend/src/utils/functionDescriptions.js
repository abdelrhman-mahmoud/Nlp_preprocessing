export const FUNCTION_DESCRIPTIONS = {
  // ==== Structural ====
  remove_html: {
    category: 'structural',
    description: 'Strip HTML tags and entities',
    example: '<p>Hi</p> → Hi',
  },
  remove_urls: {
    category: 'structural',
    description: 'Remove URLs and links',
    example: 'Visit https://x.com → Visit',
  },
  remove_emoji: {
    category: 'structural',
    description: 'Remove emoji characters',
    example: 'Hi 😀 → Hi',
  },
  emoji_to_text: {
    category: 'structural',
    description: 'Convert emoji to text descriptions',
    example: '😀 → smiling_face',
  },

  // ==== Character-Level ====
  remove_digits: {
    category: 'character',
    description: 'Remove all digits (Latin + Arabic-Indic)',
    example: 'Price 250 → Price',
  },
  remove_punctuation: {
    category: 'character',
    description: 'Remove punctuation marks',
    example: 'Hi, world! → Hi world',
  },
  remove_tashkeel: {
    category: 'character',
    description: 'Remove Arabic diacritics (harakat)',
    example: 'يَدْرُسُ → يدرس',
  },
  remove_tatweel: {
    category: 'character',
    description: 'Remove kashida (ـ)',
    example: 'الطـــلاب → الطلاب',
  },
  normalize_repetition: {
    category: 'character',
    description: 'Reduce repeated letters (3+)',
    example: 'يدرسوووون → يدرسون',
  },

  // ==== Normalization ====
  expand_contractions: {
    category: 'normalization',
    description: "Expand English contractions",
    example: "I'm → I am",
  },
  lowercase: {
    category: 'normalization',
    description: 'Convert to lowercase',
    example: 'HELLO → hello',
  },
  normalize_basic: {
    category: 'normalization',
    description: 'Basic Arabic normalization (alef, yaa, taa)',
    example: 'إأآا → ا',
  },
  normalize_arabic: {
    category: 'normalization',
    description: 'Basic Arabic normalization',
    example: 'ى → ي',
  },
  normalize_camel: {
    category: 'normalization',
    description: 'Advanced normalization (CAMeL Tools)',
    example: 'Comprehensive Unicode + char normalization',
  },

  // ==== Correction ====
  spell_correct: {
    category: 'correction',
    description: 'Auto-correct misspelled words',
    example: 'teh → the',
  },

  // ==== Filtering ====
  remove_stopwords: {
    category: 'filtering',
    description: 'Remove common stopwords',
    example: 'the cat sat → cat sat',
  },

  // ==== Morphological ====
  stem: {
    category: 'morphology',
    description: 'English Porter stemmer',
    example: 'running → run',
  },
  stem_isri: {
    category: 'morphology',
    description: 'Arabic ISRI stemmer (aggressive)',
    example: 'الطلاب → طلب',
  },
  stem_light: {
    category: 'morphology',
    description: 'Arabic light stemmer (Tashaphyne)',
    example: 'الطلاب → طلاب',
  },
  lemmatize: {
    category: 'morphology',
    description: 'English WordNet lemmatizer',
    example: 'better → good',
  },
  lemmatize_qalsadi: {
    category: 'morphology',
    description: 'Arabic Qalsadi lemmatizer',
    example: 'يدرسون → درس',
  },
  lemmatize_msa_camel: {
    category: 'morphology',
    description: 'CAMeL MSA morphological lemmatizer',
    example: 'يدرس → درس (no diacritics)',
  },
  lemmatize_egy_camel: {
    category: 'morphology',
    description: 'CAMeL Egyptian dialect lemmatizer',
    example: 'بيحب → حب',
  },

  // ==== Finalize ====
  normalize_whitespace: {
    category: 'finalize',
    description: 'Collapse multiple whitespaces',
    example: '  hi    world  → hi world',
  },
};