import fitz


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract all text from a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text as a single string.
    """

    document = fitz.open(file_path)

    extracted_text = []

    for page in document:
        page_text = page.get_text()
        extracted_text.append(page_text)

    document.close()

    return "\n".join(extracted_text)