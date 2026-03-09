from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

# Add the parent directory (project root) to the Python path
# This allows running `python app/main.py` directly from the IDE play button
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_core.messages import HumanMessage
from app.graph.workflow import graph
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

app = FastAPI(title="Multi-Agent RAG Research Assistant")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

@app.post("/query", response_model=QueryResponse)
async def process_query(req: QueryRequest):
    try:
        initial_state = {"messages": [HumanMessage(content=req.query)]}
        result = graph.invoke(initial_state)
        final_message = result["messages"][-1]
        
        return QueryResponse(answer=final_message.content, sources=[])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
