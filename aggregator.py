from langchain_core.messages import AIMessage
from app.graph.state import AgentState

def aggregator_agent(state: AgentState):
    """
    Aggregates all the worker responses and creates a final summary.
    """
    query = state["messages"][0].content
    worker_messages = [m.content for m in state["messages"] if getattr(m, "name", "") in ["Financial", "Legal", "Technical", "WebSearch"]]
    
    if not worker_messages:
        final_answer = "No domain agents were able to find relevant information."
    else:
        combined = "\n\n".join(worker_messages)
        final_answer = f"Based on the query '{query}', here are the aggregated insights:\n\n{combined}\n\n(Aggregated by the Multi-Agent System)"
        
    return {"messages": [AIMessage(content=final_answer, name="Aggregator")], "next_node": "FINISH"}
