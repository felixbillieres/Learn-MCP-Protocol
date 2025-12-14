# Instructions - Project 17

## Your mission

Create a tool that uses sampling to request an LLM completion.

## Steps to follow

1. **Create a basic FastMCP server**

2. **Create a `ask_question` tool**:
   - Takes a parameter `question` (str) and `ctx: Context`
   - Uses `await ctx.sampling.create_message()` to request a response from the LLM
   - Builds a message with role "user" and content with type "text"
   - Returns the LLM response

3. **Create a `generate_summary` tool**:
   - Takes a parameter `text` (str) and `ctx: Context`
   - Asks the LLM to generate a summary of the text
   - Uses a system prompt to guide the LLM
   - Returns the summary

## Hints

- Use `ctx.sampling.create_message()` with a list of `messages`
- Each message has `role` ("user" or "system") and `content` with `type: "text"` and `text: "..."`
- For system prompt, use `system_prompt` as parameter or a message with role "system"
- The response contains `role`, `content`, and possibly `model` and `stop_reason`

## Test

Note: Sampling requires a real MCP client with LLM. The test will verify that the tool can be called.
