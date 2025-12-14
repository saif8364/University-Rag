from config.chroma_client import get_chroma_client


def store_sections(collection_name: str, sections: list[str], vectors: list[list[float]]):
    client = get_chroma_client()
    collection = client.get_or_create_collection(name=collection_name)

    ids = [f"section_{i}" for i in range(len(sections))]

    collection.add(
        ids=ids,
        documents=sections,
        embeddings=vectors
    )

    return True
