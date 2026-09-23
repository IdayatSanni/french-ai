from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from app.services.conversation_service import ConversationService
from app.agents.chat_agent import ChatAgent

load_dotenv()

app = FastAPI()

chat_agent = ChatAgent()
conversation_service = ConversationService()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: ChatRequest):
    history = conversation_service.get_history(
        request.session_id
    )

    print(history)
    response = chat_agent.respond(
        request.message,
        history
    )

    conversation_service.add_message(
        request.session_id,
        "user",
        request.message
    )

    conversation_service.add_message(
        request.session_id,
        "assistant",
        response
    )

    return {
        "response": response
    }