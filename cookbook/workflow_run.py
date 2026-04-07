from agno.workflow import Workflow
from agents.workflow import researcher, writer

content_workflow = Workflow(
    name="Content Creation",
    steps=[researcher, writer]
)

content_workflow.print_response(
    "Write an article about AI trends. Focus on top 10 stories",
    stream=True
)