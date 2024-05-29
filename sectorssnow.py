from dbfunctions import *
import keys
from imports import *


logo_path = '/Users/anishnavale/Desktop/GenAI Project/project/Images/Bucks.jpg'

# Function to add logo to the sidebar
def add_logo_to_sidebar():
    st.sidebar.image(logo_path, width=100, use_column_width=False)  # Adjust width as needed
    
# Initialize OpenAI client and Langchain chat model
llm = ChatOpenAI(openai_api_key=keys.get_openai_api_key())
output_parser = StrOutputParser()

llm1 = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.2, max_tokens=1024, api_key=keys.get_anthropic_api_key())
output_parser1 = StrOutputParser()

llm2 = ChatCohere(cohere_api_key=keys.get_cohere_api_key())
output_parser2 = StrOutputParser()

def Evaluate_answer(r, r1, r2, input):
    context = get_context()
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"As an unbiased world-class LLM response Evaluator. You have a response from ChatGPT: {r}, a response from Claude: {r1} and a response from Cohere: {r2}. These responses are for the prompt: {input} and is based on the data: {context}. If a response is not present, don't consider it."),
        ("user", "{input}")
        ])

    chain = prompt | llm | output_parser
    response = chain.invoke({"input": "Compare the response and tell me which response is better and why it is better in bullet points."})
    return response

# Function to process the chat
def process_chat(user_input):
    if user_input:
        context = get_context()
        # Adding context to the message
        prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a world-class financial assistant providing in-depth insights into company financial data, stock data and investment tips. Using the following information: {context}, answer questions with in-depth and holistic analysis of company financials, stock data, sentiment analysis and investment insights for tailored analysis."),
        ("user", "{input}")
        ])

        chain = prompt | llm | output_parser
        response = chain.invoke({"input": f"{user_input} Dive deeper into the analysis and provide deep insights in a structured way."})
        return response

def process_chat1(user_input):
    if user_input:
        context = get_context()
        # Adding context to the message
        prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a world-class financial assistant providing in-depth insights into company financials, stock data and investment tips. Using the following information: {context}, answer questions with in-depth and holistic analysis of company financials, stock data, sentiment analysis and investment insights for tailored analysis."),
        ("user", "{input}")
        ])

        chain = prompt | llm1 | output_parser1
        response = chain.invoke({"input": f"{user_input} Dive deeper into the analysis and provide deep insights in a structured way."})
        return response
    
def process_chat2(user_input):
    if user_input:
        context = get_context()
        # Adding context to the message
        prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a world-class financial assistant providing in-depth insights into company financial data, stock data and investment tips. Using the following information: {context}, answer questions with in-depth and holistic analysis of company financials, stock data, sentiment analysis and investment insights for tailored analysis."),
        ("user", "{input}")
        ])

        chain = prompt | llm2 | output_parser2
        response = chain.invoke({"input": f"{user_input} Dive deeper into the analysis and provide deep insights in a structured way."})
        return response
    
def parse_recommendations(text, available_stocks):
    recommendations = []
    for line in text.split('\n'):
        if ':' in line:
            stock, rationale = line.split(':', 1)
            if stock.strip() in available_stocks:  # Filter recommendations based on available stocks
                recommendations.append((stock.strip(), rationale.strip()))
    return recommendations


def get_available_stocks_from_snowflake():
    try:
        # Get Snowflake connection
        conn = keys.get_snowflake_conn()

        if conn is None:
            return "Error: Snowflake connection is not established."

        # Query to retrieve stock symbols and their sectors from the company_info table
        query = 'SELECT "ticker", "sector" FROM "company_info"'

        # Execute the query
        cursor = conn.cursor()
        cursor.execute(query)

        # Fetch the results
        rows = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Check if rows are fetched
        if not rows:
            return "Error: No data fetched from the company_info table."

        # Process the fetched data
        available_stocks = {}
        for row in rows:
            if isinstance(row, tuple) and len(row) == 2 and all(isinstance(val, str) for val in row):
                available_stocks[row[0]] = row[1]
            else:
                return "Error: Fetched data is not in the expected format."

        # Print available stocks and sectors
        print("Available Stocks and Sectors:")
        for stock, sector in available_stocks.items():
            print(f"{stock}: {sector}")

        return available_stocks

    except Exception as e:
        # Handle exceptions and return an error message
        return f"Error fetching available stocks: {e}"


def get_cohere_recommendations(risk_tolerance, investment_goals, investment_horizon, preferred_sectors):
    try:
        # Get available stocks and their sectors from Snowflake
        available_stocks = get_available_stocks_from_snowflake()
        
        if not isinstance(available_stocks, dict):
            return "Error: Available stocks data is not in the expected format."

        # Filter available stocks based on preferred sectors
        filtered_stocks = {}
        if available_stocks:
            for stock, sector in available_stocks.items():
                if sector in preferred_sectors:
                    filtered_stocks[stock] = sector

        if not filtered_stocks:
            return "Error: No stocks available in the preferred sectors."

        # Formulate the prompt with user profile, sector information, and available stocks
        prompt = f"""
        User Profile:
        - Risk Tolerance: {risk_tolerance}
        - Investment Goals: {', '.join(investment_goals)}
        - Investment Horizon: {investment_horizon} years
        - Preferred Sectors: {', '.join(preferred_sectors)}
        
        Available Stocks and Sectors:
        {', '.join([f"{stock} ({sector})" for stock, sector in filtered_stocks.items()])}
        
        Based on the available stocks and their sectors, along with the user profile provided above, please recommend suitable stocks and provide a detailed rationale for each recommended stock.
        
        Additionally, suggest the percentage of investment in each recommended stock in a different line.
        """

        # Invoke Cohere model with the prompt
        response = llm2.invoke(prompt)

        return response
        
    except Exception as e:
        # Handle exceptions and return an error message
        return f"Error: {e}"



