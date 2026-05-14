from langchain_core.runnables import history
from app.core.logger import logger
from openai import OpenAI, responses
from app.core.config import API_KEY,BASE_URL
from app.rag.prompt import (RAG_PROMPT)
from app.rag.memory import (save_message,get_message)
#------------------------------
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)
#------------------------------
def ask_llm(
        user_id,
        question,
        context
):
    history=get_message(user_id)
    prompt=RAG_PROMPT.format(
        context=context,
        question=question,
    )
    message=history+[
        {
            "role":"user",
            "content":prompt
        }
    ]
    logger.info(
        f"user question: {question}"
    )
    response=client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=message
    )
    answer=response.choices[0].message.content
    save_message(
        user_id,
    "user",
        question
        )
    save_message(
        user_id,
        "assistant",
        answer
    )
    logger.info(
        f"llm answer: {answer}"
    )
    return answer