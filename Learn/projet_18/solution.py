from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Create the MCP server
mcp_server = FastMCP(
    "AdvancedSamplingServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Create the creative_ideation tool
@mcp_server.tool()
async def creative_ideation(
    topic: str,
    ctx: Context
) -> str:
    """
    Generates creative ideas on a topic.
    
    Args:
        topic: The topic for ideation
        ctx: MCP Context
        
    Returns:
        Generated ideas
    """
    # TODO: Use ctx.sampling.create_message() with:
    # - temperature: 0.9
    # - model_preferences: {"intelligencePriority": 0.8}
    # - messages: request creative ideas
    
    pass

# TODO: Create the conversation tool
@mcp_server.tool()
async def conversation(
    message_history: list[dict[str, Any]],
    new_message: str,
    ctx: Context
) -> str:
    """
    Continues a conversation with history.
    
    Args:
        message_history: List of previous messages
        new_message: The new message
        ctx: MCP Context
        
    Returns:
        The LLM response
    """
    # TODO: Build the complete message list
    # TODO: Use max_tokens: 500
    # TODO: Call sampling
    
    pass

# TODO: Create the quick_response tool
@mcp_server.tool()
async def quick_response(
    question: str,
    ctx: Context
) -> str:
    """
    Generates a quick response (optimized for speed).
    
    Args:
        question: The question
        ctx: MCP Context
        
    Returns:
        A short and quick response
    """
    # TODO: Use sampling with:
    # - high speedPriority
    # - max_tokens: 100
    
    pass


def main():
    print("My MCP server with advanced sampling is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
