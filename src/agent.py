from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from src.tools import get_tools
import os

load_dotenv()

SYSTEM_PROMPT = """You are a helpful customer support agent.

You have access to a web search tool. Use it ONLY when:
- User asks about current events, news, facts, or data
- You are not confident about the answer

Do NOT search for:
- Simple greetings or casual conversation
- Questions you can answer from your own knowledge

After giving an answer, always reflect:
- Is my answer complete and accurate?
- Did I miss any important information?
- If yes, search again and improve the answer.

Always be concise and helpful."""

def create_agent():
    model = ChatAnthropic(
        model="claude-haiku-4-5-20251001",
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    tools = get_tools()
    agent = create_react_agent(
        model=model,
        tools=tools,
        prompt=SYSTEM_PROMPT
    )
    return agent