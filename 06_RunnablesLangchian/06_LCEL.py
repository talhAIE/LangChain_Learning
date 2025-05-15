from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableBranch,RunnablePassthrough,RunnableLambda,RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Wite a complete report on the following topic {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Summarize the following report {text}",
    input_variables=['text']
)

parser=StrOutputParser()

model=ChatOpenAI()

report_gen=RunnableSequence(prompt1,model,parser)

def check_length(text:str)->bool:
    if len(text.split())>200:
        print(f"Report: {len(text.split())} words")
        print("Summarizing the report...")
        print('\n')
        return True

# branch_chain=RunnableBranch(
#     (lambda x:len(x.split())>200,RunnableSequence(prompt2,model,parser)),
#     RunnablePassthrough())
# branch_chain=RunnableBranch(
#     (RunnableLambda(check_length),RunnableSequence(prompt2,model,parser)),
#     RunnablePassthrough())
# final_chain=RunnableSequence(report_gen,branch_chain)
# result=final_chain.invoke({"topic":"AI"})
# print(result)

branch_chain=RunnableBranch(
    (check_length,prompt2 | model | parser),
    RunnablePassthrough())
final_chain=report_gen | branch_chain
result=final_chain.invoke({"topic":"AI"})
print(result)
