from typing import Annotated, TypedDict, Sequence, Optional
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    """The complete state of the LangGraph execution."""
    # The messages list will append new messages using operator.add
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # The next node to route to, determined by the supervisor
    next_node: Optional[str]
