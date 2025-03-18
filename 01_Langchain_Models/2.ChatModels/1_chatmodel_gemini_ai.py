# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# from dotenv import load_dotenv #to load environment variables

# load_dotenv() #load environment variables
# api_key=os.getenv("GEMINI_API_KEY") # Get the API key from .env file
# model=ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite',
#                              google_api_key=api_key,
#                              temperature=0.5,
#                              max_tokens=10)

# result=model.invoke('what is capital of islamabad is?')
# print(result.content)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke('What is the capital of India')

print(result.content)