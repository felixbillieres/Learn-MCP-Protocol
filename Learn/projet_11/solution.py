from mcp.server.fastmcp import FastMCP
from typing import Any

# TODO: Create the MCP server with prompt support
mcp_server = FastMCP(
    "PromptsServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Add capabilities={"prompts": {}}
)

# Prompt definitions
PROMPTS = {
    "greeting": {
        "title": "Greeting",
        "description": "A friendly greeting message",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "Hello! How can I help you today?"
                }
            }
        ]
    },
    "help": {
        "title": "Help",
        "description": "Get help about the system",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "I need help. Can you give me information about available features?"
                }
            }
        ]
    }
}

# TODO: Create the list_prompts function
@mcp_server.list_prompts()
async def list_prompts() -> list[dict[str, Any]]:
    """
    Lists all available prompts.
    
    Returns:
        List of prompts with name, title, description
    """
    pass

# TODO: Create the get_prompt function
@mcp_server.get_prompt()
async def get_prompt(name: str) -> dict[str, Any]:
    """
    Retrieves a prompt by its name.
    
    Args:
        name: The prompt name
        
    Returns:
        Dict with 'messages' containing formatted messages
        
    Raises:
        ValueError: If the prompt doesn't exist
    """
    pass


def main():
    print("My MCP server with prompts is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
