# 🔌 NLP Preprocessing Backend

Flask REST API for English & Arabic text preprocessing with CAMeL Tools dialectal support.

---

## 📋 Requirements

- Python 3.10+
- pip
- ~3 GB free disk space (for CAMeL models)

---

## 🚀 Installation

### 1. Create Virtual Environment

\`\`\`bash
python3.10 -m venv venv
source venv/bin/activate     # Linux/Mac
# venv\\Scripts\\activate     # Windows
\`\`\`

### 2. Install Dependencies

\`\`\`bash
pip install --upgrade pip
pip install -r requirements.txt
\`\`\`

### 3. Download CAMeL Tools Models

\`\`\`bash
# Light (~200 MB) — recommended for development
camel_data -i light

# OR Full (~2 GB) — for all features
camel_data -i defaults
\`\`\`

### 4. Configure Environment

\`\`\`bash
cp .env.example .env
\`\`\`

Edit `.env` if needed:
\`\`\`env
DEBUG=True
HOST=0.0.0.0
PORT=5000
LOG_LEVEL=INFO
MAX_TEXT_LENGTH=100000
\`\`\`

### 5. Run

\`\`\`bash
python app.py
\`\`\`

Server runs at **http://localhost:5000**

---

## 📁 Project Structure

\`\`\`
backend/
├── app.py                          # Flask entry point
├── config.py                       # Configuration
├── requirements.txt
├── .env.example
│
├── api/                            # API layer
│   ├── routes.py                   # Endpoints
│   ├── language_detector.py        # EN/AR detection
│   └── dialect_detector.py         # Arabic dialect ID
│
├── pipelines/                      # Pipeline orchestration
│   ├── base_pipeline.py            # Auto-ordering logic
│   ├── english_pipeline.py
│   └── arabic_pipeline.py
│
├── preprocessors/                  # Preprocessing modules
│   ├── common/                     # Shared (URL, HTML, emoji...)
│   ├── english/                    # EN-specific
│   └── arabic/                     # AR-specific (incl. CAMeL)
│
├── models/                         # Custom resources
│   ├── english/
│   │   └── stopwords_custom.txt
│   └── arabic/
│       ├── stopwords_custom.txt
│       └── slang_dict.json
│
├── utils/                          # Utilities
│   ├── logger.py                   # Rotating logger
│   ├── validators.py
│   ├── exceptions.py
│   └── decorators.py
│
├── logs/                           # Rotating log files
│   ├── app.log
│   ├── api.log
│   ├── error.log
│   └── preprocessing.log
│
└── tests/                          # Pytest tests
    ├── test_api.py
    ├── test_english_pipeline.py
    └── test_arabic_pipeline.py
\`\`\`

---

## 📡 API Endpoints

### `GET /api/health`
Health check.

**Response:**
\`\`\`json
{
  "status": "ok",
  "supported_languages": ["en", "ar"],
  "supported_dialects": ["MSA", "EGY", "GLF", "LEV", "NOR"]
}
\`\`\`

---

### `POST /api/detect-language`
Detect English or Arabic.

**Request:**
\`\`\`json
{ "text": "Hello world" }
\`\`\`

**Response:**
\`\`\`json
{ "language": "en" }
\`\`\`

---

### `POST /api/detect-dialect`
Identify Arabic dialect.

**Request:**
\`\`\`json
{ "text": "ازيك يا صاحبي" }
\`\`\`

**Response:**
\`\`\`json
{
  "top_dialect": "EGY",
  "scores": {
    "EGY": 0.87,
    "LEV": 0.08,
    "MSA": 0.05
  }
}
\`\`\`

---

### `GET /api/functions/<language>`
List available preprocessing functions.

**Example:** `GET /api/functions/ar`

**Response:**
\`\`\`json
{
  "language": "ar",
  "count": 16,
  "functions": [
    "remove_html", "remove_urls", "remove_emoji",
    "remove_tashkeel", "remove_tatweel",
    "normalize_repetition", "normalize_camel",
    "remove_stopwords", "stem_isri", "stem_light",
    "lemmatize_qalsadi", "lemmatize_msa_camel",
    "lemmatize_egy_camel", "normalize_whitespace"
  ]
}
\`\`\`

---

### `POST /api/preprocess`
Run a custom pipeline.

**Request:**
\`\`\`json
{
  "text": "يَدْرُسُ الطُلّابُ راااائع 📚",
  "language": "ar",
  "steps": [
    "remove_emoji",
    "remove_tashkeel",
    "normalize_repetition",
    "lemmatize_msa_camel"
  ],
  "auto_order": true
}
\`\`\`

**Response:**
\`\`\`json
{
  "output": "درس طالب رائع",
  "language": "ar",
  "applied": [...],
  "skipped": [],
  "order": [...],
  "history": [...],
  "dialect": { "top_dialect": "MSA", "scores": {...} }
}
\`\`\`

---

### `POST /api/preprocess/smart`
Auto-detect + apply recommended pipeline.

**Request:**
\`\`\`json
{ "text": "ازيك يا صاحبي" }
\`\`\`

**Response:** Same shape as `/preprocess`.

---

## 🔧 Available Functions

### Common (English + Arabic)
| Function | Description |
|----------|-------------|
| `remove_html` | Strip HTML tags & entities |
| `remove_urls` | Remove URLs |
| `remove_emoji` | Remove emoji |
| `emoji_to_text` | Convert emoji → text |
| `remove_digits` | Remove all digits |
| `remove_punctuation` | Remove punctuation |
| `normalize_repetition` | Reduce repeated letters |
| `normalize_whitespace` | Collapse whitespace |

### English-only
| Function | Description |
|----------|-------------|
| `expand_contractions` | `I'm` → `I am` |
| `lowercase` | Convert to lowercase |
| `spell_correct` | Auto-correct spelling |
| `remove_stopwords` | Remove EN stopwords |
| `stem` | Porter stemmer |
| `lemmatize` | WordNet lemmatizer |

