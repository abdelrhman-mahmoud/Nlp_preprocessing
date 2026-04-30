# Models Directory

ملفات المصادر المخصصة (custom resources) اللي بتستخدمها الـ preprocessors.

## 📁 English (`/english`)

| File | Purpose |
|------|---------|
| `stopwords_custom.txt` | كلمات إضافية للستوبووردز (سطر لكل كلمة) |
| `spell_dict.pkl` | spell checker cached (auto-generated) |

## 📁 Arabic (`/arabic`)

| File | Purpose |
|------|---------|
| `stopwords_custom.txt` | ستوبووردز عربية إضافية (شامل العامية) |
| `slang_dict.json` | قاموس عامية → فصحى |
| `camel_cache/` | ملفات CAMeL Tools المؤقتة |

## ➕ كيف تضيف Resources جديدة؟

1. حط الفايل في الفولدر المناسب
2. حدّث `utils/file_loader.py` لو محتاج format جديد
3. الـ preprocessors بتلوّد الفايلات automatically عند الـ import