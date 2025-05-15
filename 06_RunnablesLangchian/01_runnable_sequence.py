from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

prompt1=PromptTemplate(
    template="""
Write a joke on the following topic {topic} must be short funny and in simple language
""",
input_variables=['topic']
)

prompt2=PromptTemplate(
template="Categorize the following text in term of joke {text}",
input_variables=['text']
)

parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)
print(chain.invoke({"topic":"AI"}))

# joke=RunnableSequence(prompt1,model,parser).invoke({"topic":"AI"})
# category=RunnableSequence(prompt2,model,parser).invoke({"text":joke})

# print(joke)
# print(category)