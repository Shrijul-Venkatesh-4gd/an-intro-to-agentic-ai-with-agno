from pydantic import BaseModel

class ChatbotModel(BaseModel):
    user_input: str
    output: str