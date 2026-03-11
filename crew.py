from crewai import Crew

def create_crew(agents, tasks):

    researcher, profiler, strategist, interviewer = agents

    research_task, profile_task, resume_task, interview_task = tasks

    crew = Crew(
        agents=[researcher, profiler, strategist, interviewer],
        tasks=[research_task, profile_task, resume_task, interview_task],
        verbose=True,
        tracing=True
    )

    return crew
