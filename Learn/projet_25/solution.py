# FINAL PROJECT - Complete Project Manager MCP
# 
# TODO: Create a professional MCP server with ALL features
# - Tools for CRUD projects/tasks
# - Resources to expose data
# - Prompts for workflows
# - Elicitation for interactions
# - Authorization for security
# - Well-structured code

from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from typing import Any, Optional, List, Dict

# TODO: Necessary imports
# TODO: Create the server with all capabilities
mcp_server = FastMCP(
    "ProjectManager",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Add all necessary capabilities
)

# TODO: Pydantic models for Project and Task
# TODO: Storage (dicts or similar)
# TODO: CRUD Tools
# TODO: Resources
# TODO: Prompts
# TODO: Authorization
# TODO: Main function

def main():
    print("Project Manager MCP is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    main()
