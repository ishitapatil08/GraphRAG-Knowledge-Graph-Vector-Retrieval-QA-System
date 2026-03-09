from app.graph.state import AgentState

def supervisor_agent(state: AgentState):
    """
    Supervisor that routes based on keywords in the query.
    In a real app, this would use an LLM with tool calling to select the next node dynamically.
    For local prototyping without an API key, we use keyword heuristic routing.
    """
    query = state["messages"][0].content.lower()
    last_message = state["messages"][-1]
    
    # If the last message is from a worker, we route to the aggregator
    if hasattr(last_message, "name") and last_message.name in ["Financial", "Legal", "Technical", "WebSearch"]:
        return {"next_node": "Aggregator"}
    
    # Simple semantic routing
    if any(kw in query for kw in ["finance", "revenue", "money", "cost", "q3"]):
        return {"next_node": "Financial"}
    elif any(kw in query for kw in ["law", "legal", "contract", "compliance", "policy"]):
        return {"next_node": "Legal"}
    elif any(kw in query for kw in ["api", "technical", "auth", "backend", "token"]):
        return {"next_node": "Technical"}
    else:
        return {"next_node": "WebSearch"}
