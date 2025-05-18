from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(
    file_path='Langchain/07_RAG_Components/02_Text_Splitters/facemaskdetection.pdf'
)
 
docs=loader.load()
text="""

Artificial Intelligence (AI) is transforming the way we live and work. From self-driving cars to virtual assistants like Siri and Alexa, AI is becoming a part of everyday life. It helps businesses automate processes, doctors diagnose diseases, and teachers personalize learning. However, as AI technology grows, so do concerns about privacy, bias, and job displacement. Developers and researchers must ensure that AI is used ethically and responsibly. The future of AI holds great promise, but it also requires careful planning and regulation to ensure it benefits everyone.

"""

text_splitter=CharacterTextSplitter(
 
chunk_size=200, # number of characters
chunk_overlap=14, # number of characters to overlap 
separator='' # separator to split the text
)
# result=text_splitter.split_text(text) 
result=text_splitter.split_documents(docs) # list of chunks
# print(result)
print(len(result))
# print(result[0]) # each chunk will be a document object
print(result[0].page_content)
print('-'*10)
print(result[1].page_content)

# for the RAG based applications 10 to 20 % is a good number for chunk overlap
