from langchain_huggingface import HuggingFaceEmbeddings

embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

def embed_sections(sections: list[str]):
    return embeddings_model.embed_documents(sections)