### Arabic-only
| Function | Description |
|----------|-------------|
| `remove_tashkeel` | Remove diacritics |
| `remove_tatweel` | Remove kashida |
| `normalize_basic` | Basic regex normalization |
| `normalize_camel` | CAMeL Tools normalization |
| `remove_stopwords` | Remove AR stopwords |
| `stem_isri` | ISRI stemmer (aggressive) |
| `stem_light` | Tashaphyne light stemmer |
| `lemmatize_qalsadi` | Qalsadi lemmatizer |
| `lemmatize_msa_camel` | CAMeL MSA lemmatizer |
| `lemmatize_egy_camel` | CAMeL Egyptian lemmatizer |

---

## 🧠 Auto-Ordering

Steps are auto-reordered by best-practice sequence:

\`\`\`
1. Structural cleanup        (HTML, URLs, emoji)
2. Character-level cleanup   (digits, punctuation, tashkeel)
3. Normalization             (case, basic + camel)
4. Spell correction
5. Stopword filtering
6. Morphological reduction   (stemming, lemmatization)
7. Final whitespace cleanup
\`\`\`

Disable with `"auto_order": false` to use exact user order.

---

## 🎨 Custom Resources

### Add custom stopwords

Edit `models/arabic/stopwords_custom.txt`:
\`\`\`
يلا
طب
ايوه
كده
\`\`\`

### Add slang/dialect mapping

Edit `models/arabic/slang_dict.json`:
\`\`\`json
{
  "ازيك": "كيف حالك",
  "ايه": "ماذا"
}
\`\`\`

Resources are auto-loaded at startup.

---

## 🧪 Testing

\`\`\`bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Specific test file
pytest tests/test_arabic_pipeline.py -v
\`\`\`

---

## 📊 Logging

Logs are rotated automatically (5 MB max, 5 backups).

| File | Purpose |
|------|---------|
| `logs/app.log` | General application logs |
| `logs/api.log` | API requests |
| `logs/preprocessing.log` | Pipeline executions |
| `logs/error.log` | Errors only |

---

## 🐳 Docker

\`\`\`bash
# Build
docker build -t nlp-backend .

# Run
docker run -p 5000:5000 \\
  -v $(pwd)/logs:/app/logs \\
  -v $(pwd)/models:/app/models \\
  nlp-backend
\`\`\`

---

## 🐛 Troubleshooting

### CAMeL models not loading
\`\`\`bash
camel_data -i light
# or
camel_data -i morphology-db-msa-r13
\`\`\`

### NLTK data missing
\`\`\`python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
\`\`\`

### Port 5000 already in use
\`\`\`bash
# Change in .env
PORT=5001
\`\`\`

---

## 🔒 Security Notes

- Set `DEBUG=False` in production
- Use a reverse proxy (Nginx) in production
- Add rate limiting (e.g., Flask-Limiter)
- Set `MAX_TEXT_LENGTH` to prevent DoS

---

## 📜 License

MIT