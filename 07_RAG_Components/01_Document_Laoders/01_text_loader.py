from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()
prompt=PromptTemplate(
    template="Wite a summary for the following poem- \n {poem}",
    input_variables=["poem"]
)
parser=StrOutputParser()

loader =TextLoader(
    file_path='Langchain/07_RAG_Components/01_Document_Laoders/aipoem.txt',
    encoding='utf-8'
) # TextLoader is a class that loads text files
docs=loader.load() # it will load the text file and return a list of documents

# print(docs)

# print(type(docs))

# print(len(docs))
# # extract the first document
# print(docs[0])
# print(type(docs[0]))
print(docs[0].page_content)
print(docs[0].metadata)



chain=prompt | model | parser
result=chain.invoke(docs[0].page_content)
print(result)