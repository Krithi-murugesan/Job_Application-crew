from crewai_tools import (
    FileReadTool,
    ScrapeWebsiteTool,
    MDXSearchTool,
    SerperDevTool
)

def load_tools():

    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    read_resume = FileReadTool(
        file_path='./data/Krithi_resume_ETL.md'
    )

    semantic_search_resume = MDXSearchTool(
        mdx='./data/Krithi_resume_ETL.md'
    )

    return {
        "search_tool": search_tool,
        "scrape_tool": scrape_tool,
        "read_resume": read_resume,
        "semantic_search_resume": semantic_search_resume
    }
