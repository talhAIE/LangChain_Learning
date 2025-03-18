from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint #used when we want to use api from hf
# from dotenv import load_dotenv

# load_dotenv()
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = ''
# we have to congifure the endpoint for the huggingface api
llm=HuggingFaceEndpoint(
    repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)
result=model.invoke('what is capital of pakistan')
print(result.content)