# Instructions - Project 02

## Your mission

Add two simple tools to your MCP server.

## Steps to follow

1. **Use the server from project 01** as a base (or create a new one)

2. **Create the `say_hello` tool**:
   - Takes a parameter `name` (type `str`)
   - Returns a string with a message: `f"Hello, {name}! How are you?"`
   - Add a descriptive docstring
   - Use the decorator `@mcp_server.tool()`
   - The function must be `async`

3. **Create the `calculate_sum` tool**:
   - Takes two parameters `a` and `b` (type `int`)
   - Returns an `int`: the sum of a and b
   - Add a descriptive docstring
   - Use the decorator `@mcp_server.tool()`
   - The function must be `async`

## Hints

- Don't forget the `async` before `def`!
- Don't forget the decorator `@mcp_server.tool()` right before the function
- The docstring is important to describe the tool
- Parameter and return types are important (MCP uses them)

## Test

Use `python test.py` to verify that:
- The tools are properly registered
- The tools work correctly

## Expected result

When you start the server and a client calls it:
- `say_hello("Alice")` should return `"Hello, Alice! How are you?"`
- `calculate_sum(5, 3)` should return `8`
