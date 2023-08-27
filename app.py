import streamlit as st
from streamlit_chat import message
import llama

def clear_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Say something to get started!"}]

st.title("Good Doctor")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Say something to get started!"}]

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])

    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
    )

    b.form_submit_button("Send", use_container_width=True)

for index, msg in enumerate(st.session_state.messages):
    message(msg["content"], is_user=msg["role"] == "user", key=f"message_{index}")

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    response = llama.get_response(user_prompt)

    msg = {"role": "assistant", "content": response}

    st.session_state.messages.append(msg)

if len(st.session_state.messages) > 1:
    st.button('Clear Chat', on_click=clear_chat)
