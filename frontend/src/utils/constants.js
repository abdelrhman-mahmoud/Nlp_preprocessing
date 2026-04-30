export const LANGUAGES = {
  en: { code: 'en', name: 'English', flag: '🇬🇧', dir: 'ltr' },
  ar: { code: 'ar', name: 'Arabic',  flag: '🇸🇦', dir: 'rtl' },
};

export const DIALECTS = {
  MSA: { name: 'Modern Standard Arabic', flag: '🇸🇦', color: '#3b82f6' },
  EGY: { name: 'Egyptian',                flag: '🇪🇬', color: '#f59e0b' },
  GLF: { name: 'Gulf',                    flag: '🇸🇦', color: '#10b981' },
  LEV: { name: 'Levantine',               flag: '🇱🇧', color: '#8b5cf6' },
  NOR: { name: 'Maghrebi (North Africa)', flag: '🇲🇦', color: '#ec4899' },
};

export const FUNCTION_CATEGORIES = {
  structural:    { label: '🏗️ Structural Cleanup',    color: '#6366f1' },
  character:     { label: '🔤 Character-Level',       color: '#0ea5e9' },
  normalization: { label: '✨ Normalization',          color: '#10b981' },
  correction:    { label: '✏️ Correction',             color: '#f59e0b' },
  filtering:     { label: '🚫 Filtering',              color: '#ef4444' },
  morphology:    { label: '🧬 Morphological',          color: '#8b5cf6' },
  finalize:      { label: '🎯 Finalize',               color: '#64748b' },
};