# TODO: Import FastMCP from mcp.server.fastmcp
from mcp.server.fastmcp import FastMCP

# TODO: Create the FastMCP server (use project 01 as base)
mcp_server = FastMCP(
    "MyFirstServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Create the say_hello tool
# - Takes a parameter name (type str)
# - Returns a string: f"Hello, {name}! How are you?"
# - Add a descriptive docstring
# - Use the decorator @mcp_server.tool()
# - The function must be async
@mcp_server.tool()
async def say_hello(name: str) -> str:
    """Says hello to a person."""
    pass

# TODO: Create the calculate_sum tool
# - Takes two parameters a and b (type int)
# - Returns an int: the sum of a and b
# - Add a descriptive docstring
# - Use the decorator @mcp_server.tool()
# - The function must be async
@mcp_server.tool()
async def calculate_sum(a: int, b: int) -> int:
    """Calculates the sum of two integers."""
    pass

def main():
    print("My first MCP server is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    main()
