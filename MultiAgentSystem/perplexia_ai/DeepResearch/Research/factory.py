"""Factory for creating Multi-Agents implementations.
"""

from enum import Enum
from perplexia_ai.core.chat_interface import ChatInterface
from perplexia_ai.DeepResearch.Research.Agents import DeepResearchChat

class AgentMode(Enum):
  DEEP_RESEARCH = "deep_research"


def create_chat_implementation(mode: AgentMode) -> ChatInterface:
    """Create and return the appropriate chat implementation.
    """
    if mode == AgentMode.DEEP_RESEARCH:
        return DeepResearchChat()
