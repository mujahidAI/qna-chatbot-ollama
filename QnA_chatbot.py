import streamlit as st 
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import ollama
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up LangChain tracing environment variables for debugging and logging
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "QnA ChatBot with Ollama"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Define the base chat prompt with system and user messages
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

def generate_response(question, llm, temperature, max_tokens):
    """
    Generates a response from the selected LLM based on the user's question.

    Args:
        question (str): The user input question.
        llm (str): The name of the LLM model to be used.
        temperature (float): Sampling temperature to control response creativity.
        max_tokens (int): Maximum number of tokens to generate in the response.

    Returns:
        str: The model's generated answer.
    """
    # Initialize the Ollama language model
    llm = Ollama(model=llm)

    # Output parser to extract plain string output from the model
    output_parser = StrOutputParser()

    # Chain the prompt, model, and parser together
    chain = prompt | llm | output_parser

    # Execute the chain with the user's question
    answer = chain.invoke({'question': question})
    return answer

# Streamlit UI layout
st.title("Enhanced Q&A Chatbot With Ollama")

# Sidebar options for model selection and configuration
llm = st.sidebar.selectbox("Select Open Source model", [
    "gemma:2b",         # Google Gemma lightweight model
    "mistral",          # Fast, accurate small model
    "llama2:7b",        # Meta’s LLaMA 2, solid general-purpose model
    "llama3:8b",        # Updated Meta model, more capable
    "phi3:mini",        # Microsoft’s compact conversational model
    "dolphin-mixtral",  # Chat-optimized version of Mistral
    "openchat:7b",      # Tuned for conversation tasks
    "neural-chat",      # Intel's general chatbot model
    "starcoder2:3b"     # Optimized for code generation
])

# Sidebar sliders for temperature and token control
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Token", min_value=50, max_value=300, value=150)

# Main input area for user queries
st.write("Go ahead and ask me anything:")
user_input = st.text_input("You: ")

# Handle user input and generate a response
if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide a question to get started.")
