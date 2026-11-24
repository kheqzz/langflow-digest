# LangFlow Daily Digest - Project Rangkuman & Security Guide

## 1. INISIALISASI PROYEK LANGFLOW

### Setup Lingkungan
```bash
pip install langflow
docker run -p 7860:7860 mode/huggingflow:latest
http://localhost:7860
```

## 2. METHOD WAJIB & SERING DIGUNAKAN
| Method | Fungsi |
|--------|--------|
| `lf.load_flow(path)` | Muat flow JSON |
| `lf.run_flow(inputs)` | Jalankan flow |
| `lf.save_flow(name, flow)` | Simpan flow |
| `lf.create_component(type)` | Buat komponen |

## 3. KEAMANAN: MENCEGAH PROMPT INJECTION
```python
import re
from html import escape

class PromptInjectionGuard:
    def detect_injection(self, text):
        patterns = [
            r"(?i)(ignore.*(previous|prior))",
            r"(?i)(jailbreak)",
            r"(?i)(system.*prompt)",
        ]
        return any(re.search(p, text) for p in patterns)
    
    def sanitize(self, text):
        return escape(text)
```

## 4. RAG BOT
```python
class RAGChatbot:
    def __init__(self, vector_store, llm):
        self.retriever = vector_store.as_retriever(k=4)
        self.llm = llm
