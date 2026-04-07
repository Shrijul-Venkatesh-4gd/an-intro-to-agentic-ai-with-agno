from agno.agent import Agent
from agno.models.google import Gemini

from utils.settings import settings
from models.chatbot_model import ChatbotModel
from database.postgres import db


chatbot = Agent(
    name="Chatbot Agent",
    description="A chatbot system backed by user session memory",
    instructions='''
        You are an expert chat assistant. Your goal is to assist the
        user with any and all questions that they have. Make sure to
        keep your responses professional and precise. Do not provide
        more information than what is asked. Also ensure that you are
        polite and respectful in your tone, even when disagreeing.
    ''',
    model=Gemini(
        id="gemini-2.5-flash",
        api_key=settings.GEMINI_API_KEY
    ),
    output_schema=ChatbotModel,
    db=db,
    update_memory_on_run=True
)