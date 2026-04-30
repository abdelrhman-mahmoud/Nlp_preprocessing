import React from 'react';
import { Globe, MessageCircle } from 'lucide-react';
import { LANGUAGES, DIALECTS } from '../utils/constants';

const LanguageBadge = ({ language, dialect, dialectScores }) => {
  if (!language || language === 'unknown') return null;

  const lang = LANGUAGES[language];
  const dialectInfo = dialect ? DIALECTS[dialect] : null;

  return (
    <div className="badges-row">
      <span className="badge">
        <Globe size={14} />
        {lang.flag} {lang.name}
      </span>

      {dialectInfo && (
        <span
          className="badge badge-dialect"
          style={{ borderLeft: `3px solid ${dialectInfo.color}` }}
        >
          <MessageCircle size={14} />
          {dialectInfo.flag} {dialectInfo.name} ({dialect})
        </span>
      )}

      {dialectScores && (
        <details className="badge badge-dialect" style={{ cursor: 'pointer' }}>
          <summary>📊 Dialect scores</summary>
          <div style={{ marginTop: '0.5rem', fontSize: '0.8rem' }}>
            {Object.entries(dialectScores).map(([d, score]) => (
              <div key={d}>
                {d}: {(score * 100).toFixed(1)}%
              </div>
            ))}
          </div>
        </details>
      )}
    </div>
  );
};

export default LanguageBadge;