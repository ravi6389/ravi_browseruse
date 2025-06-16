import asyncio
import httpx


# WARNING: Disable SSL verification globally (not safe for production!)
original_httpx_client = httpx.Client

class UnsafeClient(httpx.Client):
    def __init__(self, *args, **kwargs):
        kwargs['verify'] = False
        super().__init__(*args, **kwargs)

httpx.Client = UnsafeClient

from langchain_groq import ChatGroq



# from browser_use.browser import BrowserProfile, BrowserSession

from langchain.chains import LLMChain

from browser_use import Agent
# from browser_use.browser import BrowserProfile, BrowserSession
import os
import logging
from langchain_openai import AzureChatOpenAI
import certifi

import asyncio


import certifi

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import (
	BaseMessage,
	HumanMessage,
	SystemMessage,
)
# from langchain_openai import ChatOpenAI


# os.environ['CURL_CA_BUNDLE'] = ''
# os.environ['REQUESTS_CA_BUNDLE'] = ''
# os.environ['SSL_CERT_FILE'] = ''  

# os.environ['CURL_CA_BUNDLE'] = ''
# os.environ['SSL_CERT_FILE'] = 'C:\\Users\\RSPRASAD\\AppData\\Local\\.certifi\\cacert.pem'


# GROQ_API_KEY = "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"
# GROQ_API_KEY = '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'
# GROQ_API_KEY = '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'
GROQ_API_KEY = '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'
# GROQ_API_KEY = st.secrets['GROQ_API_KEY']
llm = ChatGroq(temperature=0.8, groq_api_key=GROQ_API_KEY, model_name="llama3-70b-8192")
# llm = AzureChatOpenAI(
#     api_key = "082d3990364b4fadbc133fa8935b7905",
#                         azure_endpoint = "https://becopenaidev7.openai.azure.com/",
#                         model = "gpt-4o",
#                         api_version="2024-02-01",
#                         temperature = 0.
#     # other params...
# )
# print(llm.invoke('hi'))

# browser_profile = BrowserProfile(
# 	# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
# 	executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
# 	user_data_dir='C:\\Users\\RSPRASAD\\AppData\\Local\\Google\\Chrome\\User Data',
# 	headless=False,
# )
# browser_session = BrowserSession(browser_profile=browser_profile)

async def main():
	logger = logging.getLogger(__name__)
	test_prompt = 'What is the capital of France? Respond with a single word.'
	test_answer = 'paris'
	llm = ChatGroq(temperature=0.8, groq_api_key=GROQ_API_KEY, model_name="llama3-70b-8192")
	try:
		# dont convert this to async! it *should* block any subsequent llm calls from running
		response = llm.invoke([HumanMessage(content=test_prompt)])  # noqa: ASYNC
		response_text = str(response.content).lower()
		logger.info(test_prompt)
		
		logger.info(response_text)
		
	except Exception as e:
		print(e)
	
	agent = Agent(
		task='Find todays DOW stock price',
		# llm=ChatOpenAI(model='gpt-4o'),
		llm = llm,
		# browser_session=browser_session,
	)

	await agent.run()
	# await browser_session.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	print('Welcome to test groq')
	
	asyncio.run(main())