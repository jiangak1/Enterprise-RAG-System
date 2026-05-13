from fastapi import APIRouter,UploadFile,File
from langchain_community.callbacks.llmonitor_callback import user_ctx

from app.rag.loader import load_pdf,load_txt
from app.rag.splitter import split_text
from app.rag.vector_store import add_chunks_to_vectorstore
from app.rag.retriever import  retrieve
from app.rag.chat import ask_llm
from pydantic import BaseModel
from app.rag.web_loader import load_web
router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path =f"temp_{file.filename}"

    with open(file_path,"wb") as f:
        f.write(await file.read())

    if file.filename.endswith(".pdf"):

        text = load_pdf(file_path)

    elif file.filename.endswith(".txt"):
        text = load_txt(file_path)
    else:
        return {
            "error": "unsupported file type"
        }
    chunks=split_text(text)
    add_chunks_to_vectorstore(
        chunks,
        user_id="test_user",
        source=file.filename
        )
    return{
        "message":"success",
        "chunks":len(chunks)
    }

class URLRequest(BaseModel):
    url: str
@router.post("/upload_url")
def upload_web(request:URLRequest):
    text = load_web(request.url)
    chunks=split_text(text)
    add_chunks_to_vectorstore(chunks,
                              user_id="test_user",
                              source=request.url
                              )
    return{
        "message":"url upload success",
        "chunks":len(chunks)
    }
@router.get("/ask")
def ask(question:str):
    related_chunks=retrieve(question,
                            user_id="text_user"
                            )
    context ="\n".join(related_chunks)
    answer=ask_llm(context,question)
    return {
        "question":question,
        "answer":answer,
    "context":context,}