import os
from google.adk.agents import LlmAgent
from .web_scraping_tool import scrape_website
from dotenv import load_dotenv

load_dotenv()


test_agent = LlmAgent(
    name="web_agent",
    model=os.environ.get("MODEL_NAME"),
    description="scrapes web for information",
    instruction="Assist user by providing information from provided webpage URL",
    tools=[scrape_website]
)

root_agent = test_agent
