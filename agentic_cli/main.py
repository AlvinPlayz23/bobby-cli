import argparse
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from .core.agent import run_agent

def main():
    parser = argparse.ArgumentParser(description="Agentic Coding CLI Tool")
    parser.add_argument(
        "prompt",
        type=str,
        nargs="?",
        help="The coding task for the AI to perform.",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Run in interactive mode.",
    )
    args = parser.parse_args()

    console = Console()
    console.print(Panel("[bold magenta]Welcome to the Agentic Coding CLI Tool![/bold magenta]", border_style="green"))

    if args.interactive:
        run_agent(interactive=True)
    elif args.prompt:
        run_agent(prompt=args.prompt)
    else:
        prompt = Prompt.ask("[bold cyan]What can I code for you today?[/bold cyan]")
        run_agent(prompt=prompt)

if __name__ == "__main__":
    main()
