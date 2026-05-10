from PyPDF2 import PdfFileReader

def load_text(file_path):
    with open(file_path, 'r',encoding="utf-8") as f:
        return f.read()

def load_pdf(file_path):
    reader = PdfFileReader(file_path)
    text=""
    for page in reader.pages:
        text += page.extractText()
    return text