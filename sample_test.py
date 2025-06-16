import os
from langchain import LLMChain
from langchain_groq import ChatGroq
from langchain import PromptTemplate

# Set up GROQ_API_KEY
GROQ_API_KEY = "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"

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize Groq
llm = ChatGroq(temperature=0.8, groq_api_key=GROQ_API_KEY, model_name="llama3-70b-8192")

# Define a simple prompt for AI explanation
prompt_template = PromptTemplate.from_template(
 template="Can you explain what AI is?",
 input_variables=[]
)

# Create LLMChain
llm_chain = LLMChain(
 llm=llm,
 prompt=prompt_template
)

# Run LLMChain
response = llm_chain.run()

# Print the response
print(response)