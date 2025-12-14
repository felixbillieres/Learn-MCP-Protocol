from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Create the MCP server
mcp_server = FastMCP(
    "AgenticServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Create simple tools that the LLM can use
@mcp_server.tool()
async def calculate(expression: str, ctx: Context) -> float:
    """
    Evaluates a simple mathematical expression.
    
    Args:
        expression: Expression to evaluate (e.g., "2 + 2")
        ctx: MCP Context
        
    Returns:
        The calculation result
    """
    # TODO: Evaluate the expression (use eval with caution or a secure library)
    # For this project, we can use eval() but in production use a secure library
    pass

@mcp_server.tool()
async def search_info(term: str, ctx: Context) -> str:
    """
    Searches for information on a term (simulated).
    
    Args:
        term: The term to search for
        ctx: MCP Context
        
    Returns:
        Information about the term
    """
    # TODO: Simulate a search (return hardcoded info)
    pass

@mcp_server.tool()
async def convert_unit(
    value: float,
    source_unit: str,
    target_unit: str,
    ctx: Context
) -> float:
    """
    Converts a value from one unit to another.
    
    Args:
        value: The value to convert
        source_unit: Source unit (e.g., "km", "m", "kg")
        target_unit: Target unit
        ctx: MCP Context
        
    Returns:
        The converted value
    """
    # TODO: Implement basic conversions (km->m, kg->g, etc.)
    pass

# Tool definitions for the LLM (MCP format)
TOOLS_FOR_LLM = [
    {
        "name": "calculate",
        "description": "Evaluates a simple mathematical expression",
        "inputSchema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematical expression to evaluate"
                }
            },
            "required": ["expression"]
        }
    },
    # TODO: Add definitions for search_info and convert_unit
]

# TODO: Create the agent_solver tool
@mcp_server.tool()
async def agent_solver(
    question: str,
    ctx: Context
) -> str:
    """
    Uses an LLM agent with tools to solve a complex question.
    
    Args:
        question: The question to solve
        ctx: MCP Context
        
    Returns:
        The agent's response
    """
    # TODO: Use ctx.sampling.create_message() with:
    # - messages: [{"role": "user", "content": {"type": "text", "text": question}}]
    # - tools: TOOLS_FOR_LLM
    # - max_tokens: 500
    
    # The LLM will be able to call tools automatically
    pass


def main():
    print("My MCP server with agentic workflows is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
