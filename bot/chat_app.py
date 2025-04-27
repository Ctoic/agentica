import streamlit as st
import requests

st.set_page_config(page_title="Llama3 Chat", page_icon="🦙")
st.title("Chat with Llama3 (Ollama)")

# To store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare request to Ollama API
    payload = {
        "model": "llama3",
        "messages": st.session_state.messages
    }

    try:
        # Send POST request to Ollama
        response = requests.post("http://localhost:11434/api/chat", json=payload)
        response.raise_for_status()
        data = response.json()

        # Get Llama3's reply
        bot_reply = data["message"]["content"]

        # Add bot reply to history
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        # Show bot reply
        with st.chat_message("assistant"):
            st.markdown(bot_reply)

    except Exception as e:
        st.error(f"Error contacting Ollama: {e}")
