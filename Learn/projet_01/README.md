# Project 01: Create a basic MCP server

## Objective

Create your first MCP server with FastMCP. This is the foundation of any MCP project!

## Concepts to learn

### What is MCP?

MCP (Model Context Protocol) is a protocol that allows applications (like Claude Desktop) to communicate with servers that expose **tools**, **resources**, and **prompts**.

### FastMCP

FastMCP is a Python library that simplifies creating MCP servers.

### Basic structure

An MCP server needs:
1. A `FastMCP` instance that represents the server
2. A configuration (name, host, port)
3. An entry point to start the server

## Example structure

A basic MCP server looks like this:

```python
from mcp.server.fastmcp import FastMCP

mcp_host = "127.0.0.1"
mcp_port = 8000
mcp_server = FastMCP(
    "MyServer",
    host=mcp_host,
    port=mcp_port,
    stateless_http=True,
    json_response=True
)
```

And to start it:

```python
mcp_server.run(transport="streamable-http")
```

## What you will create

In this project, you will create a simple MCP server that:
- Is named "MyFirstServer"
- Listens on `127.0.0.1:8000`
- Can be started and displays a message

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
