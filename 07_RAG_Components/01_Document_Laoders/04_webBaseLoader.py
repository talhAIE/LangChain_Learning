from langchain_community.document_loaders import WebBaseLoader # it is used to load the web pages
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()
parser=StrOutputParser()
prompt=PromptTemplate(
    template='Answer the following question \n {question} from the following text \n {context}',
    input_variables=['question','context']
)
url='https://www.amazon.com/MSI-GeForce-Ventus-Gaming-Graphics/dp/B0C7W8GZMJ/ref=sr_1_1?dib=eyJ2IjoiMSJ9.GUFWTvWxGJ-rkLZIQNXV_VsKk4m7M8y_BNsupOmqP6faDNXAhw61Yh6lMQhBrEM_KjqEeB41Mu2KSEYzUmAskB-aBjVKYT-Kf4WQGhqOceW7sGDMeb_WKbNSIVKlpK-is-jT5_TcV7JQfcJG7Vv1F0H8LlNvTEuvsG9mJdOE4ktcq7PVYtvEvERcIwqVJ6YKotA5auuLrLpsJefgycsuoOVjhmpSYqLdNp4bKENpN8Q.tTwf_FBUhzIYrkACLhovWxQshKpycCbP2O3TAjZyerA&dib_tag=se&keywords=rtx%2B4060&qid=1747457335&sr=8-1&th=1'
loader=WebBaseLoader(url) # with single url we will get only one document but we can pass list of urls to get multiple documents
docs=loader.load()

chain=prompt | model | parser

result=chain.invoke({'question' : input('Enter your question : '),'context' : docs[0].page_content})

print(result)

# project idea : chrome plugin user can talk with web pages and get the information
