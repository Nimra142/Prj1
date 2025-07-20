import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyA38dCDXy0lxjOSw1hqt5_tT1Cz-A9WQKc")  # Replace with your API key

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🤖 Chatbot with Gemini + Streamlit")
st.markdown("Ask anything below:")
with st.sidebar:
# Chat session state
 if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.history.append(("You", user_input))
    try:
        response = model.generate_content(user_input)
        st.session_state.history.append(("Gemini", response.text))
    except Exception as e:
        st.session_state.history.append(("Gemini", f"Error: {e}"))

# Display chat history
for sender, message in st.session_state.history:
    st.markdown(f"**{sender}:** {message}")

