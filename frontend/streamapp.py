import streamlit as st
import requests
st.title("CHATBOT  AI 🤖")
if "messages" not in st.session_state:
    st.session_state.messages=[]
user_input=st.chat_input("Ask anything.....")
if user_input:
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })

    response=requests.post(
        "http://127.0.0.1:8000/chat/",
        json={"message":user_input}
    )

    bot_reply=response.json()["response"]
    st.session_state.messages.append({
        "role":"assistant",
        "content":bot_reply
    })
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.write(msg['content'])