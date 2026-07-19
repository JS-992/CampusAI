from app.services.document_processing.document_service import (
    extract_text_from_document
)


pdf_path = "test_documents/OS.pdf"

ppt_path = "test_documents/OS unit 3.pptx"


pdf_text = extract_text_from_document(pdf_path)

ppt_text = extract_text_from_document(ppt_path)


print("PDF TEXT")
print("=" * 50)
print(pdf_text[:500])


print("\nPPT TEXT")
print("=" * 50)
print(ppt_text[:500])