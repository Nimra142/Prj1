from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import streamlit as st
from streamlit_chat import message
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(), override=True)

GOOGLE_API_KEY = "AIzaSyCU1f0kwHXEMapxO2EqEeh4deGjCzBAxQI"

st.set_page_config(
    page_title="chat gpt",
    page_icon="🤖"
)

st.subheader("Your Custom GPT" )

chat = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    temperature=0.9,api_key= GOOGLE_API_KEY 
    
)

if 'messages' not in st.session_state:
    st.session_state.messages=[]

with st.sidebar:
    system_message  = st.text_input(label="Assistant Role") 
    user_prompt = st.text_input(label="Enter Your Prompt") 
    if system_message:
        if not any(isinstance(x, SystemMessage) for x in  st.session_state.messages):
           st.session_state.messages.append(
               SystemMessage(content=system_message)
               )   

    if user_prompt:
        st.session_state.messages.append(
            HumanMessage(content=user_prompt)
        
        )
        with st.spinner('Thinking...'):
            response = chat(st.session_state.messages)  

        st.session_state.messages.append(AIMessage(content=response.content))    
                 
st.session_state.messages  
message("This is user", is_user=True)
message("This is chatgpt", is_user=False)

for i, msg in enumerate(st.session_state.messages[1:]):    
    if i%2==0:
        message(msg.content, is_user=True, key=f"{i}+😊") 
    else:
        message(msg.content, is_user=False, key=f"{i}+😎")  
    