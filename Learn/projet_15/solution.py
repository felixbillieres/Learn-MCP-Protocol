from mcp.server.fastmcp import FastMCP, Context
from typing import Any
import re

# TODO: Create the MCP server
mcp_server = FastMCP(
    "ElicitationSchemasServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Create the register tool with detailed schema
@mcp_server.tool()
async def register(ctx: Context) -> dict[str, Any]:
    """
    Registers a new user with validation via elicitation.
    
    Returns:
        Dict with confirmation message
    """
    # TODO: Create the schema with:
    # - username: string, minLength 3, maxLength 20, alphanumeric pattern
    # - email: string, email format
    # - age: integer, minimum 13, maximum 120
    # - newsletter: boolean, default false
    
    schema = {
        "type": "object",
        "properties": {
            # TODO: Add properties with their constraints
        },
        "required": []  # TODO: Add required fields
    }
    
    # TODO: Use ctx.elicitation.create() with the schema
    # TODO: Validate received data (double validation for security)
    # TODO: Return a confirmation message
    pass

# TODO: Validation function
def validate_username(username: str) -> bool:
    """Validates username according to rules."""
    if len(username) < 3 or len(username) > 20:
        return False
    if not re.match(r"^[a-zA-Z0-9]+$", username):
        return False
    return True

def validate_email(email: str) -> bool:
    """Validates email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# TODO: Create the order_product tool with enum
@mcp_server.tool()
async def order_product(ctx: Context) -> dict[str, Any]:
    """
    Orders a product with selection via enum.
    
    Returns:
        Dict with order summary
    """
    # TODO: Create the schema with:
    # - product: enum ["basic", "premium", "enterprise"]
    # - quantity: integer, min 1, max 100
    # - express_delivery: boolean
    
    # TODO: Use ctx.elicitation.create()
    # TODO: Return a summary
    pass


def main():
    print("My MCP server with elicitation and schemas is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
