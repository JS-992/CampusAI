import re


def clean_text(text: str) -> str:
    """
    Clean extracted document text.

    Removes excessive whitespace while preserving
    the original meaning of the content.
    """

    # Remove spaces and tabs at the beginning/end of each line
    text = "\n".join(
        line.strip()
        for line in text.splitlines()
    )

    # Replace 3 or more consecutive newlines with 2 newlines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Replace multiple spaces with a single space
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()