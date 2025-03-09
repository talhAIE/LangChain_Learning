from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template=ChatPromptTemplate(
    [
        ('system','You are now a customer chatbot  agent'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human','{query}')
    ]
)

chat_history=[]
with open('Langchain_Prompts/chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

chat_template.invoke({'chat_history':chat_history,'query':'what is my refund status'})