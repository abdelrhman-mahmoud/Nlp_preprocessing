import React, { useState } from 'react';
import { Copy, Check, Download } from 'lucide-react';

const OutputDisplay = ({ output, language }) => {
  const [copied, setCopied] = useState(false);

  if (!output) return null;

  const dir = language === 'ar' ? 'rtl' : 'ltr';

  const handleCopy = () => {
    navigator.clipboard.writeText(output);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  const handleDownload = () => {
    const blob = new Blob([output], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `preprocessed_${Date.now()}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="section">
      <div className="section-title">✅ Final Output</div>

      <div
        className={`output-box ${language === 'ar' ? 'arabic-text' : ''}`}
        dir={dir}
      >
        {output}
      </div>

      <div className="output-actions">
        <button className="btn-secondary" onClick={handleCopy}>
          {copied ? <><Check size={16} /> Copied!</> : <><Copy size={16} /> Copy</>}
        </button>
        <button className="btn-secondary" onClick={handleDownload}>
          <Download size={16} /> Download .txt
        </button>
      </div>
    </div>
  );
};

export default OutputDisplay;