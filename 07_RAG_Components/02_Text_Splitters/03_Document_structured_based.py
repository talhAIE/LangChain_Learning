from langchain.text_splitter import RecursiveCharacterTextSplitter , Language


code="""

import re
from typing import List

def split_into_paragraphs(text: str) -> List[str]:
    
    return [para.strip() for para in text.split('\n\n') if para.strip()]

def split_paragraph_into_sentences(paragraph: str) -> List[str]:
    # This simple regex may not handle all cases but works for general use
    return re.split(r'(?<=[.!?])\s+', paragraph)

# Dummy text with 5 paragraphs
dummy_text =""

# Split by paragraphs
paragraphs = split_into_paragraphs(dummy_text)

print("🔹 Paragraphs:")
for i, para in enumerate(paragraphs, 1):
    print(f"\n--- Paragraph {i} ---\n{para}")

# Further split the first paragraph into sentences
print("\n🔹 Sentences from Paragraph 1:")
sentences = split_paragraph_into_sentences(paragraphs[0])
for s in sentences:
    print(f"- {s}")

"""
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=150,
    chunk_overlap=0
)

chunks=splitter.split_text(code)

print(len(chunks))

print(chunks[0])
