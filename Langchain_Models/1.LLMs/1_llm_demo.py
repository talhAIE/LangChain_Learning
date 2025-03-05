
from dotenv import load_dotenv #to load environment variables
import os
load_dotenv() #load environment variables

api_key = os.getenv("GEMINI_API_KEY")  # Get the API key from .env file
print(api_key)
# Verify if API key is loaded
if api_key is None:
    raise ValueError("GEMINI_API_KEY is not set. Please check your .env file.")

from langchain_google_genai import GoogleGenerativeAI
llm = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    api_key=api_key
)

result=llm.invoke(input("Enter your text: "))
print(result)