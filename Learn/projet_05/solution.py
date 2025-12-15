# TODO: Import FastMCP and Context from mcp.server.fastmcp
from mcp.server.fastmcp import FastMCP, Context
# TODO: Import math for isinf check
# import math

mcp_server = FastMCP(
    "MyFirstServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Create the calculate_division tool
# - Takes two parameters: dividend (float) and divisor (float)
# - Also takes ctx: Context
# - Divides the dividend by the divisor
# Validations to implement:
#   - If dividend is None or not provided → ctx.error() + raise ValueError("Dividend is required")
#   - If divisor is None or not provided → ctx.error() + raise ValueError("Divisor is required")
#   - If divisor == 0 → ctx.error() + raise ValueError("Division by zero is impossible")
#   - If the result is infinite → ctx.warning() (but still return the result)
# Logging:
#   - At the start: ctx.info(): "Calculating {dividend} / {divisor}"
#   - On success: ctx.info(): "Result: {result}"
#   - On error: log with ctx.error() before raising the exception
# Returns: a float (the division result)
@mcp_server.tool()
async def calculate_division(dividend: float, divisor: float, ctx: Context) -> float:
    """Calculates the division of two numbers with validation."""
    pass

def main():
    print("My first MCP server is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    main()
