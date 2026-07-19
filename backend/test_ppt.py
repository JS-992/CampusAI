from app.services.document_processing.ppt_processor import (
    extract_text_from_ppt
)


file_path = "test_documents/OS unit 3.pptx"

text = extract_text_from_ppt(file_path)

print("Total characters:", len(text))

print(text)