import os
import gradio as gr
from typing import List, Tuple
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_demo(week: int = 1, mode_str: str = "part1", use_solution: bool = False):
    """Create and return a Gradio demo for AGnetic RAG.
    """

    from perplexia_ai.DeepResearch.Research.Agents import (
        AgentMode,
        create_chat_implementation as create_chat,
    )   
             
    chat_interface = create_chat(AgentMode.DEEP_RESEARCH)
    
    # Initialize the chat implementation 
    chat_interface.initialize()

    title = "Perplexia AI - Deep Research"
    description = "Your multi-agent research system that creates comprehensive research reports."
    
    examples = [
        ["Research the current state and future prospects of quantum computing"],
        ["Create a comprehensive report on climate change adaptation strategies"],
        ["Analyze the impact of artificial intelligence on healthcare delivery"],
        ["Frameworks for building LLM agents: an enterprise guide"]
    ]

    def respond(message: str, history: List[Tuple[str, str]]) -> str:
        return chat_interface.process_message(message, history)

    return gr.ChatInterface(
        fn=respond,
        title=title,
        description=description,
        examples=examples,
        type="messages",
        theme=gr.themes.Soft(),
    )

    if __name__ == "__main__":
        demo = create_demo()
        demo.launch()