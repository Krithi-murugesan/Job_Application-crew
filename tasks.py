from crewai import Task

def create_tasks(researcher, profiler, strategist, interviewer):

    research_task = Task(
        description="""Analyze the job posting URL ({job_posting_url}) and extract
        key skills, qualifications, and experience.""",
        expected_output="Structured list of job requirements",
        agent=researcher,
        async_execution=True
    )

    profile_task = Task(
        description="""Compile professional profile using GitHub ({github_url})
        and personal write-up ({personal_writeup}).""",
        expected_output="Comprehensive candidate profile",
        agent=profiler,
        async_execution=True
    )

    resume_strategy_task = Task(
        description="""Tailor the resume using job requirements and profile.""",
        expected_output="Updated tailored resume",
        output_file="outputs/tailored_resume.md",
        context=[research_task, profile_task],
        agent=strategist
    )

    interview_task = Task(
        description="""Generate interview questions and talking points.""",
        expected_output="Interview preparation document",
        output_file="outputs/interview_materials.md",
        context=[research_task, profile_task, resume_strategy_task],
        agent=interviewer
    )

    return research_task, profile_task, resume_strategy_task, interview_task
