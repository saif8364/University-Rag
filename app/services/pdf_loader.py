from langchain_community.document_loaders import PyPDFLoader
import re

def load_pdf_sections(file_path: str):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    full_text = "\n".join([doc.page_content for doc in docs])

    pattern = r"(?:^|\n)(SECTION\s+\d+:\s+[A-Z][A-Z\s\(\)-]+)"
    sections_raw = re.split(pattern, full_text)

    sections = []
    for i in range(1, len(sections_raw), 2):
        heading = sections_raw[i]
        content = sections_raw[i + 1] if i + 1 < len(sections_raw) else ""
        sections.append(heading + "\n" + content)

    return sections
