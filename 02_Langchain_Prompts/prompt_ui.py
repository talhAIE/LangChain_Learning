from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate,load_prompt

# Load environment variables
load_dotenv()

# Check if the API key is loaded
api_key = os.getenv("GEMINI_API_KEY")
st.header('Research-Tool') #title
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template=load_prompt('template.json')

# fill the place holders
# prompt =template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro',
                               google_api_key=api_key) #initialize the model


if st.button("summarize"):
    # result=model.invoke(prompt) #invoke the model
    # we did two time invoke instead of two time we can use chain concept to use one time invoke
    chain=template | model
    result=chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})
    st.write(result.content) #display the result
