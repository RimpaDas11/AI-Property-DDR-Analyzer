import pdfplumber

def extract_text(pdf_path):
    text_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            text_data.append({"page": page_num + 1, "text": text})
    return text_data
