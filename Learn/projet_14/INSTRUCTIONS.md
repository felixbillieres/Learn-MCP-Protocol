# Instructions - Project 14

## Your mission

Create a tool that uses elicitation to request information from the user.

## Steps to follow

1. **Create a basic FastMCP server**

2. **Create a `create_profile` tool**:
   - Takes no parameters (or only `ctx: Context`)
   - Uses `await ctx.elicitation.create()` to request:
     - Name (string)
     - Age (integer)
     - Email (string, optional)
   - Returns a dict with collected information

3. **Create a `configure_preferences` tool**:
   - Requests via elicitation:
     - Preferred theme (enum: "dark", "light", "auto")
     - Notifications enabled (boolean)
   - Returns preferences

## Hints

- Elicitation requires a JSON schema to define requested fields
- Use `ctx.elicitation.create()` with `message` and `requested_schema`
- The schema follows JSON Schema format (type, title, description, etc.)
- The response is a dict with provided values

## Test

Note: Elicitation requires a real MCP client to be tested. The test will verify that the tool can be called.
