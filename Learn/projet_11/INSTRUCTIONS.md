# Instructions - Project 11

## Your mission

Create an MCP server that exposes prompts (message templates).

## Steps to follow

1. **Create a FastMCP server** with prompt support:
   ```python
   capabilities={"prompts": {}}
   ```

2. **Create `list_prompts`** decorated with `@mcp_server.list_prompts()`:
   - Returns a list of available prompts
   - Each prompt must have:
     - `name`: Unique identifier (e.g., "greeting")
     - `title`: Readable title (optional)
     - `description`: Prompt description

3. **Create `get_prompt`** decorated with `@mcp_server.get_prompt()`:
   - Takes a parameter `name` (str)
   - Returns a dict with:
     - `messages`: List of messages (format for LLM)
     - Each message has `role` ("user" or "assistant") and `content` with `type: "text"` and `text: "..."`

4. **Create at least 2 prompts**:
   - `greeting`: A greeting message
   - `help`: A help message

## Hints

- Functions must be `async`
- For `get_prompt`, return messages formatted for an LLM
- Message format: `{"role": "user", "content": {"type": "text", "text": "..."}}`

## Test

Use `python test.py` to verify that prompts are listed and retrievable.
