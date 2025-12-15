# TODO: Import FastMCP and Context from mcp.server.fastmcp
from mcp.server.fastmcp import FastMCP, Context
# TODO: Import BaseModel and Field from pydantic
# from pydantic import BaseModel, Field
# TODO: Import List, Dict, Optional from typing
# from typing import List, Dict, Optional

mcp_server = FastMCP(
    "MyFirstServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Global list to store users
# users: List[User] = []

# TODO: Create a Pydantic User model
# - id: int (required)
# - name: str (required)
# - email: str | None (optional)
# - tags: List[str] (list of tags, can be empty)
# - score: float (required, default value 0.0)
# - Use Field() for descriptions
class User:
    pass

# TODO: Create a UserStatistics model
# - total: int (total number of users)
# - by_tag: Dict[str, int] (number of users per tag)
# - average_score: float (average score)
class UserStatistics:
    pass

# TODO: Create the add_user tool
# - Takes a parameter user (type User) and ctx: Context
# - Simulates adding a user (stores in an in-memory list)
# - Returns the user with their assigned ID
# - Logs with ctx.info()
@mcp_server.tool()
async def add_user(user: User, ctx: Context) -> User:
    """Adds a user to the list."""
    pass

# TODO: Create the list_users tool
# - Takes ctx: Context
# - Takes an optional parameter tag_filter: str | None
# - If tag_filter is provided, returns only users having this tag
# - Otherwise, returns all users
# - Returns List[User]
# - Logs with ctx.info()
@mcp_server.tool()
async def list_users(tag_filter: Optional[str], ctx: Context) -> List[User]:
    """Lists all users, optionally filtered by tag."""
    pass

# TODO: Create the get_statistics tool
# - Takes ctx: Context
# - Returns UserStatistics
# - Calculates total, stats by tag, and average score
# - Logs with ctx.info()
@mcp_server.tool()
async def get_statistics(ctx: Context) -> UserStatistics:
    """Gets statistics about users."""
    pass

def main():
    print("My first MCP server is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    main()
