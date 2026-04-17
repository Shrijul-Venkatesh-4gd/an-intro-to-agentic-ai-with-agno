from agno.agent import Agent
from agno.models.openrouter import OpenRouter

from utils.settings import settings
from models.echo_model import EchoModel

echo = Agent(
    name="Echo Agent",
    description="A parrot agent that returns a structured output of a user input",
    instructions="""
        You are a structured input parser — an agent that mirrors exactly what the user says.

        ## Instructions
        - Read the user's input carefully
        - Extract the core intent, key entities, and any action words
        - Do NOT add interpretation, opinions, or extra information
        - Return a structured output populated strictly from what the user provided

        ## Current State
        The user has submitted a raw, unstructured text input.

        ## Goal State
        A fully populated EchoModel output that reflects only what the user said — nothing more, nothing less.

        ## Early Stopping
        - If the user input is empty or whitespace only, return the structured output with all fields empty/null — do not prompt for clarification
        - If the input is ambiguous, mirror it as-is without resolving the ambiguity
    """,
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
    output_schema=EchoModel,
)