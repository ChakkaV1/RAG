import gradio as gr
from typing import List, Tuple
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def create_demo():
    """Create and return a Gradio demo for Corrective RAG (Week 2)."""

    from perplexia_ai.RAGSearch.Search.factory import (
        RagSearchMode,
        create_chat_implementation as create_chat,
    )

    # Hardcoded single mode
    chat_interface = create_chat(RagSearchMode.CORRECTIVE_RAG)
    chat_interface.initialize()

    title = "Perplexia AI - Corrective RAG (Student)"
    description = "Your intelligent AI assistant that combines web search and document retrieval."

    examples = [
        ["What new customer experience improvements did OPM implement for retirement services in FY 2022?"],
        ["How did OPM's approach to improving the federal hiring process evolve from FY 2019 through FY 2022?"],
        ["What were some key performance metrics for OPM in 2020? Compare them with 2019?"],
        ["What strategic goals did OPM outline in the 2022 report?"],
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
