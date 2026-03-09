from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

def get_retriever(domain: str):
    """
    Creates a dummy FAISS retriever for a specific domain.
    In a real app, this would load a persistent index from disk.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Mock data
    data = {
        "financial": [
            Document(page_content="Q3 Revenue was $1.2B, up 15% YoY.", metadata={"source": "Q3_Report"}),
            Document(page_content="The company acquired a new AI startup for $200M.", metadata={"source": "News"}),
        ],
        "legal": [
            Document(page_content="The new compliance law 24-B requires strict data localization.", metadata={"source": "Law_24B"}),
            Document(page_content="All vendor contracts must be renewed annually under section 4.", metadata={"source": "Policy"}),
        ],
        "technical": [
            Document(page_content="The backend API rate limit is 1000 requests per minute per IP.", metadata={"source": "API_Docs"}),
            Document(page_content="To authenticate, use a JWT Bearer token in the Authorization header.", metadata={"source": "Auth_Guide"})
        ]
    }
    
    docs = data.get(domain, [Document(page_content="No specific documents found.", metadata={"source": "None"})])
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 2})
