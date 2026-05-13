from openai import OpenAI
from app.core.config import API_KEY,BASE_URL
from app.rag.prompt import (RAG_PROMPT)
#------------------------------
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)
#------------------------------
def ask_llm(context,question):
    prompt=RAG_PROMPT.format(
        context=context,
        question=question,
    )
    response=client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    return response.choices[0].message.content

