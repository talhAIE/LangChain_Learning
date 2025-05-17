from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader=DirectoryLoader(
    path='Langchain/07_RAG_Components/01_Document_Laoders/books', # path to the directory containing the pdf files
    glob='*.pdf', # glob pattern to match all th pdf files
    loader_cls=PyPDFLoader # loader class to use to load the pdf files
)

# docs=loader.load()
docs=loader.lazy_load()

# print(len(docs)) # it will print the number of documents in the directory in my case is 137
# print(docs[9].page_content)
# print(docs[9].metadata)


# why its taking time to load the code
# because it is loading all the pdf files in the directory
# we are loading all the pdf in the memory to perform operations
# what if we have 10000 pdf files in the directory
# it will take too much time to load all the pdf files in the memory also it will take too much memory
# so we need to use a better way to load the pdf files
# we have lazy loading in the langchain

# lazy loading

for doc in docs:
    print(doc.metadata)

# if we have a lot of documents in the directory we can use lazy loading
