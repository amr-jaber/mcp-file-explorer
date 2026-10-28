# Local File Explorer MCP Server & Client

A secure, lightweight **Model Context Protocol (MCP)** implementation built with Python. It enables AI clients to browse local directories and read text-file contents through the standard input/output (`stdio`) transport.

## ✨ Features

- **Directory listing (`list_directory`)** — Browse directory contents and distinguish files from folders.
- **File reading (`read_file_content`)** — Read text files and source code through an MCP tool.
- **Two testing options** — Inspect tools interactively with MCP Inspector or test them programmatically with `mcp_client.py`.
- **Claude Desktop integration** — Connect the server to Claude Desktop for natural-language interaction with local files.

> **Security note:** The server can expose local file contents to the connected AI client. Only run it with directories and files you trust, and review the server implementation before use. Consider restricting accessible paths and handling errors for missing files, directories, and unsupported encodings.

## 🧰 Tech Stack

- **Python 3.13**
- **Model Context Protocol Python SDK** (`mcp`, version 1.x; install with `mcp<2`)
- **AnyIO / asyncio** for asynchronous communication

## 📁 Project Structure

```text
mcp-file-explorer/
├── mcp_server.py   # MCP server and tools
├── mcp_client.py   # Programmatic stdio client
└── README.md       # Project documentation
```

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/amr-jaber/mcp-file-explorer.git
cd mcp-file-explorer
```

### 2. (Recommended) Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
py -3.13 -m venv .venv
.venv\\Scripts\\Activate.ps1
```

**macOS / Linux:**

```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

### 3. Install the MCP SDK

```bash
python -m pip install "mcp<2"
```

Confirm Python is available:

```bash
python --version
```

## 🚀 Usage & Testing

Run commands from the project directory unless noted otherwise.

### Option 1: Test with MCP Inspector

MCP Inspector provides an interactive interface for connecting to and testing MCP servers.

```bash
npx @modelcontextprotocol/inspector python mcp_server.py
```

Open the local URL printed in the terminal. Navigate to **Tools** and try `list_directory` or `read_file_content`.

> This option requires Node.js and `npx` to be installed.

### Option 2: Run the programmatic client

```bash
python mcp_client.py
```

This runs the client script to test stdio communication and tool invocation. Make sure `mcp_server.py` and `mcp_client.py` match the SDK version installed in your environment.

## 🤖 Claude Desktop Integration

You can register the server in Claude Desktop by editing `claude_desktop_config.json`.

### 1. Locate the configuration file

On Windows, it is commonly located at:

```text
%APPDATA%\\Claude\\claude_desktop_config.json
```

The exact location may vary by operating system or installation.

### 2. Add the server configuration

Merge the following entry into the existing `mcpServers` object. Replace the example path with the **absolute path** to your `mcp_server.py` file.

```json
{
  "mcpServers": {
    "local-file-explorer": {
      "command": "python",
      "args": [
        "C:\\\\ABSOLUTE\\\\PATH\\\\TO\\\\mcp-file-explorer\\\\mcp_server.py"
      ]
    }
  }
}
```

**Important:** If the configuration already contains other MCP servers, preserve them and add only the `local-file-explorer` entry. JSON does not allow comments or trailing commas.

If Claude Desktop cannot find `python`, use the full path to the Python executable in the `command` field. If the project depends on a virtual environment, point `command` to that environment's Python executable.

### 3. Restart and verify

1. Save the configuration file.
2. Fully quit and reopen Claude Desktop.
3. Check that the `local-file-explorer` server and its tools are available.
4. Try asking Claude to list a directory or read a text file.

## 🛡 Security & Limitations

- Grant access only to files you are comfortable making available to the connected AI client.
- Do not expose secrets, credentials, private keys, or sensitive documents.
- For stronger isolation, update the server to allow access only within a configured base directory and reject path traversal outside it.
- The described tools are intended for text-file access; binary files may not be readable as text.
- This README documents the expected setup and commands; exact behavior depends on the implementation in `mcp_server.py` and `mcp_client.py`.

## 🧯 Troubleshooting

- **`python` is not recognized:** Install Python or set `command` to the full path of the Python executable.
- **Module not found (`mcp`):** Activate the environment used by the server and run `python -m pip install "mcp<2"`.
- **Server does not appear in Claude Desktop:** Validate the JSON, verify the absolute script path, then restart Claude Desktop.
- **Inspector does not launch:** Confirm Node.js and `npx` are installed and available on your `PATH`.

## 👤 Author

- GitHub: [@amr-jaber](https://github.com/amr-jaber)
