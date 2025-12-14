# Instructions - Project 18

## Your mission

Create tools that use advanced sampling parameters.

## Steps to follow

1. **Create a basic FastMCP server**

2. **Create a `creative_ideation` tool**:
   - Takes `topic` (str) and `ctx: Context`
   - Uses sampling with:
     - `temperature`: 0.9 (creative)
     - `model_preferences`: high intelligencePriority
     - Requests creative ideas on the topic
   - Returns the ideas

3. **Create a `conversation` tool**:
   - Takes `message_history` (list of dict) and `new_message` (str) and `ctx: Context`
   - Builds a conversation with history
   - Uses `max_tokens`: 500
   - Returns the response

4. **Create a `quick_response` tool**:
   - Takes `question` (str) and `ctx: Context`
   - Uses sampling with:
     - `speed_priority`: high
     - `max_tokens`: 100 (short response)
   - Returns a quick response

## Hints

- Use `model_preferences` with `intelligencePriority`, `speedPriority`, etc.
- `temperature` controls creativity (0 = deterministic, 2 = very creative)
- For conversations, pass all messages in the list

## Test

The test will verify that tools use advanced parameters.
