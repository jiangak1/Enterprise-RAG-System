from fastapi import APIRouter,UploadFile,File
import os

from app.rag.loader import load_text
from app.rag.splitter import split_text
from app.rag.retriever import  retrieve
from app.rag.chat import ask_llm


router = APIRouter()

chunks_store=[]

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path =f"data/{file.filename}"

    with open(file_path,"wb") as f:
        f.write(await file.read())

    text = load_text(file_path)
    chunks=split_text(text)
    chunks_store.extend(chunks)
    return{
        "message":"success",
        "chunks":len(chunks)
    }
@router.get("/ask")
def ask(question:str):
    related_chunks=retrieve(question,chunks_store)
    context ="\n".join(related_chunks)
    answer=ask_llm(context,question)
    return {"answer":answer}