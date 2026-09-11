from openai import OpenAI
from openai.types.beta import Agent

from app.prompts.chat_prompts import CAFE_SYSTEM_PROMPT

class ChatAgent:
    def __init__(self):
        self.client = OpenAI()

    def respond(self, user_message: str) -> str:
        response = self.client.responses.create(
            model="gpt-5.6",
            instructions=CAFE_SYSTEM_PROMPT,
            input=user_message,
        )

        return response.output_text