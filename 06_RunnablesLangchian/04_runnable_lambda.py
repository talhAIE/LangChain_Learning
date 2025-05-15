# from langchain.schema.runnable import RunnableLambda

# def word_count(text:str)->int:
#     return len(text.split()) # count the number of words in the text

# runnable_fun=RunnableLambda(word_count)
# print(runnable_fun.invoke("Yea you are right i am learning langchian currently"))

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnablePassthrough,RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

def word_count(text:str)->int:
    return len(text.split()) # count the number of words in the text
prompt1=PromptTemplate(
    template="""
Write a joke on the following topic {topic} must be short funny and in simple language
""",
input_variables=['topic']
)
parser=StrOutputParser()
joke_gen=RunnableSequence(prompt1,model,parser)
paralle_gen=RunnableParallel({
'joke':RunnablePassthrough(),
'word_count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_gen,paralle_gen)
result=final_chain.invoke({"topic":"AI"})
print(f"Joke:{result['joke']}")
print(f"Word Count:{result['word_count']}")