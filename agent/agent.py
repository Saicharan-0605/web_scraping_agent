from google.adk.agents import LlmAgent
from .web_scraping_tool import scrape_website


test_agent = LlmAgent(
    name="web_agent",
    model="gemini-2.5-flash",
    description="scrapes web for information",
    instruction="Assist user by providing information from provided webpage URL",
    tools=[scrape_website]
)

root_agent = test_agent
