import dbfunctions
import keys
from imports import *

import streamlit as st
from openai import OpenAI
#from langchain_openai import ChatOpenAI
#from langchain.utilities import ChatSession
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas

# Initialize OpenAI client and Langchain chat model
llm = ChatOpenAI(openai_api_key=keys.get_openai_api_key())
output_parser = StrOutputParser()

def get_context():
    conn = keys.get_snowflake_conn()
    cur = conn.cursor()
    sql = 'select * from "context_data"'
    cur.execute(sql)
    context = cur.fetch_pandas_all()
    return context

# Streamlit UI
st.title("Buck$Buddy - Your AI-Powered Financial Assistant")

# Session state to maintain context
if 'context' not in st.session_state:
    st.session_state['context'] = {}


# User input
user_input = st.text_input("Ask a financial question:")

# Function to process the chat
def process_chat(user_input):
    if user_input:
        context = get_context()
        # Adding context to the message
        prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a world-class financial assistant providing in-depth insights into company financials, stock data and investment tips. Using the following information :{context}, answer questions with in-depth and holistic analysis."),
        ("user", "{input}")
        ])

        chain = prompt | llm | output_parser
        response = chain.invoke({"input": f"{user_input} Dive deeper into the analysis and provide deep insights in a structured way."})
        return response

# Process and display the response
if user_input:
    response = process_chat(user_input)
    st.write("Buddy:", response)

# Set sidebar title
#st.sidebar.title("BUCKSBUDDY - Your AI-Powered Financial Navigator")

# Add a section for available companies
st.sidebar.subheader("Current Available Companies for analysis:")
companies = {
    "AAPL": "Apple",
    "GOOGL": "Alphabet Inc. (Google)",
    "MSFT": "Microsoft",
    "ADBE": "Adobe",
    "TSLA": "Tesla",
    "ABNB": "Airbnb",
    "DASH": "DoorDash",
    "BA": "Boeing",
    "META": "Meta Platforms Inc. (formerly Facebook)",
    "NVDA": "NVIDIA"
}


# Display the list of companies
for company in companies:
    st.sidebar.write(company)

# Run the application
st.write("Ask any financial questions to get tailored advice.")

