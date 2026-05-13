from langchain_community.document_loaders import (WebBaseLoader)

def load_web(url):
    loader = WebBaseLoader(
        web_paths=[url]
    )
    document=loader.load()
    text="\n".join(
        [doc.page_content for doc in document]
    )
    return text