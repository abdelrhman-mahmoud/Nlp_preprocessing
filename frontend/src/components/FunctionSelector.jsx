import React, { useMemo, useState } from 'react';
import { Search, CheckSquare, Square } from 'lucide-react';
import { FUNCTION_DESCRIPTIONS } from '../utils/functionDescriptions';
import { FUNCTION_CATEGORIES } from '../utils/constants';

const FunctionSelector = ({ functions, selectedSteps, onToggle, onSelectAll, onClearAll }) => {
  const [search, setSearch] = useState('');
  const [categoryFilter, setCategoryFilter] = useState('all');

  const filtered = useMemo(() => {
    return functions.filter((fn) => {
      const meta = FUNCTION_DESCRIPTIONS[fn] || {};
      const matchSearch = fn.toLowerCase().includes(search.toLowerCase()) ||
                          (meta.description || '').toLowerCase().includes(search.toLowerCase());
      const matchCategory = categoryFilter === 'all' || meta.category === categoryFilter;
      return matchSearch && matchCategory;
    });
  }, [functions, search, categoryFilter]);

  const categories = useMemo(() => {
    const set = new Set();
    functions.forEach(fn => {
      const c = FUNCTION_DESCRIPTIONS[fn]?.category;
      if (c) set.add(c);
    });
    return Array.from(set);
  }, [functions]);

  return (
    <div className="section">
      <div className="section-title">
        🛠️ Available Functions ({functions.length})
        <span style={{
          marginInlineStart: 'auto',
          fontSize: '0.85rem',
          fontWeight: 'normal',
          color: 'var(--text-secondary)'
        }}>
          Selected: {selectedSteps.length}
        </span>
      </div>

      <div className="functions-toolbar">
        <div style={{ position: 'relative', flex: 1, minWidth: 200 }}>
          <Search size={16} style={{
            position: 'absolute',
            left: 10,
            top: '50%',
            transform: 'translateY(-50%)',
            color: 'var(--text-tertiary)'
          }} />
          <input
            type="text"
            placeholder="Search functions..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{
              width: '100%',
              padding: '0.5rem 0.75rem 0.5rem 2rem',
              border: '1px solid var(--border)',
              borderRadius: '6px',
              background: 'var(--bg-primary)',
              color: 'var(--text-primary)',
              fontSize: '0.9rem',
            }}
          />
        </div>

        <select
          value={categoryFilter}
          onChange={(e) => setCategoryFilter(e.target.value)}
          style={{
            padding: '0.5rem',
            border: '1px solid var(--border)',
            borderRadius: '6px',
            background: 'var(--bg-primary)',
            color: 'var(--text-primary)',
            fontSize: '0.9rem',
          }}
        >
          <option value="all">All categories</option>
          {categories.map(c => (
            <option key={c} value={c}>{FUNCTION_CATEGORIES[c]?.label || c}</option>
          ))}
        </select>

        <button className="btn-secondary" onClick={onSelectAll}>
          <CheckSquare size={16} /> Select all
        </button>
        <button className="btn-secondary" onClick={onClearAll}>
          <Square size={16} /> Clear
        </button>
      </div>

      <div className="functions-grid">
        {filtered.map((fn) => {
          const meta = FUNCTION_DESCRIPTIONS[fn] || {};
          const cat  = FUNCTION_CATEGORIES[meta.category];
          const isSelected = selectedSteps.includes(fn);

          return (
            <div
              key={fn}
              className={`function-card ${isSelected ? 'selected' : ''}`}
              onClick={() => onToggle(fn)}
            >
              <div className="function-card-header">
                <span className="function-name">{fn}</span>
                <input
                  type="checkbox"
                  className="function-checkbox"
                  checked={isSelected}
                  onChange={() => onToggle(fn)}
                  onClick={(e) => e.stopPropagation()}
                />
              </div>

              {cat && (
                <span
                  className="function-category"
                  style={{ background: cat.color + '22', color: cat.color }}
                >
                  {cat.label}
                </span>
              )}

              {meta.description && (
                <div className="function-description" style={{ marginTop: '0.5rem' }}>
                  {meta.description}
                </div>
              )}

              {meta.example && (
                <div className="function-example">{meta.example}</div>
              )}
            </div>
          );
        })}
      </div>

      {filtered.length === 0 && (
        <div className="pipeline-empty">No functions match your search.</div>
      )}
    </div>
  );
};

export default FunctionSelector;