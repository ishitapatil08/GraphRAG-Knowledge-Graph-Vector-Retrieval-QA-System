from langgraph.graph import StateGraph, START, END
from app.graph.state import AgentState
from app.graph.nodes import financial_agent, legal_agent, technical_agent, web_search_agent
from app.graph.supervisor import supervisor_agent
from app.graph.aggregator import aggregator_agent

def create_workflow():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("Supervisor", supervisor_agent)
    workflow.add_node("Financial", financial_agent)
    workflow.add_node("Legal", legal_agent)
    workflow.add_node("Technical", technical_agent)
    workflow.add_node("WebSearch", web_search_agent)
    workflow.add_node("Aggregator", aggregator_agent)
    
    # Add edges
    workflow.add_edge(START, "Supervisor")
    
    workflow.add_conditional_edges(
        "Supervisor",
        lambda x: x["next_node"],
        {
            "Financial": "Financial",
            "Legal": "Legal",
            "Technical": "Technical",
            "WebSearch": "WebSearch",
            "Aggregator": "Aggregator"
        }
    )
    
    for node in ["Financial", "Legal", "Technical", "WebSearch"]:
        workflow.add_edge(node, "Supervisor")
        
    workflow.add_edge("Aggregator", END)
    
    return workflow.compile()

graph = create_workflow()
