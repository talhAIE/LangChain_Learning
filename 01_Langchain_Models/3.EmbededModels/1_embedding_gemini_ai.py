from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")  # Get the API key from .env file

embedding=GoogleGenerativeAIEmbeddings(
    model='models/embedding-001',
    google_api_key=api_key
)

result=embedding.embed_query('what is the capital of pakistan')
print(result[:5])