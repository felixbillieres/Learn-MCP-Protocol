from mcp.server.fastmcp import FastMCP
import sys

# Configuration
TRANSPORT = sys.argv[1] if len(sys.argv) > 1 else "http"

mcp_server = FastMCP("MonServeurTransport", host="127.0.0.1", port=8000)

@mcp_server.tool()
async def info_transport() -> dict:
    """Retourne des infos sur le transport utilisé."""
    return {"transport": TRANSPORT}

def main():
    print(f"Serveur avec transport {TRANSPORT} démarre !")
    if TRANSPORT == "http":
        mcp_server.run(transport="streamable-http")
    else:
        mcp_server.run(transport="stdio")

if __name__ == "__main__":
    main()

