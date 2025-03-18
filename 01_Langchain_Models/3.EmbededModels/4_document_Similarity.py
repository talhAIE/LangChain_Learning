from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")  # Get the API key from .env file

embedding=GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=api_key)

pakistan_facts = [
    "Pakistan is the world's fifth-most populous country, with over 240 million people.",
    "Islamabad is the capital of Pakistan, while Karachi is its largest city.",
    "Pakistan is home to K2, the second-highest mountain in the world.",
    "The Indus River is the lifeline of Pakistan's agriculture and economy.",
    "Pakistan became the first Islamic nuclear power in 1998."
]

text=input("Enter your query: ")

embedding_docs=embedding.embed_documents(pakistan_facts)
embedding_query=embedding.embed_query(text)

scores=cosine_similarity([embedding_query],embedding_docs)[0] #adding [0] to get 1d vector
#now fetch relavant document
index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(pakistan_facts[index])
print(f"Similarity Score is {score}")
print(f"Query : {text}")


