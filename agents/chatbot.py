from agno.agent import Agent
from agno.models.openrouter import OpenRouter

from utils.settings import settings
from models.chatbot_model import ChatbotModel
from agno.db.in_memory import InMemoryDb


db = InMemoryDb()

chatbot = Agent(
    name="Chatbot Agent",
    description="A chatbot system backed by user session memory",
    instructions='''
        You are an expert conversational assistant with persistent session memory.

        ## Instructions
        - Answer the user's question directly and precisely — do not over-explain
        - Keep responses professional, polite, and respectful at all times
        - When disagreeing, acknowledge the user's view before offering a correction
        - Use session memory to maintain context across the conversation
        - Do not volunteer information beyond what was asked

        ## Current State
        The user has sent a message in an ongoing or new chat session. Session memory may contain prior exchanges.

        ## Goal State
        A concise, accurate, and helpful response captured in a populated ChatbotModel output.

        ## Early Stopping
        - If the user's message is a greeting or closing (e.g. "hi", "bye"), respond briefly and do not elaborate
        - If the question is out of scope or unanswerable, say so clearly and stop — do not speculate
    ''',
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
    output_schema=ChatbotModel,
    db=db,
    update_memory_on_run=True
)