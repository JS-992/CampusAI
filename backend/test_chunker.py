from app.services.document_processing.document_service import (
    extract_text_from_document
)

from app.services.document_processing.text_cleaner import (
    clean_text
)

from app.services.document_processing.chunker import (
    split_text_into_chunks
)


file_path = "test_documents/OS.pdf"


raw_text = extract_text_from_document(file_path)

cleaned_text = clean_text(raw_text)

chunks = split_text_into_chunks(
    cleaned_text,
    chunk_size=1000,
    overlap=100
)


print("Total chunks:", len(chunks))


for index, chunk in enumerate(chunks):

    print("\n")
    print("=" * 60)
    print(f"CHUNK {index + 1}")
    print("=" * 60)

    print(chunk[:300])