from mcp.server.fastmcp import FastMCP, Context
from typing import List
import os

mcp_server = FastMCP("RootsServer", host="127.0.0.1", port=8000)

def get_authorized_roots(ctx: Context) -> List[str]:
    """Retrieves authorized roots."""
    # TODO: Use ctx.roots.list() to get roots
    # Note: FastMCP may have limitations, simulate if necessary
    pass

def is_path_authorized(path: str, roots: List[str]) -> bool:
    """Checks that a path is in an authorized root."""
    # TODO: Check that the path is under one of the roots
    pass

@mcp_server.tool()
async def list_files(ctx: Context) -> List[str]:
    """Lists files in authorized roots."""
    # TODO: Get roots, list files
    pass

@mcp_server.tool()
async def read_file(path: str, ctx: Context) -> str:
    """Reads a file if it's authorized."""
    # TODO: Check that the path is authorized, read the file
    pass

def main():
    print("Server with roots is starting!")
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    main()
