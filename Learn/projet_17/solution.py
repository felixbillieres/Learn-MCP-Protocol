from mcp.server.fastmcp import FastMCP, Context

# TODO: Create the MCP server
mcp_server = FastMCP(
    "SamplingServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Create the ask_question tool
@mcp_server.tool()
async def ask_question(
    question: str,
    ctx: Context
) -> str:
    """
    Asks a question to the LLM via sampling.
    
    Args:
        question: The question to ask
        ctx: MCP Context
        
    Returns:
        The LLM response
    """
    # TODO: Use ctx.sampling.create_message() with:
    # - messages: [{"role": "user", "content": {"type": "text", "text": question}}]
    # - max_tokens: 200 (optional)
    # 
    # The response has .content.text which contains the text
    
    # TODO: Return the response
    pass

# TODO: Create the generate_summary tool
@mcp_server.tool()
async def generate_summary(
    text: str,
    ctx: Context
) -> str:
    """
    Generates a summary of a text via the LLM.
    
    Args:
        text: The text to summarize
        ctx: MCP Context
        
    Returns:
        The generated summary
    """
    # TODO: Use ctx.sampling.create_message() with:
    # - messages: [{"role": "user", "content": {"type": "text", "text": f"Summarize this text: {text}"}}]
    # - system_prompt: "You are an assistant that creates concise summaries"
    # - max_tokens: 150
    
    # TODO: Return the summary
    pass


def main():
    print("My MCP server with sampling is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
