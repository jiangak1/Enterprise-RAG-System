from openai import OpenAI
from app.core.config import API_KEY,BASE_URL

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)
def ask_llm(context,question):
    prompt=f"""
你是一个文档助手。
已知内容：
{context}
用户问题:
{question}
请基于已知内容回答。
"""
    response=client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    return response.choices[0].message.content

