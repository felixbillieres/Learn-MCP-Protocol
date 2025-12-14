from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Create the MCP server with resource support
mcp_server = FastMCP(
    "ResourcesServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Add capabilities={"resources": {}}
)

# Resource data (in-memory storage)
RESOURCES = {
    "config://app/settings": {
        "name": "Application settings",
        "description": "Main application configuration",
        "mimeType": "application/json",
        "content": '{"theme": "dark", "language": "en", "notifications": true}'
    },
    "info://server/version": {
        "name": "Server version",
        "description": "MCP server version information",
        "mimeType": "text/plain",
        "content": "Version 1.0.0\nBuild: 2024-01-15"
    }
}

# TODO: Create the list_resources function
async def list_resources() -> list[dict[str, Any]]:
    """
    Lists all available resources.

    Returns:
        List of dictionaries with uri, name, description, mimeType
    """
    pass

# TODO: Register the function with FastMCP
# mcp_server.list_resources = list_resources

# TODO: Create the read_resource function
async def read_resource(uri: str, ctx: Context = None) -> dict[str, Any]:
    """
    Reads the content of a resource.

    Args:
        uri: The URI of the resource to read

    Returns:
        Dict with 'contents' containing a list of contents

    Raises:
        ValueError: If the URI doesn't exist
    """
    pass

# TODO: Register the function with FastMCP
# mcp_server.read_resource = read_resource

def main():
    print("My MCP server with resources is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
