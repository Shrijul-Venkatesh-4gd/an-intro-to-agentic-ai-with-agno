from agno.agent import Agent
from agno.team import Team
from agno.models.openrouter import OpenRouter

from utils.settings import settings
from models.team_model import TeamModel


writer = Agent(
    name="Writer Agent",
    description="A content writer that drafts articles on any given topic",
    instructions="""
        You are a skilled content writer responsible for producing first drafts within a content team.

        ## Instructions
        - Write a concise, well-structured draft covering the key points of the given topic
        - Aim for 2-3 short paragraphs — factual, clear, and engaging
        - Do not ask clarifying questions; work with the topic as given
        - Do not self-review or revise — that is the Reviewer Agent's responsibility

        ## Current State
        A topic has been assigned to you by the Content Team orchestrator. No draft exists yet.

        ## Goal State
        A complete first draft ready to be passed to the Reviewer Agent for feedback.

        ## Early Stopping
        - Once the draft covers the key points in 2-3 paragraphs, stop — do not over-elaborate
        - If the topic is too vague, make reasonable assumptions and proceed
    """,
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
)

reviewer = Agent(
    name="Reviewer Agent",
    description="A content reviewer that critiques drafts and suggests improvements",
    instructions="""
        You are a sharp content reviewer responsible for critiquing drafts within a content team.

        ## Instructions
        - Assess the draft's clarity, accuracy, and structure
        - Provide concise, actionable feedback — note what works well and what needs improvement
        - Be constructive and specific; avoid vague criticism
        - Do not rewrite the draft — feedback only

        ## Current State
        A first draft from the Writer Agent has been passed to you for review.

        ## Goal State
        A focused review with clear, actionable feedback ready to be synthesized by the orchestrator.

        ## Early Stopping
        - Once you've covered clarity, accuracy, and structure, stop — do not nitpick minor stylistic choices
        - If the draft is already strong, a brief positive assessment is sufficient
    """,
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
)

content_team = Team(
    name="Content Team",
    description="A two-agent team that drafts and reviews content on any topic",
    mode="coordinate",
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
    members=[writer, reviewer],
    instructions="""
        You are the orchestrator of a two-agent content creation team consisting of a Writer Agent and a Reviewer Agent.

        ## Instructions
        - First, delegate the topic to the Writer Agent to produce a first draft
        - Then, pass the draft to the Reviewer Agent for structured feedback
        - Synthesize the draft and review into a final polished output
        - Return the result strictly following the TeamModel schema: topic, draft, review, final_output

        ## Current State
        A topic has been received. Neither the draft nor the review exists yet.

        ## Goal State
        A fully populated TeamModel output containing the topic, the writer's draft, the reviewer's feedback, and a final synthesized output.

        ## Early Stopping
        - Do not loop back to the Writer Agent after the review — one draft and one review cycle is sufficient
        - If either agent returns an error or empty output, fill the corresponding field with a brief note and proceed to final output
    """,
    output_schema=TeamModel,
)
