from app.services.vector_store.chroma_service import search_similar_chunks
from app.services.llm.gemini_service import ask_gemini
from app.services.embedding.embedding_service import generate_embedding

def ask_question(question: str):
    query_embedding = generate_embedding(question)

    results = search_similar_chunks(query_embedding)

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    prompt = f"""
You are an AI tutor.

Answer ONLY using the study material below.

Study Material:

{context}

Question:
{question}

If the answer is not present in the material, say:
"I couldn't find this in the uploaded notes."
"""

    answer = ask_gemini(prompt)

    return answer