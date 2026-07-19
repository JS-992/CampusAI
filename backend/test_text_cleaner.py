from app.services.document_processing.document_service import (
    extract_text_from_document
)

from app.services.document_processing.text_cleaner import (
    clean_text
)


file_path = "test_documents/OS.pdf"


raw_text = extract_text_from_document(file_path)

cleaned_text = clean_text(raw_text)


print("RAW TEXT")
print("=" * 50)
print(raw_text[:1000])


print("\n\nCLEANED TEXT")
print("=" * 50)
print(cleaned_text[:1000])