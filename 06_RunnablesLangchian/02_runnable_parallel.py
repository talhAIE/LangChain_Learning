from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

prompt1=PromptTemplate(
template="Generate a X(twitter) post on the following topic {topic}",
input_variables=['topic']
)
prompt2=PromptTemplate(
template="Generate a LinkedIn post on the following topic {topic}",
input_variables=['topic']
)

parser=StrOutputParser()

parallel_run=RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1,model,parser),
        'linkedin':RunnableSequence(prompt2,model,parser)
    }
)
result=parallel_run.invoke({"topic":"AI"})
print(result['tweet'])
print("--------------------------------")
print(result['linkedin'])