import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: { 'Content-Type': 'application/json' },
  timeout: 30000,
});

// ==================== API METHODS ====================

export const checkHealth = async () => {
  const { data } = await api.get('/health');
  return data;
};

export const detectLanguage = async (text) => {
  const { data } = await api.post('/detect-language', { text });
  return data;
};

export const detectDialect = async (text) => {
  const { data } = await api.post('/detect-dialect', { text });
  return data;
};

export const getFunctions = async (language) => {
  const { data } = await api.get(`/functions/${language}`);
  return data;
};

export const preprocess = async ({ text, language, steps, autoOrder = true }) => {
  const { data } = await api.post('/preprocess', {
    text,
    language,
    steps,
    auto_order: autoOrder,
  });
  return data;
};

export const preprocessSmart = async (text) => {
  const { data } = await api.post('/preprocess/smart', { text });
  return data;
};

export default api;