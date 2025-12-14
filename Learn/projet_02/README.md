# Project 02: Add your first tool

## Objective

Add your first tool to your MCP server. Tools are functions that MCP clients can call!

## Concepts to learn

### What is a tool?

A tool is a Python function decorated with `@mcp_server.tool()` that:
- Can receive parameters
- Can return results
- Is automatically exposed by the MCP server
- Can be called by MCP clients (like Claude Desktop)

### The decorator @mcp_server.tool()

This decorator transforms a normal Python function into an MCP tool. Example:

```python
@mcp_server.tool()
async def my_function(param1: str, param2: int) -> str:
    """Tool description"""
    return f"Result: {param1} and {param2}"
```

**Important**: Tools must be `async` (asynchronous) functions!

### Docstring = Description

Your function's docstring becomes the tool's description in MCP. This is what will be visible to clients!

## What you will create

In this project, you will create two simple tools:
1. `say_hello`: takes a name parameter and returns a greeting message
2. `calculate_sum`: takes two numbers and returns their sum

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
