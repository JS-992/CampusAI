
import chromadb
def add_chunk_to_collection(
    chunk_id: str,
    embedding,
    document: str,
    metadata: dict
):

    collection.add(
        ids=[chunk_id],
        embeddings=[embedding.tolist()],
        documents=[document],
        metadatas=[metadata]
    )
def search_similar_chunks(
    query_embedding,
    n_results=3
):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    return results
def delete_chunk(chunk_id: str):
    collection.delete(
        ids=[chunk_id]
    )
def delete_material_chunks(material_id: int):

    results = collection.get()

    ids_to_delete = []

    for chunk_id in results["ids"]:

        if chunk_id.startswith(f"material_{material_id}_"):

            ids_to_delete.append(chunk_id)

    if ids_to_delete:

        collection.delete(ids=ids_to_delete)

        print(f"Deleted {len(ids_to_delete)} old vectors.")

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="campusai_materials"
)