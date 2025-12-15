# TODO: Import FastMCP from mcp.server.fastmcp
from mcp.server.fastmcp import FastMCP

# TODO: Create the FastMCP server
# - Server name: "MyFirstServer"
# - Host: "127.0.0.1"
# - Port: 8000
# - Options: stateless_http=True and json_response=True
mcp_server = FastMCP(
    "MyFirstServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

def main():
    # TODO: Display message: "My first MCP server is starting!"
    # TODO: Display the server URL: "URL: http://127.0.0.1:8000/mcp"
    # TODO: Start the server with mcp_server.run(transport="streamable-http")
    pass

if __name__ == "__main__":
    main()
