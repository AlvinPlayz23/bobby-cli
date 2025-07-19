# Agentic Coding CLI Tool

This is a command-line tool that uses a large language model (LLM) to perform coding tasks. You can provide a prompt to the AI, and it will use a set of tools to accomplish the task.

## Features

- **Create, edit, rename, and delete files and folders.**
- **Run terminal commands.**
- **Powered by Google's Gemini Pro.**
- **Beautiful and user-friendly CLI.**

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/agentic-cli.git
   cd agentic-cli
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Gemini API key:**
   You can set your Gemini API key as an environment variable:
   ```bash
   export GEMINI_API_KEY="your-api-key"
   ```
   If you don't set the environment variable, the tool will prompt you for your API key when you run it.

## Usage

To run the tool, use the following command:

```bash
python -m agentic_cli.main "your coding prompt"
```

If you don't provide a prompt, the tool will ask you for one.

### Example

```bash
python -m agentic_cli.main "Create a new file called 'hello.py' with the content 'print(\"Hello, World!\")'"
```

## Tools

The AI has access to the following tools:

- `create_file(path: str, content: str = "")`: Creates a new file.
- `edit_file(path: str, content: str)`: Edits an existing file.
- `rename_file(old_path: str, new_path: str)`: Renames a file.
- `delete_file(path: str)`: Deletes a file.
- `create_folder(path: str)`: Creates a new folder.
- `edit_folder(path: str, new_path: str)`: Renames a folder.
- `rename_folder(old_path: str, new_path: str)`: Renames a folder.
- `delete_folder(path: str)`: Deletes a folder.
- `terminal_run(command: str)`: Runs a command in the terminal.
- `terminal_stop(pid: int)`: Stops a running process.
