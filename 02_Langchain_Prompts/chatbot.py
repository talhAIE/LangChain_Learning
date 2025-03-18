from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


# Load environment variables
load_dotenv()

# Check if the API key is loaded
api_key = os.getenv("GEMINI_API_KEY")

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro',
                               google_api_key=api_key) #initialize the model
chat_history=[
    SystemMessage(content='You are now a helping Assistant'),
]
#infinte loop unless user type exit
while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower()=='exit':
        break
    result=model.invoke(chat_history) #invoke the model
    chat_history.append(AIMessage(result.content))
    print('Bot:',result.content)
    # we have to maintain chathistory to maintain the context of the conversation
    # now the issue is we dont know which message is from user and which is from bot
    # langchain provide a way to maintain the context of the conversation using builint classes
    # langchian has three types of messages 1. UserMessage 2. BotMessage 3. SystemMessage
    # UserMessage: message from the user
    # BotMessage: message from the bot
    # SystemMessage: message from the system 

print(chat_history)

