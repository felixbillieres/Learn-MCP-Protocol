# Project 04: Use Context for logging

## Objective

Learn to use the MCP `Context` to log information (info, warning, error) during tool execution.

## Concepts to learn

### What is Context?

The `Context` is an object automatically passed to MCP tools that allows you to:
- **Log information** (`ctx.info()`, `ctx.warning()`, `ctx.error()`)
- **Track execution** of the tool in real time
- **Inform the client** of what's happening

### Context methods

```python
@mcp_server.tool()
async def my_tool(ctx: Context):
    await ctx.info("Starting operation")
    await ctx.warning("Warning, this is a warning")
    await ctx.error("An error occurred")
```

**Important**: These methods are `async`! You must use `await`.

### Why use Context?

- Allows the client to see what's happening in real time
- Useful for debugging
- Provides visibility on execution
- Can inform the user of problems without stopping execution

## What you will create

In this project, you will create a tool that:
- Uses Context to log steps
- Displays info, warning, and error messages according to the context
- Shows how logging helps understand what's happening

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
