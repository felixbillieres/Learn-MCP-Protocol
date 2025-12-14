from mcp.server.fastmcp import FastMCP
from typing import Any, Optional

# TODO: Create the server with support for prompts AND resources
mcp_server = FastMCP(
    "AdvancedPromptsServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Add capabilities={"prompts": {}, "resources": {}}
)

# Resources
RESOURCES = {
    "doc://examples/code_sample": {
        "content": "def example_function():\n    return 'Hello, World!'"
    },
    "doc://guidelines/best_practices": {
        "content": "1. Use meaningful variable names\n2. Write docstrings\n3. Handle errors properly"
    }
}

# TODO: Implement list_resources and read_resource
@mcp_server.list_resources()
async def list_resources() -> list[dict[str, Any]]:
    """Lists available resources."""
    pass

@mcp_server.read_resource()
async def read_resource(uri: str) -> dict[str, Any]:
    """Reads a resource."""
    pass

# TODO: Create list_prompts with advanced prompts
@mcp_server.list_prompts()
async def list_prompts() -> list[dict[str, Any]]:
    """Lists advanced prompts."""
    pass

# TODO: Create get_prompt with multiple messages and resources
@mcp_server.get_prompt()
async def get_prompt(
    name: str,
    arguments: Optional[dict[str, Any]] = None
) -> dict[str, Any]:
    """
    Retrieves an advanced prompt.
    
    For tutorial: returns multiple messages
    For code_analysis: includes a reference to a resource
    """
    if arguments is None:
        arguments = {}
    
    # TODO: Implement tutorial with multiple messages
    # TODO: Implement code_analysis with resource reference
    pass


def main():
    print("My MCP server with advanced prompts is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
