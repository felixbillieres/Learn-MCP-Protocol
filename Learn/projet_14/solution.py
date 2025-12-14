from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Create the MCP server
mcp_server = FastMCP(
    "ElicitationServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Create the create_profile tool
@mcp_server.tool()
async def create_profile(ctx: Context) -> dict[str, Any]:
    """
    Creates a user profile by requesting information via elicitation.
    
    Returns:
        Dict with created profile information
    """
    # TODO: Use ctx.elicitation.create() to request:
    # - name (string, required)
    # - age (integer, required)
    # - email (string, optional)
    # 
    # Example schema for a field:
    # {
    #     "type": "object",
    #     "properties": {
    #         "name": {"type": "string", "title": "Name", "description": "Your name"}
    #     },
    #     "required": ["name"]
    # }
    
    # TODO: Return collected information
    pass

# TODO: Create the configure_preferences tool
@mcp_server.tool()
async def configure_preferences(ctx: Context) -> dict[str, Any]:
    """
    Configures user preferences via elicitation.
    
    Returns:
        Dict with configured preferences
    """
    # TODO: Use ctx.elicitation.create() to request:
    # - theme (enum: "dark", "light", "auto")
    # - notifications (boolean)
    
    # TODO: Return preferences
    pass


def main():
    print("My MCP server with elicitation is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
