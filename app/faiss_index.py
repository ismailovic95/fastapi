import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = None
embeddings = None
metadata = []

def build_index(corpus, meta):
    global index, embeddings, metadata
    metadata = meta
    embeddings = model.encode(corpus, convert_to_numpy=True)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

def search_similar(query_text, top_k=5):
    query_embedding = model.encode([query_text])[0]
    _, indices = index.search(np.array([query_embedding]), k=top_k)
    return [metadata[i] for i in indices[0]]
