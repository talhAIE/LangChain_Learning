from langchain_community.document_loaders import CSVLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template='''Please analyze this portion of the CSV data and provide key insights:
    {context}''',
    input_variables=['context']
)

loader = CSVLoader(file_path='Langchain/07_RAG_Components/01_Document_Laoders/gloabal.csv')
docs = loader.load()

# Process data in chunks of 100 rows
chunk_size = 100
all_analyses = []

for i in range(0, len(docs), chunk_size):
    chunk = docs[i:i + chunk_size]
    chunk_content = "\n".join([doc.page_content for doc in chunk])
    
    chain = prompt | model | parser
    chunk_analysis = chain.invoke({'context': chunk_content})
    all_analyses.append(chunk_analysis)
    print(f"Processed rows {i+1} to {min(i+chunk_size, len(docs))}")

# Combine all analyses
final_prompt = PromptTemplate(
    template='''Please provide a comprehensive summary of the following analyses:
    {analyses}''',
    input_variables=['analyses']
)

final_chain = final_prompt | model | parser
final_analysis = final_chain.invoke({'analyses': "\n\n".join(all_analyses)})
print("\nFinal Analysis:")
print(final_analysis)
