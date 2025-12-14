# Instructions - Project 08

## Your mission

Create an MCP server that exposes configuration resources.

## Steps to follow

1. **Create a basic FastMCP server** (resource support is automatically detected)

2. **Create a `list_resources` function** and register it with FastMCP:
   ```python
   async def list_resources() -> list[dict[str, Any]]:
       # Implement the logic
       pass
   
   # Register the function
   mcp_server.list_resources = list_resources
   ```
   - Returns a list of resources
   - Each resource must have:
     - `uri`: The unique URI (e.g., `"config://app/settings"`)
     - `name`: A short name
     - `description`: Resource description
     - `mimeType`: MIME type (e.g., `"application/json"` or `"text/plain"`)

3. **Create a `read_resource` function** and register it with FastMCP:
   ```python
   async def read_resource(uri: str, ctx: Context = None) -> dict[str, Any]:
       # Implement the logic
       pass
   
   # Register the function
   mcp_server.read_resource = read_resource
   ```
   - Takes a parameter `uri` (str)
   - Returns the resource content
   - If the URI doesn't exist, raises a `ValueError`

4. **Expose at least 2 resources**:
   - `config://app/settings`: App configuration (JSON)
   - `info://server/version`: Server version (text)

## Hints

- Functions must be `async`
- **Important**: In FastMCP, you must directly assign the functions (`mcp_server.list_resources = list_resources`) instead of using decorators
- For `read_resource`, return a dict with `contents` containing a list
- Each content has: `uri`, `mimeType`, and either `text` (for text) or `blob` (for base64 binary)

## Test

Use `python test.py` to verify that resources are listed and readable.
