from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools
from agno.models.openrouter import OpenRouter

from utils.settings import settings

researcher = Agent(
    name="Researcher",
    instructions='''
        Search Hacker News to find relevant stories and information 
        about the given topic. Return a summary of your findings.
        Make sure you dont ask any clarifying questions to the user.
        If the information is insufficient, make assumptions and
        move on.
    ''',
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
    tools=[HackerNewsTools()]
)

writer = Agent(
    name="Writer",
    instructions='''
        Using the research provided, write a clear and engaging article 
        about the topic.
    ''',
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    )
)