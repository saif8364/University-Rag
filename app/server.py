import fastapi
app=fastapi.FastAPI()


@app.post("/")
def send_response():
    return {"message":"Hello from server!"}

@app.post("/query")
def send_response():
    return {"message":"query received!"}

