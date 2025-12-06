from config.chroma_client import get_chroma_client
from services.embeddings import embed_sections
from config.llm_client import get_llm_client
from langchain.messages import SystemMessage,HumanMessage


client= get_chroma_client();
collection=client.get_collection(name="University_IOOP_Sections")
model=get_llm_client()

query='Societies in university'
embedding=embed_sections([query])


results=collection.query(query_embeddings=embedding, n_results=2);
print(results)

system_message=SystemMessage(content="You are a helpful assistant that helps students to Know and Give relevent Answer to the question from this text: {results}.Be sure not to answer out of scope of the this")
messages=[
    system_message,
    HumanMessage("Based on the above text, answer the question: {query}.in simple and Short manner")
]

response=model.invoke(messages);
print(response)




