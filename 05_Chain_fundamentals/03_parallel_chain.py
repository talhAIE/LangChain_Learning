"""
text->Notes and Quiz

Workflow : 
text -> Model 1 -> Notes
text -> Model 2 -> Quiz
Notes and Quiz -> Model 3 -> Merge output
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableParallel # runnable parallel : to run multiple chain in parallel 

load_dotenv()

model1=ChatOpenAI()
model2=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

# prompts

prompt_1=PromptTemplate(
    template="""
Generate short and simple notes for the following text \n {text} in basic level english with student nature 
""",
input_variables=['text']
)

prompt_2=PromptTemplate(
template="""
Generate a 5 short questions answers for the following text \n {text}
""",
input_variables=['text']
)

prompt_3=PromptTemplate(
template="""
merge the provided notes and quiz into a single document \n {notes} \n {quiz}
""",
input_variables=['notes','quiz']
)

# parser
parser=StrOutputParser()

# Parallel Chain
parallel_chain=RunnableParallel({
    'notes': prompt_1 | model1 | parser,
    'quiz' : prompt_2 | model2 | parser
})

# chain for merging notes and quiz
merge_chain=prompt_3 | model1 | parser

chain= parallel_chain | merge_chain

result=chain.invoke(input('Enter a text:'))
print(result)


# visualize the chain
chain.get_graph().print_ascii()
