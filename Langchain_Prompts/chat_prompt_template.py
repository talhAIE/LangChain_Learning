from langchain_core.prompts import ChatPromptTemplate


chat_template=ChatPromptTemplate(
    [
        ('system','You are now a helping Assistant in {domain}'),
        ('human','what is {topic}, explain in simple terms')
    ]
)

prompt=chat_template.invoke(
    {
    'domain':'finance',
    'topic':'stock market'}
)

print(prompt)