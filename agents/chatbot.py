from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.db.in_memory import InMemoryDb
from utils.settings import settings
from models.chatbot_model import ChatbotModel

# 1. Role
ROLE = "You are an expert chat assistant."

# 2. Instruction Set
INSTRUCTION_SET = [
    "Assist the user with any questions they have",
    "Keep responses professional and precise",
    "Be concise and to the point", 
    "summarize information when possible", 
    "limit responses to what is necessary to answer the question",
    "Do not provide more information than what is asked for",
    """Always return your response strictly in valid JSON format with the following structure:
        {
        "user_input": "<repeat the user's input here> str",
        "output": "<your response> str"
        }"""
]

# 3. Current State
CURRENT_STATE = [
    "You have access to user session memory",
    "Use prior conversation context when relevant"
]

# 4. Goal State
GOAL_STATE = [
    "Provide clear and accurate responses",
    "Ensure the answer directly resolves the user's query"
]

# 5. Guardrails
GUARDRAILS = [
    "Do not speculate if unsure; say 'I don’t know'",
    "Stay within the scope of the user’s question",
    "Avoid unnecessary elaboration",
    "Stop once the query is fully answered"
]


def build_instructions(role, instruction_set, current_state, goal_state, guardrails):
    return f"""
ROLE:
{role}

INSTRUCTION SET:
{chr(10).join(f"- {i}" for i in instruction_set)}

CURRENT STATE:
{chr(10).join(f"- {c}" for c in current_state)}

GOAL STATE:
{chr(10).join(f"- {g}" for g in goal_state)}

GUARDRAILS:
{chr(10).join(f"- {g}" for g in guardrails)}
"""

db = InMemoryDb()

chatbot = Agent(
    name="Chatbot Agent",
    description="A chatbot system backed by user session memory",
    instructions=build_instructions(
        ROLE,
        INSTRUCTION_SET,
        CURRENT_STATE,
        GOAL_STATE,
        GUARDRAILS
    ),
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
    output_schema=ChatbotModel,
    db=db,
    update_memory_on_run=True
)