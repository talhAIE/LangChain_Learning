from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema 

from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()

# first we have to make a schema using ResponseSchema class

schema=[
    ResponseSchema(name='fact_1',description='fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='fact 3 about the topic'),
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="""
give me 3 facts about the topic{topic}\n{format_instruction}
""",
input_variables=['topic'],
partial_variables={'format_instruction': parser.get_format_instructions()}
)
# prompt=template.format(topic='black hole')
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(final_result)
# print(type(final_result))

chain=template | model | parser
result=chain.invoke({'topic':'black hole'})
print(result)


# disadvantage of structured output parser is we can't do data validation 
# for data validation we have to use pydantic parser 




