from langchain_core.messages import HumanMessage, AIMessage

conversation_history = []

def add_message(role, content):
    if role == "human":
        conversation_history.append(HumanMessage(content=content))
    else:
        conversation_history.append(AIMessage(content=content))

def get_history():
    return conversation_history

def clear_history():
    conversation_history.clear()