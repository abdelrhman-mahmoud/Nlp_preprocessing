# NLP Preprocessing Web App

A full-stack web application for preprocessing **English** and **Arabic** (MSA + Dialectal) text through customizable, composable pipelines — built with Flask and React.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)](https://python.org)
[![React](https://img.shields.io/badge/react-18.2-blue.svg)](https://reactjs.org)
[![Flask](https://img.shields.io/badge/flask-3.0-red.svg)](https://flask.palletsprojects.com)

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
- [Tech Stack](#tech-stack)
- [Testing](#testing)
- [Arabic Dialect Support](#arabic-dialect-support)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Multi-Language Support
- English and Arabic (MSA + Dialectal) preprocessing pipelines
- Auto language detection
- Arabic dialect identification: MSA, Egyptian, Gulf, Levantine, Maghrebi

### Composable Pipelines
- Mix and match any preprocessing functions in any combination
- Drag and drop to reorder steps
- Auto-ordering by best-practice sequence
- **Smart Run** mode — one-click automatic pipeline

### English Preprocessing Functions
| Function | Description |
|----------|-------------|
| HTML / URL / Emoji removal | Strip web artifacts |
| Contraction expansion | `I'm` → `I am` |
| Lowercase | Normalize casing |
| Digit & punctuation removal | Clean non-alphabetic characters |
| Letter repetition normalization | `Helloooo` → `Hello` |
| Spell correction | Fix common spelling errors |
| Stopword removal | Remove high-frequency filler words |
| Porter stemming | Suffix-stripping stemmer |
| WordNet lemmatization | Dictionary-based lemmatizer |

### Arabic Preprocessing Functions
| Function | Description |
|----------|-------------|
| Tashkeel removal | Strip diacritical marks |
| Tatweel removal | Remove kashida elongation |
| Letter repetition normalization | `يدرسوووون` → `يدرسون` |
| Basic & CAMeL normalization | Standardize character variants |
| Stopword removal | Custom + dialectal stopword lists |
| ISRI & Tashaphyne stemmers | Lightweight Arabic stemmers |
| Qalsadi lemmatizer | Rule-based Arabic lemmatizer |
| CAMeL morphological lemmatizer | MSA + Egyptian dialect support |

### UI Highlights
- Dark / Light mode toggle
- RTL layout support for Arabic text
- Real-time language detection feedback
- Step-by-step processing history viewer
- One-click copy and download of output
- Fully responsive design

---

## Architecture

```
nlp-preprocessing-app/
├── backend/                  # Flask REST API
│   ├── api/                  # Routes and language detectors
│   ├── pipelines/            # Pipeline orchestration classes
│   ├── preprocessors/        # Modular, single-responsibility preprocessors
│   ├── models/               # Custom NLP resources
│   ├── utils/                # Logger, input validators
│   ├── logs/                 # Rotating log files
│   └── tests/                # Pytest test suite
│
├── frontend/                 # React application
│   └── src/
│       ├── components/       # Reusable UI components
│       ├── hooks/            # Custom React hooks
│       ├── context/          # Theme context provider
│       ├── services/         # Axios API client
│       ├── styles/           # Global CSS with variables
│       └── utils/            # Constants and helpers
│
├── notebooks/                # Jupyter notebooks for pipeline testing
├── docker-compose.yml        # Multi-container orchestration
└── README.md
```

---

## Quick Start

### Option 1: Docker (Recommended)

```bash
git clone https://github.com/abdelrhman-mahmoud/Nlp_preprocessing
cd Nlp_preprocessing
docker-compose up --build
```

Once running:
- **Frontend** → http://localhost:3000
- **Backend API** → http://localhost:5000/api

### Option 2: Manual Setup

**Backend**
```bash
cd backend
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
camel_data -i light
cp .env.example .env
python app.py
```

**Frontend** *(in a separate terminal)*
```bash
cd frontend
npm install --legacy-peer-deps
cp .env.example .env
npm start
```

---

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/health` | Health check |
| `POST` | `/api/detect-language` | Detect language (en / ar) |
| `POST` | `/api/detect-dialect` | Identify Arabic dialect |
| `GET` | `/api/functions/<lang>` | List available functions for a language |
| `POST` | `/api/preprocess` | Run a custom pipeline |
| `POST` | `/api/preprocess/smart` | Auto-detect language + run default pipeline |

### Example Request

```bash
curl -X POST http://localhost:5000/api/preprocess \
  -H "Content-Type: application/json" \
  -d '{
    "text": "يَدْرُسُ الطُلّابُ راااائع 📚",
    "language": "ar",
    "steps": [
      "remove_emoji",
      "remove_tashkeel",
      "normalize_repetition",
      "normalize_camel",
      "lemmatize_msa_camel"
    ],
    "auto_order": true
  }'
```

### Example Response

```json
{
  "output": "درس طالب رائع",
  "language": "ar",
  "applied": ["remove_emoji", "remove_tashkeel", "normalize_repetition", "normalize_camel", "lemmatize_msa_camel"],
  "history": [...],
  "dialect": {
    "top_dialect": "MSA",
    "scores": { "MSA": 0.92, "EGY": 0.04 }
  }
}
```

---

## Tech Stack

**Backend**
- [Flask 3.0](https://flask.palletsprojects.com) — REST API framework
- [NLTK](https://www.nltk.org/) — English stopwords, stemming, lemmatization
- [PyArabic](https://github.com/linuxscout/pyarabic) — Arabic character manipulation
- [Tashaphyne](https://github.com/linuxscout/tashaphyne) — Arabic light stemmer
- [Qalsadi](https://github.com/linuxscout/qalsadi) — Arabic lemmatizer
- [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) — Dialect ID + morphological analysis
- [langdetect](https://github.com/Mimino666/langdetect) — Language identification

**Frontend**
- [React 18](https://reactjs.org) — UI framework
- [@hello-pangea/dnd](https://github.com/hello-pangea/dnd) — Drag and drop
- [lucide-react](https://lucide.dev) — Icon library
- [axios](https://axios-http.com) — HTTP client
- CSS variables — Theming system

**DevOps**
- Docker + docker-compose
- Nginx for static frontend serving

---

## Testing

**Backend**
```bash
cd backend
pytest tests/ -v
```

**Frontend**
```bash
cd frontend
npm test
```

**Notebooks** — Test pipelines interactively:
```bash
cd notebooks
jupyter notebook 01_complete_pipeline_test.ipynb
```

---

## Arabic Dialect Support

| Code | Dialect | Region |
|------|---------|--------|
| MSA | Modern Standard Arabic | Pan-Arab |
| EGY | Egyptian | Egypt |
| GLF | Gulf | Saudi Arabia, UAE, Kuwait, Qatar |
| LEV | Levantine | Syria, Lebanon, Jordan, Palestine |
| NOR | Maghrebi | Morocco, Algeria, Tunisia |

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) — Arabic NLP toolkit
- [NLTK](https://www.nltk.org/) — English NLP foundation
- [PyArabic](https://github.com/linuxscout/pyarabic) — Arabic text utilities
- [Tashaphyne](https://github.com/linuxscout/tashaphyne) — Arabic stemming
- [Qalsadi](https://github.com/linuxscout/qalsadi) — Arabic lemmatization

---

Built with ❤️ by **Abdelrhman** — for questions or suggestions, open an issue or submit a PR.
