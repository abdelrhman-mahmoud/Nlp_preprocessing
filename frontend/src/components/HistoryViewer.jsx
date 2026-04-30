import React, { useState } from 'react';
import { ChevronDown, ChevronRight } from 'lucide-react';

const HistoryViewer = ({ history, language }) => {
  const [open, setOpen] = useState(true);

  if (!history?.length) return null;

  const dir = language === 'ar' ? 'rtl' : 'ltr';

  return (
    <div className="section">
      <div
        className="section-title"
        style={{ cursor: 'pointer' }}
        onClick={() => setOpen(!open)}
      >
        {open ? <ChevronDown size={20} /> : <ChevronRight size={20} />}
        📜 Step-by-Step History ({history.length} steps)
      </div>

      {open && (
        <div>
          {history.map((h, i) => (
            <div key={i} className="history-item">
              <div className="history-step">
                <span className="pipeline-item-number">{i}</span>
                {h.step}
              </div>
              <div
                className={`history-text ${language === 'ar' ? 'arabic-text' : ''}`}
                dir={dir}
              >
                {h.error ? (
                  <span className="history-error">⚠️ {h.error}</span>
                ) : (
                  h.text
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default HistoryViewer;