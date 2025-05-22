from fastapi import FastAPI, Query, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.related import fetch_and_index_posts, get_similar_posts
from app.models import RelatedPost
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
def startup_event():
    fetch_and_index_posts()

@app.get("/related-posts", response_model=list[RelatedPost])
def related_posts(post_id: int, x_api_key: str = Header(default=None)):
    from app.config import API_KEY
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return get_similar_posts(post_id)

@app.get("/health")
def health():
    return {"status": "ok"}
