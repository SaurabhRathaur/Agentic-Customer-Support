from src.agent import create_agent
from src.memory import add_message, get_history
from langchain_core.messages import HumanMessage

agent = create_agent()

def run_agent(user_input):
    add_message("human", user_input)
    
    result = agent.invoke({
        "messages": get_history()
    })
    
    response = result["messages"][-1].content
    add_message("ai", response)
    return response

if __name__ == "__main__":
    print("Customer Support Agent ready!")
    print("-" * 40)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = run_agent(user_input)
        print(f"Agent: {response}")
        print()