# Project 05: Error handling and validation

## Objective

Learn to handle errors properly in your MCP tools, with data validation and clear error messages.

## Concepts to learn

### Why handle errors?

In MCP, you must:
- **Validate inputs** before using them
- **Handle error cases** properly
- **Return clear messages** to the client
- **Use Context** to log errors

### Error types in Python

```python
# ValueError: invalid value
if age < 0:
    raise ValueError("Age cannot be negative")

# RuntimeError: runtime error
if not resource_available:
    raise RuntimeError("Resource is not available")

# KeyError, TypeError, etc.: native Python errors
```

### Best practice: Validate early, always log

```python
@mcp_server.tool()
async def my_tool(param: str, ctx: Context):
    # 1. Validate inputs
    if not param:
        await ctx.error("Parameter cannot be empty")
        raise ValueError("param is empty")

    # 2. Log the start
    await ctx.info(f"Processing {param}")

    # 3. Try the operation
    try:
        result = do_operation(param)
    except SpecificError as e:
        await ctx.error(f"Error during operation: {e}")
        raise RuntimeError(f"Cannot process {param}") from e

    # 4. Return the result
    return result
```

## What you will create

In this project, you will create a tool that:
- Validates input parameters
- Handles different error cases
- Uses Context to log errors
- Returns clear error messages

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
