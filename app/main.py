from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from app.agents.chat_agent import ChatAgent

app = FastAPI()

chat_agent = ChatAgent()

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: ChatRequest):
    response = chat_agent.respond(request.message)

    return {
        "response": response
    }