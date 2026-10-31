from mcp.server.fastmcp import FastMCP
import os


mcp = FastMCP("Local File Explorer")

@mcp.tool()
def list_directory(dir_path: str) -> str:
   
    try:
        if not os.path.exists(dir_path):
            return f"Error: Path does not exist: {dir_path}"
        
        items = os.listdir(dir_path)
        formatted_items = []
        for item in items:
            full_path = os.path.join(dir_path, item)
            item_type = "📁 [Directory]" if os.path.isdir(full_path) else "📄 [File]"
            formatted_items.append(f"{item_type} {item}")
            
        return f"Contents of {dir_path}:\n" + "\n".join(formatted_items)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def read_file_content(file_path: str) -> str:
   
    try:
        if not os.path.exists(file_path):
            return f"Error: File does not exist: {file_path}"
            
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            if len(content) > 5000:
                content = content[:5000] + "\n... [Truncated due to length] ..."
        return content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
