from dbfunctions import *
import keys
from imports import *

# Initialize OpenAI client and Langchain chat model
llm = ChatOpenAI(openai_api_key=keys.get_openai_api_key())
output_parser = StrOutputParser()

llm1 = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.2, max_tokens=1024, api_key=keys.get_anthropic_api_key())
output_parser1 = StrOutputParser()

llm2 = ChatCohere(cohere_api_key=keys.get_cohere_api_key())
output_parser2 = StrOutputParser()

# Function to process the chat
def process_chat_GPT(user_input):
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

def process_chat_Claude(user_input):
    if user_input:
        context = get_context()
        # Adding context to the message
        prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a world-class financial assistant providing in-depth insights into company financials, stock data and investment tips. Using the following information :{context}, answer questions with in-depth and holistic analysis."),
        ("user", "{input}")
        ])

        chain = prompt | llm1 | output_parser1
        response = chain.invoke({"input": f"{user_input} Dive deeper into the analysis and provide deep insights in a structured way."})
        return response
    
def process_chat_Cohere(user_input):
    if user_input:
        context = get_context()
        # Adding context to the message
        prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a world-class financial assistant providing in-depth insights into company financials, stock data and investment tips. Using the following information :{context}, answer questions with in-depth and holistic analysis."),
        ("user", "{input}")
        ])

        chain = prompt | llm2 | output_parser2
        response = chain.invoke({"input": f"{user_input} Dive deeper into the analysis and provide deep insights in a structured way."})
        return response

# Main function to render app contents
def app_body():
    st.title("Buck$Buddy - Your AI-Powered Financial Assistant")

    # Session state to maintain context
    if 'context' not in st.session_state:
        st.session_state['context'] = {}

    # User input
    user_input = st.text_input("Ask a financial question:")

    # Process and display the response
    if user_input:
        response = process_chat_GPT(user_input)
        response1 = process_chat_Claude(user_input)
        response2 = process_chat_Cohere(user_input)
        st.write("GPT:", response)
        st.divider()
        st.write("Claude:", response1)
        st.divider()
        st.write("Cohere:", response2)
        

    # Sidebar details
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

# Main function to render app contents
def app_body1():
    st.title("Buck$Buddy - Your AI-Powered Financial Assistant")

    # Session state to maintain context
    if 'context' not in st.session_state:
        st.session_state['context'] = {}

    # User input
    user_input1 = st.text_input("Ask a financial question to Claude:")

    # Process and display the response
    if user_input1:
        response = process_chat_Claude(user_input1)
        st.write("Buddy:", response)

# Main function to render app contents
def app_body2():
    st.title("Buck$Buddy - Your AI-Powered Financial Assistant")

    # Session state to maintain context
    if 'context' not in st.session_state:
        st.session_state['context'] = {}

    # User input
    user_input2 = st.text_input("Ask a financial question to Cohere:")

    # Process and display the response
    if user_input2:
        response = process_chat_Cohere(user_input2)
        st.write("Buddy:", response)

# Set up tabs
tab1, tab2, tab3 = st.tabs(["Chat GPT", "Claude", "Cohere"])

with tab1:
    app_body()

with tab2:
    app_body1()

with tab3:
    app_body2()

# Run the main application
st.write("Ask any financial questions to get tailored advice.")