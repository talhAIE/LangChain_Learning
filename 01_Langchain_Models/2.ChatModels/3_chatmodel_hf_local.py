from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline #used when we want to use localy hosted model
import os
os.environ['HF_HOME']='D:/Huggingface_cache'
#when we run this code we get download the model from huggingface and then run the code on our system
llm=HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_tokens=100
    )
)
model=ChatHuggingFace(llm=llm)
result=model.invoke('what is capital of pakistan')
print(result.content) 