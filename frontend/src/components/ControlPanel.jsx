import React from 'react';
import { Play, Sparkles, Settings } from 'lucide-react';

const ControlPanel = ({
  autoOrder,
  setAutoOrder,
  onRun,
  onSmartRun,
  loading,
  disabled,
}) => (
  <div className="section">
    <div className="control-row">
      <label className="toggle-switch">
        <input
          type="checkbox"
          checked={autoOrder}
          onChange={(e) => setAutoOrder(e.target.checked)}
        />
        <Settings size={16} />
        <span>Auto-order steps (recommended)</span>
      </label>

      <div style={{ display: 'flex', gap: '0.5rem' }}>
        <button
          className="btn-secondary"
          onClick={onSmartRun}
          disabled={loading}
          title="Auto-detect language & apply default pipeline"
        >
          <Sparkles size={16} /> Smart Run
        </button>

        <button
          className="btn-primary"
          onClick={onRun}
          disabled={loading || disabled}
        >
          {loading ? (
            <><span className="loader" /> Processing...</>
          ) : (
            <><Play size={16} /> Run Pipeline</>
          )}
        </button>
      </div>
    </div>
  </div>
);

export default ControlPanel;