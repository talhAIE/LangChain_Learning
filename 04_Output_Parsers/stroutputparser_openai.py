from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate


load_dotenv()

model=ChatOpenAI()

# 1st prompt-> detailed report
template1=PromptTemplate(
    template="""
write a detailed report on {topic}""",
input_variables=['topic']
)

# 2nd prompt-> summary
template2=PromptTemplate(
    template="""
write a 5 line summary on the following text. \n{text}""",
input_variables=['text']
)

prompt1=template1.invoke({'topic': 'black hole'})
print('--'*20)
print(prompt1)
result=model.invoke(prompt1)
print('--'*20)
print(result.content)

prompt2=template2.invoke({'text': result})
print('--'*20)
print(prompt2)
result2=model.invoke(prompt2)
print('--'*20)
print(result2.content)





