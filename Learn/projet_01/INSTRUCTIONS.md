# Instructions - Project 01

## Your mission

Create a basic MCP server that displays a startup message.

## Steps to follow

1. **Create a FastMCP server** in `solution.py`:
   - Server name: `"MyFirstServer"`
   - Host: `"127.0.0.1"`
   - Port: `8000`
   - Options: `stateless_http=True` and `json_response=True`

2. **Create a `main()` function** that:
   - Displays a message: `"My first MCP server is starting!"`
   - Displays the server URL: `"URL: http://127.0.0.1:8000/mcp"`
   - Starts the server with `mcp_server.run(transport="streamable-http")`

3. **Add the entry point** `if __name__ == "__main__": main()`

## Hints

- Import `FastMCP` from `mcp.server.fastmcp`
- Don't worry if the server doesn't do anything else for now, that's normal!

## Test

Once finished, run `python solution.py` and verify that:
- The message is displayed
- The server starts (it will stay listening, that's normal)

To test, you can also use `python test.py` which verifies that the server is created correctly.

## Expected result

When you start the server, you should see:
```
My first MCP server is starting!
URL: http://127.0.0.1:8000/mcp
```

The server then stays listening (press Ctrl+C to stop it).
