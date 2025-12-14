from mcp.server.fastmcp import FastMCP, Context
from typing import Any, Set

# TODO: Create the server with subscription support
mcp_server = FastMCP(
    "SubscriptionsServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Add capabilities={"resources": {"subscribe": True}}
)

# Status resource state
status_content = {"status": "running", "uptime": 0}

# TODO: Handle subscriptions (URI -> set of clients)
# subscriptions: dict[str, Set] = {}

# TODO: Implement list_resources
@mcp_server.list_resources()
async def list_resources() -> list[dict[str, Any]]:
    """
    Lists available resources.
    """
    pass

# TODO: Implement read_resource
@mcp_server.read_resource()
async def read_resource(uri: str) -> dict[str, Any]:
    """
    Reads a resource.
    """
    if uri == "status://app/current":
        return {
            "contents": [{
                "uri": uri,
                "mimeType": "application/json",
                "text": str(status_content)
            }]
        }
    raise ValueError(f"Resource not found: {uri}")

# TODO: Create a tool to modify status
@mcp_server.tool()
async def update_status(
    status: str,
    uptime: int,
    ctx: Context
) -> dict[str, Any]:
    """
    Updates the application status and notifies subscribers.

    Args:
        status: New status
        uptime: New uptime
        ctx: MCP Context

    Returns:
        Update confirmation
    """
    global status_content
    # TODO: Update status_content
    # TODO: Notify subscribers with ctx or server
    # Note: FastMCP may have limitations, the concept is what matters
    pass


def main():
    print("My MCP server with subscriptions is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
