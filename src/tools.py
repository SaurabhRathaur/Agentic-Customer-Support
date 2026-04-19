from langchain_tavily import TavilySearch

def get_tools():
    return [TavilySearch(max_results=3)]