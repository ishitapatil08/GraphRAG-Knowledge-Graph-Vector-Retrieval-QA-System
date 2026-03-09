from langchain_core.messages import AIMessage
from app.graph.state import AgentState
from app.tools.retriever import get_retriever
from app.tools.web import get_web_search_tool

fin_retriever = get_retriever("financial")
leg_retriever = get_retriever("legal")
tech_retriever = get_retriever("technical")
web_search = get_web_search_tool()

def financial_agent(state: AgentState):
    query = state["messages"][0].content
    docs = fin_retriever.invoke(query)
    content = "\n".join([d.page_content for d in docs])
    msg = AIMessage(content=f"Financial Agent Findings:\n{content}", name="Financial")
    return {"messages": [msg]}

def legal_agent(state: AgentState):
    query = state["messages"][0].content
    docs = leg_retriever.invoke(query)
    content = "\n".join([d.page_content for d in docs])
    msg = AIMessage(content=f"Legal Agent Findings:\n{content}", name="Legal")
    return {"messages": [msg]}

def technical_agent(state: AgentState):
    query = state["messages"][0].content
    docs = tech_retriever.invoke(query)
    content = "\n".join([d.page_content for d in docs])
    msg = AIMessage(content=f"Technical Agent Findings:\n{content}", name="Technical")
    return {"messages": [msg]}

def web_search_agent(state: AgentState):
    query = state["messages"][0].content
    try:
        content = web_search.invoke(query)
    except Exception as e:
        content = f"Web search failed: {e}"
    msg = AIMessage(content=f"Web Search Agent Findings:\n{content}", name="WebSearch")
    return {"messages": [msg]}
