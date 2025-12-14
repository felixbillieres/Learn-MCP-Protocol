# Project 17: Use sampling to request LLM completions

## Objective

Learn to use sampling to request language model completions via the MCP client.

## Concepts to learn

### What is sampling?

**Sampling** allows MCP servers to request LLM completions from the client. This allows servers to use AI without needing their own API keys.

### Advantages

- No need for API keys in the server
- Client controls which model to use
- User can see and modify prompts before sending
- Security: client-side control

### Sampling flow

1. Server sends `sampling/createMessage` with messages and parameters
2. Client presents the request to the user (who can modify)
3. Client sends to LLM
4. Client presents the response (which can be modified)
5. Client returns the response to the server

### Usage in FastMCP

In FastMCP, you use Context to request sampling:
```python
response = await ctx.sampling.create_message(
    messages=[...],
    max_tokens=100
)
```

## What you will create

In this project, you will create a tool that uses sampling to get a response from an LLM.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
