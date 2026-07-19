from app.services.document_processing.pdf_processor import (
    extract_text_from_pdf
)


file_path = "test_documents/OS.pdf"

text = extract_text_from_pdf(file_path)

print(text)