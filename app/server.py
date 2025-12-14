import fastapi
from fastapi import Body
from fastapi.middleware.cors import CORSMiddleware
from retriever import GetAnswer

app=fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
def send_response(data = Body(...)):
    print("Received query:", data)
    try:
        answer=GetAnswer(data['query'])
    except Exception as e:
        answer="Error processing the request"
        print("Error details:", e)
    return {"answer":answer}

    
