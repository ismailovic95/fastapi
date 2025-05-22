import requests
from app.config import WP_API_URL
from app.faiss_index import build_index, search_similar

posts = []

def fetch_and_index_posts():
    global posts
    res = requests.get(WP_API_URL)
    wp_data = res.json()

    posts = [
        {
            "id": post["id"],
            "title": post["title.rendered"],
            "content": post["content.rendered"]
        } for post in wp_data
    ]

    corpus = [p["title"] + ". " + p["content"] for p in posts]
    metadata = [{"id": p["id"], "title": p["title"]} for p in posts]
    build_index(corpus, metadata)

def get_similar_posts(post_id):
    query_post = next((p for p in posts if p["id"] == post_id), None)
    if not query_post:
        return []
    query_text = query_post["title"] + ". " + query_post["content"]
    similar = search_similar(query_text)
    return [s for s in similar if s["id"] != post_id]
