"""Factory for creating RAG search chat implementations."""

from enum import Enum

from perplexia_ai.core.chat_interface import ChatInterface
from perplexia_ai.RAGSearch.Search.corrective_rag import CorrectiveRAGChat

class RagSearchMode(Enum):
    """Modes for RAG Search demos."""
    CORRECTIVE_RAG = "corrective_rag"

def create_chat_implementation(mode: RagSearchMode) -> ChatInterface:
    """Create and return the appropriate chat implementation."""
    if mode == RagSearchMode.CORRECTIVE_RAG:
        return CorrectiveRAGChat()
    raise ValueError(f"Unknown mode: {mode}")

