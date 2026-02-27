from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from backend.model import generate_response
from backend.db import save_chat

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
def home():
    with open("frontend/index.html") as f:
        return f.read()

@app.post("/chat")
def chat(req: ChatRequest):
    response = generate_response(req.message)
    save_chat(req.message, response)
    return {"response": response}
