from crewai import Agent

def create_agents(tools):

    researcher = Agent(
        role="Tech Job Researcher",
        goal="Analyze job postings and extract requirements",
        tools=[tools["scrape_tool"], tools["search_tool"]],
        verbose=True,
        backstory="""Expert at extracting skills and requirements from job postings."""
    )

    profiler = Agent(
        role="Personal Profiler for Engineers",
        goal="Research applicants and build strong profiles",
        tools=[
            tools["scrape_tool"],
            tools["search_tool"],
            tools["read_resume"],
            tools["semantic_search_resume"]
        ],
        verbose=True
    )

    resume_strategist = Agent(
        role="Resume Strategist for Engineers",
        goal="Optimize resumes to match job requirements",
        tools=[
            tools["scrape_tool"],
            tools["search_tool"],
            tools["read_resume"],
            tools["semantic_search_resume"]
        ],
        verbose=True
    )

    interview_preparer = Agent(
        role="Engineering Interview Preparer",
        goal="Prepare interview questions and talking points",
        tools=[
            tools["scrape_tool"],
            tools["search_tool"],
            tools["read_resume"],
            tools["semantic_search_resume"]
        ],
        verbose=True
    )

    return researcher, profiler, resume_strategist, interview_preparer
