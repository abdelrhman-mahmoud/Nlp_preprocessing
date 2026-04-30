# 🎨 NLP Preprocessing Frontend

React playground for the NLP Preprocessing API.

---

## 📋 Requirements

- Node.js 18+ (recommended: v20)
- npm 8+
- Backend running at `http://localhost:5000`

---

## 🚀 Installation

### 1. Install Dependencies

\`\`\`bash
npm install --legacy-peer-deps
\`\`\`

> **Note:** Use `--legacy-peer-deps` because of `react-beautiful-dnd` deprecation.
> Alternatively, replace with `@hello-pangea/dnd` (drop-in replacement).

### 2. Configure Environment

\`\`\`bash
cp .env.example .env
\`\`\`

Edit `.env`:
\`\`\`env
REACT_APP_API_URL=http://localhost:5000/api
\`\`\`

### 3. Run Dev Server

\`\`\`bash
npm start
\`\`\`

App opens at **http://localhost:3000**

---

## 🏗️ Project Structure

\`\`\`
frontend/
├── public/
│   └── index.html
│
├── src/
│   ├── index.js                    # Entry point
│   ├── App.jsx                     # Main component
│   │
│   ├── components/                 # React components
│   │   ├── Header.jsx              # Logo + theme toggle
│   │   ├── TextInput.jsx           # Textarea with samples
│   │   ├── LanguageBadge.jsx       # Detected lang/dialect
│   │   ├── FunctionSelector.jsx    # Searchable checkbox grid
│   │   ├── PipelineBuilder.jsx     # Drag & drop reorder
│   │   ├── ControlPanel.jsx        # Run buttons + auto-order
│   │   ├── OutputDisplay.jsx       # Result + copy/download
│   │   └── HistoryViewer.jsx       # Step-by-step trace
│   │
│   ├── context/
│   │   └── ThemeContext.jsx        # Dark/light mode
│   │
│   ├── hooks/
│   │   ├── useDarkMode.js
│   │   └── useDebounce.js
│   │
│   ├── services/
│   │   └── api.js                  # axios API client
│   │
│   ├── utils/
│   │   ├── constants.js            # Languages, dialects, categories
│   │   └── functionDescriptions.js # Function metadata
│   │
│   └── styles/
│       ├── App.css                 # Main styles
│       ├── components.css          # Component styles
│       └── themes.css              # CSS variables
│
├── package.json
├── nginx.conf                      # Production nginx config
├── Dockerfile
└── .env.example
\`\`\`

---

## ✨ Features

### 🌐 Smart Language Detection
- Auto-detects English / Arabic as you type (debounced 600ms)
- Identifies Arabic dialect (MSA, EGY, GLF, LEV, NOR)
- Shows dialect confidence scores

### 🔧 Function Selection
- **Searchable** — find functions by name/description
- **Filter by category** — structural, character, normalization, etc.
- **Multi-select** with one-click select all/clear
- **Examples** shown for each function
- **Color-coded** categories

### 🔗 Pipeline Builder
- **Drag & drop** to reorder
- ↑ ↓ arrow buttons for keyboard users
- ✕ remove individual steps
- **Auto-order toggle** for best practices
- Numbered steps for clarity

### 🎯 Run Modes
- **Run Pipeline** — execute selected steps
- **Smart Run** — one-click auto pipeline (recommended defaults)

### 📊 Output
- Final result with **RTL support** for Arabic
- **Copy** to clipboard
- **Download** as `.txt` file
- **Step-by-step history** — see how text changes at each step

### 🎨 UI
- 🌓 **Dark / Light mode** with auto-detection (saved to localStorage)
- 📱 **Responsive** — works on mobile, tablet, desktop
- ⌨️ **Keyboard accessible**
- 🌍 **RTL support** for Arabic content
- 🎨 **CSS variables** for easy theming

---

## 🛠️ Tech Stack

| Library | Purpose | Version |
|---------|---------|---------|
| React | UI framework | 18.2 |
| @hello-pangea/dnd | Drag & drop | 16.5 |
| lucide-react | Icons | 0.294 |
| axios | HTTP client | 1.6 |
| react-scripts | Build tooling | 5.0.1 |

---

## 📜 Available Scripts

\`\`\`bash
# Start dev server (http://localhost:3000)
npm start

# Build for production (output: build/)
npm run build

# Run tests
npm test

# Eject from Create React App (irreversible)
npm run eject
\`\`\`

---

## 🎨 Theming

The app uses CSS variables defined in `src/styles/themes.css`:

\`\`\`css
:root {
  --accent: #6366f1;
  --bg-primary: #ffffff;
  --text-primary: #0f172a;
  /* ... */
}

[data-theme="dark"] {
  --accent: #818cf8;
  --bg-primary: #0f172a;
  --text-primary: #f1f5f9;
  /* ... */
}
\`\`\`

To customize:
1. Edit `themes.css`
2. Or create a new theme by adding `[data-theme="custom"] { ... }`

---

## 🔌 API Integration

The frontend talks to the Flask backend through `src/services/api.js`:

\`\`\`javascript
import { preprocess } from './services/api';

const result = await preprocess({
  text: "Hello world",
  language: "en",
  steps: ["remove_urls", "lowercase"],
  autoOrder: true,
});

console.log(result.output);
\`\`\`

### Available API Methods

| Method | Description |
|--------|-------------|
| `checkHealth()` | Server health check |
| `detectLanguage(text)` | Detect en/ar |
| `detectDialect(text)` | Identify Arabic dialect |
| `getFunctions(lang)` | List available functions |
| `preprocess({...})` | Run custom pipeline |
| `preprocessSmart(text)` | Auto pipeline |

---

## 🎬 User Flow

1. **User types text** in the textarea
2. App **auto-detects language** (after 600ms debounce)
3. If Arabic → **dialect identified** automatically
4. **Function list loaded** for the detected language
5. User **picks functions** (any order, any combination)
6. User **reorders** via drag & drop (or arrows)
7. User toggles **auto-order** if desired
8. User clicks **Run Pipeline** or **Smart Run**
9. **Output displayed** with copy/download buttons
10. **Step-by-step history** shows transformation

---

## 🐳 Docker

### Build
\`\`\`bash
docker build -t nlp-frontend .
\`\`\`

### Run
\`\`\`bash
docker run -p 3000:80 \\
  -e REACT_APP_API_URL=http://backend:5000/api \\
  nlp-frontend
\`\`\`

### Production
The Dockerfile uses multi-stage build:
1. **Stage 1**: `node:20-alpine` builds the React app
2. **Stage 2**: `nginx:alpine` serves the static files

Final image is **~50 MB**.

---

## 🐛 Troubleshooting

### `react-scripts: not found`
\`\`\`bash
rm -rf node_modules package-lock.json
npm cache clean --force
npm install --legacy-peer-deps
\`\`\`

### Cannot connect to backend
- Make sure backend is running at `http://localhost:5000`
- Check `.env` has correct `REACT_APP_API_URL`
- Restart `npm start` after editing `.env`

