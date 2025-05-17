from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(
    file_path='Langchain/07_RAG_Components/01_Document_Laoders/tesing.pdf'
)

docs=loader.load()

print(docs)
print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)

# There are more PDF loaders in the langchain

