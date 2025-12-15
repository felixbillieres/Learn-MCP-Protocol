# TODO: Import FastMCP and Context from mcp.server.fastmcp
from mcp.server.fastmcp import FastMCP, Context
# TODO: Import time for sleep simulation
# import time

mcp_server = FastMCP(
    "MyFirstServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Create the process_file tool
# - Takes a parameter filename (str) and ctx: Context
# - Simulates file processing with several steps
# - Uses Context to log each step
# Processing steps:
#   - Step 1: ctx.info(): "Starting to process file {filename}"
#   - Step 2: Check if the file exists (simulate with filename.endswith(".txt"))
#     - If yes: ctx.info(): "File found"
#     - If no: ctx.warning(): "Warning: the file does not appear to be a .txt file"
#   - Step 3: ctx.info(): "Reading content..."
#   - Step 4: Simulate an error if filename == "error.txt"
#     - If error: ctx.error(): "Error reading the file" then raise ValueError(...)
#   - Step 5: ctx.info(): "Processing completed successfully"
#   - Returns: a dict with {"file": filename, "status": "processed", "lines": 42}
# Important: Use await for all Context methods, ctx parameter must be last
@mcp_server.tool()
async def process_file(filename: str, ctx: Context) -> dict:
    """Processes a file and logs each step."""
    pass

def main():
    print("My first MCP server is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    main()
