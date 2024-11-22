from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models import Embedding
from app.database import init
import convex
import numpy as np

router = APIRouter()

@router.post("/embeddings/")
async def create_embedding(file: UploadFile = File(...)):
    # Baca file dan konversi ke embedding (misalnya, menggunakan numpy)
    contents = await file.read()
    vector = np.frombuffer(contents, dtype=np.float32).tolist()

    # Simpan embedding ke database menggunakan Convex
    client = convex.Client("https://your-convex-instance")
    embedding_id = client.insert("embeddings", {"vector": vector})

    # Simpan embedding ke database lokal
    embedding = await Embedding.create(vector=vector)
    return {"embedding_id": embedding_id, "embedding": embedding}

@router.get("/embeddings/{embedding_id}")
async def read_embedding(embedding_id: int):
    embedding = await Embedding.get(id=embedding_id)
    if embedding is None:
        raise HTTPException(status_code=404, detail="Embedding not found")
    return embedding