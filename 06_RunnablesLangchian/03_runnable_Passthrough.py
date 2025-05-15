from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel
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
template="Categorize the following joke {text}",
input_variables=['text']
)

parser=StrOutputParser()

joke_gen=RunnableSequence(prompt1,model,parser)
parallel_run=RunnableParallel({
    'joke':RunnablePassthrough(),
    'category':RunnableSequence(prompt2,model,parser)})

final_chain=RunnableSequence(joke_gen,parallel_run)
result=final_chain.invoke({"topic":"AI"})
print(f"Joke:{result['joke']}")
print(f"Category:{result['category']}")