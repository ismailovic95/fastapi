# 🧠 FastAPI AI Related Posts API

A semantic search API using FastAPI, FAISS, and sentence-transformers to serve related blog posts based on content similarity.

---

## 🚀 Features

- 🔍 Uses `sentence-transformers` to generate embeddings
- ⚡ Fast vector search with FAISS
- 🔗 Fetches real posts from WordPress
- 🔐 Secured with API Key
- 🌐 CORS support for frontend integration

---

## 🛠️ Requirements

- Python 3.8+
- pip

---

## 📦 Installation

```bash
git clone https://github.com/your-username/fastapi-ai-related.git
cd fastapi-ai-related
pip install -r requirements.txt
```

---

## 🧪 Run Locally

```bash
uvicorn main:app --reload
```

Then access:

- `http://localhost:8000/related-posts?post_id=1` with header `X-Api-Key: your-secret-token`
- `http://localhost:8000/health`

---

## 🐳 Docker (Optional)

```bash
docker build -t fastapi-ai-related .
docker run -d -p 8000:8000 fastapi-ai-related
```

---

## 🔐 Environment Configuration

Edit `app/config.py`:

```python
WP_API_URL = "https://yourdomain.com/wp-json/wp/v2/posts?...&_fields=id,title.rendered,content.rendered"
API_KEY = "your-secret-token"
```

---

## 🧱 Project Structure

```
.
├── main.py
├── requirements.txt
└── app/
    ├── config.py
    ├── models.py
    ├── faiss_index.py
    ├── related.py
    └── __init__.py
```

---

## 🧩 To-Do

- [ ] Schedule CRON to re-index new posts
- [ ] Add admin reload route
- [ ] Connect to Redis for persistent cache
