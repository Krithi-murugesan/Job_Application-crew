import os
from dotenv import load_dotenv

from tools.tools import load_tools
from agents.agents import create_agents
from tasks.tasks import create_tasks
from crew.crew_setup import create_crew

load_dotenv()

tools = load_tools()

agents = create_agents(tools)

tasks = create_tasks(*agents)

crew = create_crew(agents, tasks)

inputs = {
    "job_posting_url": "https://www.linkedin.com/jobs/...",
    "github_url": "https://github.com/Krithi-murugesan",
    "personal_writeup": """Krithika is an accomplished Software Engineering Leader
    with 11 years of experience..."""
}

result = crew.kickoff(inputs=inputs)

print(result)
