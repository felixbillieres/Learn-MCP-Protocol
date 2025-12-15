# TODO: Import FastMCP from mcp.server.fastmcp
from mcp.server.fastmcp import FastMCP
# TODO: Import BaseModel and Field from pydantic
# from pydantic import BaseModel, Field
# TODO: Import datetime for date generation
# from datetime import datetime
# TODO: Import random for ID generation
# import random

mcp_server = FastMCP(
    "MyFirstServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Create a Pydantic Message model
# - Inherits from BaseModel
# - Fields:
#   - sender: str (required, description "Sender's name")
#   - recipient: str (required, description "Recipient's name")
#   - content: str (required, description "Message content")
#   - priority: str (optional, default "normal", description "Message priority")
# - Use Field() for descriptions
class Message:
    pass

# TODO: Create a Pydantic MessageResponse model
# - message_id: int (description "Unique message ID")
# - sender: str
# - recipient: str
# - content: str
# - priority: str
# - send_date: str (description "Message send date")
class MessageResponse:
    pass

# TODO: Create the send_message tool
# - Takes a parameter message of type Message
# - Returns a MessageResponse
# - Generates a random message_id (or use a counter)
# - Creates the send date (simple string format: "2024-01-15 10:30:00")
# - Returns the formatted information
@mcp_server.tool()
async def send_message(message: Message) -> MessageResponse:
    """Sends a message and returns a response with ID and date."""
    pass

def main():
    print("My first MCP server is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    main()
