from services.pdf_loader import load_pdf_sections
from services.embeddings import embed_sections
from services.chroma_store import store_sections

def main():
    # Load PDF and extract sections
    sections = load_pdf_sections("ioop.pdf")
    print(f"Total sections found: {len(sections)}")
    print(sections[0])

    # Generate embeddings
    vectors = embed_sections(sections)
    print("Total vectors:", len(vectors))

    # Store in Chroma DB
    store_sections("University_IOOP_Sections", sections, vectors)
    print("Sections added to collection successfully.")

if __name__ == "__main__":
    main()
