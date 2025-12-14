from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Create the MCP server
mcp_server = FastMCP(
    "ElicitationURLServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# Configuration (simulated)
AUTH_URL = "https://auth.example.com/login"
API_KEY_URL = "https://auth.example.com/api-keys"

# TODO: Create the authenticate tool with URL mode
@mcp_server.tool()
async def authenticate(ctx: Context) -> dict[str, Any]:
    """
    Authenticates the user via URL mode for security.
    
    Returns:
        Dict with confirmation message
    """
    # TODO: Use ctx.elicitation.create() with mode="url"
    # Format: {
    #     "mode": "url",
    #     "message": "Please authenticate via the following URL",
    #     "url": "https://..."
    # }
    
    # TODO: After authentication (simulated), return a message
    pass

# TODO: Create the configure_api_key tool with URL mode
@mcp_server.tool()
async def configure_api_key(ctx: Context) -> dict[str, Any]:
    """
    Configures an API key via URL mode (sensitive data).
    
    Returns:
        Dict with confirmation
    """
    # TODO: Use URL mode to redirect to configuration page
    # TODO: Return a confirmation
    pass


def main():
    print("My MCP server with URL mode elicitation is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
