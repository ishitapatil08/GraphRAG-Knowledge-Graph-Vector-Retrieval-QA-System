import traceback
from app.graph.workflow import graph
from langchain_core.messages import HumanMessage

def run_test():
    try:
        print("Testing Financial Query...")
        res = graph.invoke({"messages": [HumanMessage(content="What was Q3 revenue?")]})
        print("Result:", res["messages"][-1].content)
        
        print("\nTesting Technical Query...")
        res = graph.invoke({"messages": [HumanMessage(content="How do I authenticate with the API?")]})
        print("Result:", res["messages"][-1].content)
        
    except Exception as e:
        traceback.print_exc()

if __name__ == "__main__":
    run_test()