def get_recommendations(risk_tolerance, investment_goals, investment_horizon, preferred_sectors):
    cohere_recommendations = get_cohere_recommendations(risk_tolerance, investment_goals, investment_horizon, preferred_sectors)
    return cohere_recommendations

def explain_recommendations(recommendations):
    explanations = []
    for stock, rationale in recommendations:
        explanation = f"{stock}: {rationale}"
        explanations.append(explanation)
    return explanations

def combine_recommendations(stored_data_recommendations, cohere_recommendations):
    # Combine recommendations from stored data and Cohere
    cohere_recommendations_list = cohere_recommendations.split(',')
    combined_recommendations = stored_data_recommendations + cohere_recommendations_list
    return combined_recommendations

# Main function to render app contents
def app_body():
    st.title("Buck$Buddy - Your AI-Powered Financial Assistant")

    # Session state to maintain context and responses
    if 'context' not in st.session_state:
        st.session_state['context'] = {}
    if 'response_gpt' not in st.session_state:
        st.session_state['response_gpt'] = ""
    if 'response_claude' not in st.session_state:
        st.session_state['response_claude'] = ""
    if 'response_cohere' not in st.session_state:
        st.session_state['response_cohere'] = ""

    # User input
    user_input = st.text_input("Ask a financial question:")

    # Setup subtabs within the main tab
    subtab1, subtab2, subtab3, subtab4 = st.tabs(["GPT", "Claude", "Cohere", "Evaluate Answers"])
    response = None
    response1 = None
    response2 = None

    with subtab1:
        if st.button("Ask GPT"):
            if user_input:
                response = process_chat(user_input)
                st.session_state['response_gpt'] = response
        st.write("GPT Response:", st.session_state['response_gpt'])

    with subtab2:
        if st.button("Ask Claude"):
            if user_input:
                response1 = process_chat1(user_input)
                st.session_state['response_claude'] = response1
        st.write("Claude Response:", st.session_state['response_claude'])

    with subtab3:
        if st.button("Ask Cohere"):
            if user_input:
                response2 = process_chat2(user_input)
                st.session_state['response_cohere'] = response2
        st.write("Cohere Response:", st.session_state['response_cohere'])

    with subtab4:
        if st.button("Evaluate"):
#            if response2 != None or response != None or response1 != None:
            st.session_state['Evaluation'] = Evaluate_answer(st.session_state['response_gpt'], st.session_state['response_claude'], st.session_state['response_cohere'], user_input)
            st.write("Evaluation:", st.session_state['Evaluation'])
#            else:
#                st.write("No reponse generated.")

    # Process and display the response
#    if user_input:
#        response = process_chat(user_input)
#        response1 = process_chat1(user_input)
#        response2 = process_chat2(user_input)
#        st.write("GPT:", response)
#        st.divider()
#        st.write("Claude:", response1)
#        st.divider()
#        st.write("Cohere:", response2)

    # Sidebar details
    st.sidebar.subheader("Current Available Companies for analysis:")
    companies = {
        "Apple", 
        "Microsoft", 
        "Adobe", 
        "Airbnb", 
        "Doordash", 
        "Boeing", 
        "Tesla", 
        "Google", 
        "Meta", 
        "Nvidia", 
        "Pfizer", 
        "Moderna", 
        "John Deere", 
        "FedEx", 
        "DHL", 
        "Disney", 
        "Netflix", 
        "PepsiCo", 
        "Nestle", 
        "Lockheed Martin"
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
        response = process_chat1(user_input1)
        st.write("Buddy:", response)

# Main function to render app contents
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
        response = process_chat2(user_input2)
        if response:
            response_text = response.strip()  # Get the text content
            st.write("Buddy:", response_text)


# Define a function for the Customized Recommendations tab

def recommendation_tab():
    st.subheader("Customized Stock Recommendations")
    # Collect user inputs
    risk_tolerance = st.selectbox('Select your risk tolerance:', ['High Risk', 'Medium Risk', 'Low Risk'])
    investment_goals = st.multiselect('Select your investment goals:', ['Short-term', 'Long-term', 'Retirement', 'Growth', 'Income'])
    preferred_sectors = st.multiselect('Select preferred sectors or industries:', ['Technology', 'Consumer Cyclical', 'Communication Services','Industrials','Consumer Defensive','Healthcare'])
    investment_horizon = st.slider('Select your investment horizon (in years):', 1, 30, 5)

    if st.button("Get Recommendations"):
        response = get_cohere_recommendations(risk_tolerance, investment_goals, investment_horizon, preferred_sectors)
        if response:
            if isinstance(response, str):
                st.write(response)  # If response is a string, directly display it
            else:
                recommendations = response.content.strip().split('\n')
                for recommendation in recommendations:
                    st.write(recommendation)
        else:
            st.write("No recommendations could be generated based on the inputs.")


# Set up tabs
tab1, tab2 = st.tabs(["Assistant", "Customize Recommendations"])

# Add logo to sidebar
add_logo_to_sidebar()

with tab1:
    app_body()

with tab2:
    recommendation_tab()

# Run the main application
st.write("")
