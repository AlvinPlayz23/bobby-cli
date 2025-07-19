import os
import google.generativeai as genai
from rich.console import Console
from rich.prompt import Prompt

from .tools import (
    create_file,
    edit_file,
    rename_file,
    delete_file,
    create_folder,
    edit_folder,
    rename_folder,
    delete_folder,
    terminal_run,
    terminal_stop,
)

console = Console()

def run_agent(prompt: str = None, interactive: bool = False):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        api_key = Prompt.ask("[bold yellow]Please enter your Gemini API key[/bold yellow]")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        tools=[
            create_file,
            edit_file,
            rename_file,
            delete_file,
            create_folder,
            edit_folder,
            rename_folder,
            delete_folder,
            terminal_run,
            terminal_stop,
        ],
    )

    chat = model.start_chat(history=[])

    if interactive:
        console.print("[bold green]Starting interactive session...[/bold green]")
        while True:
            prompt = Prompt.ask("[bold cyan]You[/bold cyan]")
            if prompt.lower() in ["exit", "quit"]:
                break
            response = chat.send_message(prompt)
            for part in response.parts:
                if part.function_call:
                    tool_name = part.function_call.name
                    tool_args = {key: value for key, value in part.function_call.args.items()}
                    console.print(f"AI wants to use tool: {tool_name} with args: {tool_args}")

                    tool_map = {
                        "create_file": create_file,
                        "edit_file": edit_file,
                        "rename_file": rename_file,
                        "delete_file": delete_file,
                        "create_folder": create_folder,
                        "edit_folder": edit_folder,
                        "rename_folder": rename_folder,
                        "delete_folder": delete_folder,
                        "terminal_run": terminal_run,
                        "terminal_stop": terminal_stop,
                    }

                    if tool_name in tool_map:
                        tool_map[tool_name](**tool_args)
                    else:
                        console.print(f"[red]Unknown tool: {tool_name}[/red]")
    else:
        response = chat.send_message(prompt)
        for part in response.parts:
            if part.function_call:
                tool_name = part.function_call.name
                tool_args = {key: value for key, value in part.function_call.args.items()}

                console.print(f"AI wants to use tool: {tool_name} with args: {tool_args}")

                tool_map = {
                    "create_file": create_file,
                    "edit_file": edit_file,
                    "rename_file": rename_file,
                    "delete_file": delete_file,
                    "create_folder": create_folder,
                    "edit_folder": edit_folder,
                    "rename_folder": rename_folder,
                    "delete_folder": delete_folder,
                    "terminal_run": terminal_run,
                    "terminal_stop": terminal_stop,
                }

                if tool_name in tool_map:
                    tool_map[tool_name](**tool_args)
                else:
                    console.print(f"[red]Unknown tool: {tool_name}[/red]")
