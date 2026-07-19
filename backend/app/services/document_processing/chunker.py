def split_text_into_chunks(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 100
) -> list[str]:

    if not text.strip():
        return []

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:

        end = start + chunk_size

        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start = end - overlap

    return chunks