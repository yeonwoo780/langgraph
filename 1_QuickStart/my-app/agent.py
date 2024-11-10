from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

model = ChatOpenAI(model="gpt-4o-2024-08-06")

tool = TavilySearchResults(max_results=2)
tools = [tool]

graph = create_react_agent(model, tools)