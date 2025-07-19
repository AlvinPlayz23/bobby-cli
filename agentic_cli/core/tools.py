import os
import subprocess
from rich.console import Console

console = Console()

def create_file(path: str, content: str = ""):
    """Creates a new file at the specified path with optional content."""
    try:
        with open(path, "w") as f:
            f.write(content)
        console.print(f"[green]File created: {path}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error creating file: {e}[/red]")
        return False

def edit_file(path: str, content: str):
    """Edits an existing file by replacing its content."""
    try:
        with open(path, "w") as f:
            f.write(content)
        console.print(f"[green]File edited: {path}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error editing file: {e}[/red]")
        return False

def rename_file(old_path: str, new_path: str):
    """Renames a file."""
    try:
        os.rename(old_path, new_path)
        console.print(f"[green]File renamed from {old_path} to {new_path}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error renaming file: {e}[/red]")
        return False

def delete_file(path: str):
    """Deletes a file."""
    try:
        os.remove(path)
        console.print(f"[green]File deleted: {path}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error deleting file: {e}[/red]")
        return False

def create_folder(path: str):
    """Creates a new folder."""
    try:
        os.makedirs(path, exist_ok=True)
        console.print(f"[green]Folder created: {path}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error creating folder: {e}[/red]")
        return False

def edit_folder(path: str, new_path: str):
    """Renames a folder. This is an alias for rename_folder."""
    return rename_folder(path, new_path)

def rename_folder(old_path: str, new_path: str):
    """Renames a folder."""
    try:
        os.rename(old_path, new_path)
        console.print(f"[green]Folder renamed from {old_path} to {new_path}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error renaming folder: {e}[/red]")
        return False

def delete_folder(path: str):
    """Deletes a folder and all its contents."""
    try:
        subprocess.run(["rm", "-r", path], check=True)
        console.print(f"[green]Folder deleted: {path}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error deleting folder: {e}[/red]")
        return False

processes = {}

def terminal_run(command: str):
    """Runs a command in the terminal."""
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes[process.pid] = process
        console.print(f"[green]Started process {process.pid} with command: {command}[/green]")
        return process.pid
    except Exception as e:
        console.print(f"[red]Error running command: {e}[/red]")
        return None

def terminal_stop(pid: int):
    """Stops a running process."""
    if pid not in processes:
        console.print(f"[red]Process {pid} not found.[/red]")
        return False
    try:
        processes[pid].terminate()
        del processes[pid]
        console.print(f"[green]Process {pid} stopped.[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error stopping process {pid}: {e}[/red]")
        return False
