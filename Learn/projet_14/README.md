# Project 14: Use elicitation

## Objective

Learn to use elicitation to request information from users during tool execution.

## Concepts to learn

### What is elicitation?

**Elicitation** allows MCP servers to request additional information from users during tool execution. It's a mechanism that enables interactive workflows.

### Elicitation flow

1. Server sends an elicitation request to the client
2. Client presents the request to the user
3. User responds (or cancels)
4. Client returns the response to the server
5. Server continues with the obtained information

### Elicitation modes

- **Form mode**: Structured data collection via MCP client (for non-sensitive data)
- **URL mode**: Redirect to an external URL (for sensitive data like credentials)

### Usage in FastMCP

In FastMCP, you use Context to request elicitation:
```python
response = await ctx.elicitation.create(
    message="What is your preference?",
    requested_schema={...}
)
```

## What you will create

In this project, you will create a tool that requests information from the user via elicitation.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
