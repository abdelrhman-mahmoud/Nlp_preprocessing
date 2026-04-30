import React from 'react';
import { LANGUAGES } from '../utils/constants';

const SAMPLE_TEXTS = {
  en: "I'm sooo excited to visit NYC! 🗽 Check https://example.com — it's amaaazing!!! Tickets cost \$250.",
  ar: "ازييك يا صاحبي 😄 هتيجي معانا النهاردة ولا ايه؟ السعر بقى 50 جنيه بس!",
  msa: "يَدْرُسُ الطُلّابُ في الجامِعَةِ بِجِدٍّ وَاجْتِهادٍ كُلَّ يَوْمٍ راااائع!",
};

const TextInput = ({ text, setText, language, maxLength = 100000 }) => {
  const dir = language === 'ar' ? 'rtl' : 'ltr';

  return (
    <div className="section">
      <div className="section-title">
        📝 Input Text
        <div style={{ marginInlineStart: 'auto', display: 'flex', gap: '0.5rem' }}>
          <button className="btn-secondary" onClick={() => setText(SAMPLE_TEXTS.en)}>
            🇬🇧 EN sample
          </button>
          <button className="btn-secondary" onClick={() => setText(SAMPLE_TEXTS.msa)}>
            🇸🇦 MSA sample
          </button>
          <button className="btn-secondary" onClick={() => setText(SAMPLE_TEXTS.ar)}>
            🇪🇬 EGY sample
          </button>
          <button className="btn-secondary" onClick={() => setText('')}>
            🗑️ Clear
          </button>
        </div>
      </div>

      <div className="text-input-wrapper">
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter English or Arabic text here..."
          dir={dir}
          maxLength={maxLength}
          rows={6}
          className={language === 'ar' ? 'arabic-text' : ''}
        />
        <span className="char-counter">
          {text.length} / {maxLength}
        </span>
      </div>
    </div>
  );
};

export default TextInput;