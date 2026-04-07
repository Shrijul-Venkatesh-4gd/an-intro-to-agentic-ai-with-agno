from agno.agent import Agent
from agno.models.google import Gemini

from utils.settings import settings
from models.echo_model import EchoModel

echo = Agent(
    name="Echo Agent",
    description="A parrot agent that returns a structured output of a user input",
    instructions="""
        You are a mimicker that takes a user input and returns a structured output 
        containing what you understood from the user's prompt
    """,
    model=Gemini(
        id="gemini-2.5-flash",
        api_key=settings.GEMINI_API_KEY
    ),
    output_schema=EchoModel,
)