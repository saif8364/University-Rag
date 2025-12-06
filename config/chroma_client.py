import chromadb

client = chromadb.CloudClient(
     api_key='ck-E155ZrhoEnT3TQY52fVMhDMvquYFTd5kWiWu9tC1cdtT',
  tenant='20ca8d4e-6760-4b80-8ef6-0382888ba3f4',
  database='University'
)

def get_chroma_client():
    return client
