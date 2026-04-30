import React, { useEffect, useState, useCallback } from 'react';
import { ThemeProvider } from './context/ThemeContext';
import Header           from './components/Header';
import TextInput        from './components/TextInput';
import LanguageBadge    from './components/LanguageBadge';
import FunctionSelector from './components/FunctionSelector';
import PipelineBuilder  from './components/PipelineBuilder';
import ControlPanel     from './components/ControlPanel';
import OutputDisplay    from './components/OutputDisplay';
import HistoryViewer    from './components/HistoryViewer';
import { useDebounce }  from './hooks/useDebounce';
import {
  detectLanguage,
  detectDialect,
  getFunctions,
  preprocess,
  preprocessSmart,
  checkHealth,
} from './services/api';

function App() {
  // ==================== STATE ====================
  const [text, setText]                 = useState('');
  const [language, setLanguage]         = useState(null);
  const [dialect, setDialect]           = useState(null);
  const [dialectScores, setDialectScores] = useState(null);
  const [functions, setFunctions]       = useState([]);
  const [selectedSteps, setSelectedSteps] = useState([]);
  const [autoOrder, setAutoOrder]       = useState(true);
  const [output, setOutput]             = useState('');
  const [history, setHistory]           = useState([]);
  const [loading, setLoading]           = useState(false);
  const [detecting, setDetecting]       = useState(false);
  const [error, setError]               = useState(null);
  const [serverOnline, setServerOnline] = useState(true);

  const debouncedText = useDebounce(text, 600);

  // ==================== HEALTH CHECK ====================
  useEffect(() => {
    checkHealth()
      .then(() => setServerOnline(true))
      .catch(() => setServerOnline(false));
  }, []);

  // ==================== AUTO-DETECT LANGUAGE ====================
  useEffect(() => {
    if (!debouncedText.trim()) {
      setLanguage(null);
      setDialect(null);
      setDialectScores(null);
      setFunctions([]);
      return;
    }

    const detect = async () => {
      setDetecting(true);
      setError(null);
      try {
        const { language: lang } = await detectLanguage(debouncedText);
        setLanguage(lang);

        if (lang === 'en' || lang === 'ar') {
          const { functions: fns } = await getFunctions(lang);
          setFunctions(fns);

          if (lang === 'ar') {
            const d = await detectDialect(debouncedText);
            setDialect(d.top_dialect);
            setDialectScores(d.scores);
          } else {
            setDialect(null);
            setDialectScores(null);
          }
        }
      } catch (e) {
        console.error(e);
        setError('Failed to detect language. Is the backend running?');
        setServerOnline(false);
      } finally {
        setDetecting(false);
      }
    };

    detect();
  }, [debouncedText]);

  // ==================== HANDLERS ====================
  const toggleStep = useCallback((fn) => {
    setSelectedSteps((prev) =>
      prev.includes(fn) ? prev.filter((s) => s !== fn) : [...prev, fn]
    );
  }, []);

  const handleSelectAll = () => setSelectedSteps([...functions]);
  const handleClearAll  = () => setSelectedSteps([]);

  const handleRun = async () => {
    if (!text.trim() || selectedSteps.length === 0) return;
    setLoading(true);
    setError(null);
    try {
      const result = await preprocess({
        text,
        language,
        steps: selectedSteps,
        autoOrder,
      });
      setOutput(result.output || '');
      setHistory(result.history || []);

      // If backend reordered our steps, sync the UI
      if (autoOrder && result.order) {
        setSelectedSteps(result.order);
      }
    } catch (e) {
      const msg = e.response?.data?.error || 'Preprocessing failed';
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  const handleSmartRun = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setError(null);
    try {
      const result = await preprocessSmart(text);
      setOutput(result.output || '');
      setHistory(result.history || []);
      setSelectedSteps(result.applied || []);

      if (result.dialect) {
        setDialect(result.dialect.top_dialect);
        setDialectScores(result.dialect.scores);
      }
    } catch (e) {
      const msg = e.response?.data?.error || 'Smart preprocessing failed';
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  // ==================== RENDER ====================
  return (
    <ThemeProvider>
      <div className="app">
        <Header />

        <main className="container">
          {/* Server status warning */}
          {!serverOnline && (
            <div className="error-box">
              ⚠️ Cannot connect to backend at{' '}
              <code>{process.env.REACT_APP_API_URL || 'http://localhost:5000/api'}</code>.
              Make sure the Flask server is running.
            </div>
          )}

          {/* Error message */}
          {error && (
            <div className="error-box">
              ❌ {error}
              <button
                className="btn-icon"
                style={{ float: 'right', color: 'var(--error)' }}
                onClick={() => setError(null)}
              >
                ✕
              </button>
            </div>
          )}

          {/* Input section */}
          <TextInput
            text={text}
            setText={setText}
            language={language}
          />

          {/* Language badges */}
          {language && (
            <div className="section">
              <div className="section-title">
                🌐 Detected
                {detecting && (
                  <span className="loader" style={{
                    marginInlineStart: '0.5rem',
                    borderColor: 'var(--accent)',
                    borderTopColor: 'transparent',
                  }} />
                )}
              </div>
              <LanguageBadge
                language={language}
                dialect={dialect}
                dialectScores={dialectScores}
              />
            </div>
          )}

          {/* Function selector */}
          {functions.length > 0 && (
            <FunctionSelector
              functions={functions}
              selectedSteps={selectedSteps}
              onToggle={toggleStep}
              onSelectAll={handleSelectAll}
              onClearAll={handleClearAll}
            />
          )}

          {/* Pipeline builder */}
          {selectedSteps.length > 0 && (
            <PipelineBuilder
              steps={selectedSteps}
              setSteps={setSelectedSteps}
              autoOrder={autoOrder}
            />
          )}

          {/* Controls */}
          {language && (
            <ControlPanel
              autoOrder={autoOrder}
              setAutoOrder={setAutoOrder}
              onRun={handleRun}
              onSmartRun={handleSmartRun}
              loading={loading}
              disabled={selectedSteps.length === 0}
            />
          )}

          {/* Output */}
          <OutputDisplay output={output} language={language} />

          {/* History */}
          <HistoryViewer history={history} language={language} />

          {/* Welcome message */}
          {!text.trim() && (
            <div className="section" style={{ textAlign: 'center', padding: '3rem 1rem' }}>
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>👋</div>
              <h2 style={{ marginBottom: '0.5rem' }}>Welcome to NLP Preprocessing!</h2>
              <p style={{ color: 'var(--text-secondary)', maxWidth: 500, margin: '0 auto' }}>
                Enter English or Arabic text above to start.
                The app will auto-detect the language (and Arabic dialect),
                then let you build your custom preprocessing pipeline.
              </p>
              <div style={{
                display: 'flex',
                justifyContent: 'center',
                gap: '0.75rem',
                marginTop: '1.5rem',
                flexWrap: 'wrap',
              }}>
                <span className="badge">🇬🇧 English</span>
                <span className="badge">🇸🇦 MSA Arabic</span>
                <span className="badge">🇪🇬 Egyptian</span>
                <span className="badge">🇸🇦 Gulf</span>
                <span className="badge">🇱🇧 Levantine</span>
                <span className="badge">🇲🇦 Maghrebi</span>
              </div>
            </div>
          )}
        </main>

        {/* Footer */}
        <footer style={{
          textAlign: 'center',
          padding: '2rem 1rem',
          color: 'var(--text-tertiary)',
          fontSize: '0.85rem',
          borderTop: '1px solid var(--border)',
          marginTop: '2rem',
        }}>
          Built with ❤️ using React, Flask, NLTK, PyArabic, CAMeL Tools
        </footer>
      </div>
    </ThemeProvider>
  );
}

export default App;