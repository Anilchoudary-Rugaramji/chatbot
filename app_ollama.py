from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Set API keys from environment
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your_default_key")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv(
    "LANGCHAIN_API_KEY", "your_default_key")

# Define prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}"),
    ]
)

# Streamlit UI
st.title("LangChain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want to know about")

# Create LLM model instance
llm = ChatOpenAI(model="gpt-3.5-turbo",
                 openai_api_key=os.getenv("OPENAI_API_KEY"))
output_parser = StrOutputParser()

# Create processing chain
chain = prompt | llm | output_parser

# Process user input
if input_text:
    with st.spinner("Generating response..."):
        response = chain.invoke({"question": input_text})
        st.success(response)