### CORS errors
Backend must have `flask-cors` enabled (already configured in `app.py`).

### Drag & drop not working
If using `react-beautiful-dnd` with React 18, switch to `@hello-pangea/dnd`:
\`\`\`bash
npm uninstall react-beautiful-dnd
npm install @hello-pangea/dnd
\`\`\`

Then update import in `PipelineBuilder.jsx`:
\`\`\`javascript
import { DragDropContext, Droppable, Draggable } from '@hello-pangea/dnd';
\`\`\`

---

## 📦 Build for Production

\`\`\`bash
npm run build
\`\`\`

Output goes to `build/`. Serve it with any static file server:

\`\`\`bash
# Using serve
npx serve -s build -l 3000

# Using nginx (production)
# (see nginx.conf in this repo)
\`\`\`

---

## 🎯 Customization

### Add a new sample text
Edit `src/components/TextInput.jsx`:
\`\`\`javascript
const SAMPLE_TEXTS = {
  en: "...",
  ar: "...",
  msa: "...",
  custom: "Your sample here", // ← add new
};
\`\`\`

### Add function description
Edit `src/utils/functionDescriptions.js`:
\`\`\`javascript
my_new_function: {
  category: 'normalization',
  description: 'What it does',
  example: 'input → output',
},
\`\`\`

### Change theme colors
Edit `src/styles/themes.css` — change the CSS variables.

---

## 🌍 Browser Support

- ✅ Chrome / Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari 14+
- ✅ Mobile browsers

---

## 📜 License

MIT