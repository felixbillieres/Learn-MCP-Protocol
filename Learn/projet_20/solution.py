from mcp.server.fastmcp import FastMCP, Context
from typing import Optional
import time

# TODO: Create the MCP server
mcp_server = FastMCP(
    "AuthServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# Simulated valid tokens (in production, this would be in a database)
VALID_TOKENS = {
    "Bearer token123": {
        "user_id": "user1",
        "username": "alice",
        "email": "alice@example.com",
        "expires_at": time.time() + 3600  # Expires in 1h
    },
    "Bearer token456": {
        "user_id": "user2",
        "username": "bob",
        "email": "bob@example.com",
        "expires_at": time.time() + 3600
    }
}

# TODO: Create the validate_token function
def validate_token(token: str) -> Optional[dict]:
    """
    Validates a token and returns user info.
    
    Args:
        token: The token to validate (format "Bearer ...")
        
    Returns:
        Dict with user info if valid, None otherwise
    """
    # TODO: Check that token starts with "Bearer "
    # TODO: Check that token exists in VALID_TOKENS
    # TODO: Check that token is not expired
    # TODO: Return user info if valid
    
    pass

# TODO: Create the user_info tool
@mcp_server.tool()
async def user_info(
    token: str,
    ctx: Context
) -> dict:
    """
    Retrieves information about the authenticated user.
    
    Args:
        token: Authorization token
        ctx: MCP Context
        
    Returns:
        Dict with user info
        
    Raises:
        ValueError: If the token is invalid
    """
    # TODO: Validate token
    # TODO: If invalid, raise ValueError
    # TODO: Return user info
    
    pass

# TODO: Create the sensitive_data tool
@mcp_server.tool()
async def sensitive_data(
    token: str,
    ctx: Context
) -> dict:
    """
    Accesses sensitive data (requires authentication).
    
    Args:
        token: Authorization token
        ctx: MCP Context
        
    Returns:
        Sensitive data
        
    Raises:
        ValueError: If the token is invalid
    """
    # TODO: Validate token
    # TODO: Return simulated sensitive data
    
    pass


def main():
    print("My MCP authorization server is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
