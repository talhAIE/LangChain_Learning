from langchain_huggingface import HuggingFaceEmbeddings
import os
os.environ['Embed_Models']='D:/Embedding_cache'

embedding=HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

text='Talha Abbasi'
docs=['what is the capital of pakistan','what is the capital of india']
result=embedding.embed_documents(docs)
# result=embedding.embed_query(text)
print(str(result))