# FINAL PROJECT - Task Manager MCP
# 
# TODO: Create a complete MCP server to manage a task list
# Use ALL concepts learned in previous projects!

# TODO: Necessary imports
# - FastMCP, Context from mcp.server.fastmcp
# - BaseModel, Field from pydantic
# - List, Dict, Optional from typing
# - datetime from datetime

# TODO: Create the MCP server
# mcp_server = FastMCP(...)

# TODO: Global list to store tasks
# tasks = []

# TODO: Task model
class Task:
    pass

# TODO: TaskStatistics model
class TaskStatistics:
    pass

# TODO: Utility function to find a task by ID
# def find_task_by_id(task_id: int) -> Task | None:
#     ...

# TODO: create_task tool
@mcp_server.tool()
async def create_task(...):
    pass

# TODO: list_tasks tool
@mcp_server.tool()
async def list_tasks(...):
    pass

# TODO: get_task tool
@mcp_server.tool()
async def get_task(...):
    pass

# TODO: update_task tool
@mcp_server.tool()
async def update_task(...):
    pass

# TODO: mark_completed tool
@mcp_server.tool()
async def mark_completed(...):
    pass

# TODO: delete_task tool
@mcp_server.tool()
async def delete_task(...):
    pass

# TODO: get_statistics tool
@mcp_server.tool()
async def get_statistics(...):
    pass


def main():
    print("My task management MCP server is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
