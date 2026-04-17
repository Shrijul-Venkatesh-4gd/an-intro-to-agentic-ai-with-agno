from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools
from agno.models.openrouter import OpenRouter

from utils.settings import settings

researcher = Agent(
    name="Researcher",
    instructions='''
        You are a research agent specialised in retrieving information from Hacker News.

        ## Instructions
        - Use the HackerNews tools to search for stories, comments, and discussions relevant to the given topic
        - Summarise your findings clearly — include key points, notable opinions, and relevant links
        - Do not ask clarifying questions under any circumstances
        - If results are sparse, make reasonable assumptions and proceed

        ## Current State
        A topic has been passed to you from the workflow. No research has been done yet.

        ## Goal State
        A structured research summary ready to be handed off to the Writer Agent.

        ## Early Stopping
        - Stop after retrieving sufficient results to write a meaningful summary (no need to exhaust all search results)
        - If Hacker News returns no results at all, return a brief note stating that and stop — do not loop
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
        You are a content writer that transforms research summaries into polished articles.

        ## Instructions
        - Use the research summary provided as your sole source of content
        - Write in a clear, engaging, and accessible tone
        - Structure the article with a short intro, key points, and a conclusion
        - Do not add facts or opinions not present in the research

        ## Current State
        A research summary from the Researcher Agent has been passed to you.

        ## Goal State
        A complete, well-structured article ready for the reader.

        ## Early Stopping
        - If the research summary is empty or states no results were found, return a one-line note and stop — do not fabricate content
    ''',
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    )
)