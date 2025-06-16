import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
import streamlit as st

# Load environment variables from .env file
load_dotenv()
st.write('AI powered websites crawling - BrowserUse Package on Streamlit')
task_description = st.text_input("Enter the task you want to perform:")

# Set the Proactor event loop (mainly for Windows environments)
asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

async def main():
    agent = Agent(
        task=task_description,
        llm = AzureChatOpenAI(
        api_key = "082d3990364b4fadbc133fa8935b7905",
                        azure_endpoint = "https://becopenaidev7.openai.azure.com/",
                        model = "gpt-4o",
                        api_version="2024-02-01",
                        temperature = 0.
    # other params...
)

    )
    await agent.run()

# Run the asyncio event loop with the ProactorEventLoop policy

if(task_description):
    asyncio.run(main())
