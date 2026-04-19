import streamlit as st
from src.agent import create_agent
from src.memory import add_message, get_history, clear_history
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="AI Customer Support", page_icon="🤖")
st.title("🤖 AI Customer Support Agent")
st.caption("Powered by Claude + LangGraph")

if "agent" not in st.session_state:
    st.session_state.agent = create_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    add_message("human", prompt)
    result = st.session_state.agent.invoke({
        "messages": get_history()
    })
    response = result["messages"][-1].content
    add_message("ai", response)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)