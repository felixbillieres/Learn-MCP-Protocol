# Instructions - Project 03

## Your mission

Create a Pydantic model and use it in an MCP tool.

## Steps to follow

1. **Create a Pydantic `Message` model** in `solution.py`:
   - Inherits from `BaseModel`
   - Fields:
     - `sender`: str (required, description "Sender's name")
     - `recipient`: str (required, description "Recipient's name")
     - `content`: str (required, description "Message content")
     - `priority`: str (optional, default "normal", description "Message priority")
   - Use `Field()` for descriptions

2. **Create a Pydantic `MessageResponse` model**:
   - `message_id`: int (description "Unique message ID")
   - `sender`: str
   - `recipient`: str
   - `content`: str
   - `priority`: str
   - `send_date`: str (description "Message send date")

3. **Create a `send_message` tool**:
   - Takes a parameter `message` of type `Message`
   - Returns a `MessageResponse`
   - Generates a random `message_id` (or use a counter)
   - Creates the send date (simple string format: "2024-01-15 10:30:00")
   - Returns the formatted information

## Hints

- Import `BaseModel` and `Field` from `pydantic`
- Pydantic models inherit from `BaseModel`
- `Field()` allows you to add descriptions and constraints
- To generate an ID, you can use `import random; random.randint(1, 10000)`
- For the date, you can use `from datetime import datetime; datetime.now().strftime("%Y-%m-%d %H:%M:%S")`

## Test

Use `python test.py` to verify that:
- Models are properly defined
- Validation works
- The tool works correctly

## Expected result

When you call `send_message` with a message, you should receive a `MessageResponse` with all the completed information (ID, date, etc.).
