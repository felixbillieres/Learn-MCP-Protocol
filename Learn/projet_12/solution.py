from mcp.server.fastmcp import FastMCP
from typing import Any, Optional

# TODO: Create the MCP server with prompt support
mcp_server = FastMCP(
    "PromptsArgsServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Add capabilities={"prompts": {}}
)

# TODO: Define prompts with their arguments
# Each prompt must have: name, title, description, arguments (list), and a template
PROMPTS = {
    # TODO: Add code_review with arguments: language (required), code (required)
    # TODO: Add summary with arguments: topic (required), length (optional, default "short")
}

# TODO: Create the list_prompts function with arguments
@mcp_server.list_prompts()
async def list_prompts() -> list[dict[str, Any]]:
    """
    Lists all available prompts with their arguments.
    
    Returns:
        List of prompts with name, title, description, arguments
    """
    pass

# TODO: Create the get_prompt function that accepts arguments
@mcp_server.get_prompt()
async def get_prompt(
    name: str,
    arguments: Optional[dict[str, Any]] = None
) -> dict[str, Any]:
    """
    Retrieves a prompt by its name with optional arguments.
    
    Args:
        name: The prompt name
        arguments: Dict with argument values (optional)
        
    Returns:
        Dict with 'messages' containing formatted messages
        
    Raises:
        ValueError: If the prompt doesn't exist or if required arguments are missing
    """
    if arguments is None:
        arguments = {}
    
    # TODO: Check that the prompt exists
    # TODO: Validate required arguments
    # TODO: Replace placeholders in template with arguments
    # TODO: Return formatted messages
    pass


def main():
    print("My MCP server with prompts and arguments is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
