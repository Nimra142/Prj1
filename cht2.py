from langchain_google_genai import ChatGoogleGenerativeAI
#import google.generativeai as genai
#import time
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from streamlit_chat import message
import streamlit as st 
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv(), override=True)

GOOGLE_API_KEY="AIzaSyA38dCDXy0lxjOSw1hqt5_tT1Cz-A9WQKc"
# Streamlit page config
st.set_page_config(page_title='ChatGPT', page_icon="🤖")#

# Initialize chat model
chat =  ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0.5, 
    api_key=GOOGLE_API_KEY,
    max_output_tokens=150,
    max_retries=2,
    convert_system_message_to_human=True
)

# Initialize session state if not present
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""  # To hold user input and clear it after submission

# Sidebar for inputs
with st.sidebar:
    # Input for system message (Assistant's role)
    system_message = st.text_input(label="Assistant Role", placeholder="Define assistant's role")

    # Input for user prompt
    user_prompt = st.text_input(label="Enter your prompt", placeholder="Type your message here", 
                                value=st.session_state.user_input)

    # Add system message if provided and not already added
    if system_message:
        if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
            st.session_state.messages.append(SystemMessage(content=system_message))

    # Add human message and generate AI response
    if st.button('Send') and user_prompt:
        # Add user message
        st.session_state.messages.append(HumanMessage(content=user_prompt))

 # Generate AI response
        if st.session_state.messages:
            with st.spinner("Generating response..."):
                response = chat(st.session_state.messages)
                st.session_state.messages.append(AIMessage(content=response.content))

        # Clear user input after submission
        st.session_state.user_input = ""
# Display chat messages in the main interface
for msg in st.session_state.messages:
    if isinstance(msg, SystemMessage):
        message(f"**System**: {msg.content}", is_user=False)
    elif isinstance(msg, HumanMessage):
        message(f"**You**: {msg.content}", is_user=True)
    elif isinstance(msg, AIMessage):
        message(f"**AI**: {msg.content}", is_user=False)

for i,msg in enumerate(st.session_state.messages[1:]):
    if i%2==0:
        message(msg.content, is_user=True, key=f"{i}+😁")
    else:
        message(msg.content, is_user=False, key=f"{i}+😃")
     



