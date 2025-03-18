from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from typing import TypedDict,Annotated,Optional,Literal

Revie= '''
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver. 
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality. 
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow. 
Pros: 
Insanely powerful processor (great for gaming and productivity) 
Stunning 200MP camera with incredible zoom capabilities 
Long battery life with fast charging 
S-Pen support is unique and useful 
Cons: 
Bulky and heavy-not great for one-handed use 
Bloatware still exists in One UI 
Expensive compared to competitors 
I'''

load_dotenv()
api_key=os.environ["GOOGLE_API_KEY"] = os.getenv('GEMINI_API_KEY')
print(api_key)
model=ChatGoogleGenerativeAI(
    model='gemini-1.5-pro',
    google_api_key=api_key
)

# schema
class Review(TypedDict):
    key_themes: Annotated[list[str],'Write all key themes discussed int he Review']
    pros: Annotated[Optional[list[str]],'Write down all the pros inside the list']]
    cons: Annotated[Optional[list[str]],'Write down all the cons inside the list']
    summary: Annotated[str,'A brief Summary of the Review']
    sentiment: Annotated[Literal['pos','neg'],'Return Sentiment of the Review either Negative,Positive or Neutral']
    name: Annotated[Optional[str],'Write the name of the Reviewer']

strudctured_model=model.with_structured_output(Review)
result=strudctured_model.invoke('i am happy today and i am feeling good')
print(result)
print(result['summary'])
print(result['sentiment'])