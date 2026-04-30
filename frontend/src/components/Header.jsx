import React from 'react';
import { Sun, Moon, Github } from 'lucide-react';
import { useTheme } from '../context/ThemeContext';

const Header = () => {
  const { theme, toggle } = useTheme();

  return (
    <header className="header">
      <div className="header-content">
        <div className="logo">
          🧹 NLP Preprocessing Playground
        </div>
        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <button
            className="btn-icon"
            onClick={toggle}
            aria-label="Toggle theme"
            title={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
          >
            {theme === 'dark' ? <Sun size={20} /> : <Moon size={20} />}
          </button>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-icon"
            aria-label="GitHub"
          >
            <Github size={20} />
          </a>
        </div>
      </div>
    </header>
  );
};

export default Header;