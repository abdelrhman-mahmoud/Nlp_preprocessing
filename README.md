# 🧹 NLP Preprocessing Web App

A full-stack web application for preprocessing **English** and **Arabic** (MSA + Dialectal) text with customizable, composable pipelines.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![React](https://img.shields.io/badge/react-18.2-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0-red.svg)

---

## ✨ Features

### 🌐 Multi-Language Support
- **English** preprocessing pipeline
- **Arabic** preprocessing pipeline (MSA + Dialectal)
- Auto language detection
- Arabic dialect identification: **MSA, Egyptian, Gulf, Levantine, Maghrebi**

### 🔧 Composable Pipelines
- Pick any combination of preprocessing functions
- Drag & drop to reorder steps
- Auto-ordering by best-practice sequence
- Smart Run mode — one-click auto pipeline

### 🇬🇧 English Functions
- HTML/URL/Emoji removal
- Contraction expansion (`I'm` → `I am`)
- Lowercase, digit, punctuation removal
- Letter repetition normalization (`Helloooo` → `Hello`)
- Spell correction
- Stopword removal
- Porter stemming
- WordNet lemmatization

### 🇸🇦 Arabic Functions
- Tashkeel (diacritics) removal
- Tatweel (kashida) removal
- Letter repetition normalization (`يدرسوووون` → `يدرسون`)
- Basic + CAMeL Tools normalization
- Stopword removal (custom + dialectal)
- ISRI + Tashaphyne stemmers
- Qalsadi lemmatizer
- **CAMeL morphological lemmatizer** (MSA + Egyptian)

### 🎨 Modern UI
- Dark / Light mode
- RTL support for Arabic
- Real-time language detection
- Step-by-step history viewer
- Copy & download output
- Responsive design

---

## 🏗️ Architecture

\`\`\`

nlp-preprocessing-app/
├── backend/              # Flask REST API
│   ├── api/              # Routes + detectors
│   ├── pipelines/        # Pipeline classes
│   ├── preprocessors/    # Modular preprocessors
│   ├── models/           # Custom resources
│   ├── utils/            # Logger, validators
│   ├── logs/             # Rotating logs
│   └── tests/            # Pytest tests
│
├── frontend/             # React app
│   ├── src/
│   │   ├── components/   # UI components
│   │   ├── hooks/        # Custom hooks
│   │   ├── context/      # Theme context
│   │   ├── services/     # API client
│   │   ├── styles/       # CSS
│   │   └── utils/        # Constants
│
├── notebooks/            # Jupyter test notebooks
├── docker-compose.yml    # Multi-container setup
└── README.md             # You are here
\`\`\`

---

## 🚀 Quick Start

### Option 1: Docker (Recommended)

# Clone the repo
\`\`\`
git clone https://github.com/abdelrhman-mahmoud/Nlp_preprocessing

cd Nlp_preprocessing

# Build & run everything

docker-compose up --build
\`\`\`

🎉 Open:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000/api

### Option 2: Manual Setup

#### Backend
\`\`\`
cd backend
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
camel_data -i light
cp .env.example .env
python app.py
\`\`\`

#### Frontend (in a new terminal)
\`\`\`bash
cd frontend
npm install --legacy-peer-deps
cp .env.example .env
npm start
\`\`\`

---

## 📡 API Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/api/health` | Health check |
| `POST` | `/api/detect-language` | Detect en/ar |
| `POST` | `/api/detect-dialect` | Identify Arabic dialect |
| `GET`  | `/api/functions/<lang>` | List available functions |
| `POST` | `/api/preprocess` | Run custom pipeline |
| `POST` | `/api/preprocess/smart` | Auto-detect + default pipeline |

### Example Request

\`\`\`bash
curl -X POST http://localhost:5000/api/preprocess \\
  -H "Content-Type: application/json" \\
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
\`\`\`

### Response
\`\`\`json
{
  "output": "درس طالب رائع",
  "language": "ar",
  "applied": ["remove_emoji", "remove_tashkeel", "normalize_repetition", ...],
  "history": [...],
  "dialect": {
    "top_dialect": "MSA",
    "scores": {"MSA": 0.92, "EGY": 0.04}
  }
}
\`\`\`

---

## 🛠️ Tech Stack

### Backend
- **Flask 3.0** — REST API
- **NLTK** — English stopwords, stemming, lemmatization
- **PyArabic** — Arabic char manipulation
- **Tashaphyne** — Arabic light stemming
- **Qalsadi** — Arabic lemmatization
- **CAMeL Tools** — Dialect ID + morphological analysis
- **langdetect** — Language identification

### Frontend
- **React 18** — UI framework
- **@hello-pangea/dnd** — Drag & drop
- **lucide-react** — Icons
- **axios** — API client
- **CSS variables** — Theming

### DevOps
- **Docker** + **docker-compose**
- **Nginx** for serving frontend

---

## 🧪 Testing

\`\`\`bash
# Backend tests
cd backend
pytest tests/ -v

# Frontend tests
cd frontend
npm test
\`\`\`

---

## 📓 Jupyter Notebook

Test the pipelines interactively:

\`\`\`bash
cd notebooks
jupyter notebook 01_complete_pipeline_test.ipynb
\`\`\`

---

## 🌍 Supported Arabic Dialects

| Code | Dialect | Region |
|------|---------|--------|
| MSA  | Modern Standard Arabic | Pan-Arab |
| EGY  | Egyptian | Egypt 🇪🇬 |
| GLF  | Gulf | Saudi, UAE, Kuwait, Qatar 🇸🇦 |
| LEV  | Levantine | Syria, Lebanon, Jordan, Palestine 🇱🇧 |
| NOR  | Maghrebi | Morocco, Algeria, Tunisia 🇲🇦 |

---

## 📷 Screenshots

> _Add screenshots of the UI here_

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) file.

---

## 🙏 Acknowledgments

- [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) for Arabic NLP
- [NLTK](https://www.nltk.org/) for English NLP
- [PyArabic](https://github.com/linuxscout/pyarabic) for Arabic utilities
- [Tashaphyne](https://github.com/linuxscout/tashaphyne) for Arabic stemming
- [Qalsadi](https://github.com/linuxscout/qalsadi) for Arabic lemmatization

---

## 📧 Contact

Built with ❤️ by **Abdelrhman**

For questions or suggestions, open an issue or reach out!
