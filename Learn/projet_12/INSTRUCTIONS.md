# Instructions - Project 12

## Your mission

Create prompts with dynamic arguments to personalize content.

## Steps to follow

1. **Use the base from project 11** or create a new server

2. **Modify `list_prompts`** to include arguments:
   - Each prompt can have an `arguments` field (list)
   - Each argument has `name`, `description`, `required`

3. **Modify `get_prompt`** to accept arguments:
   - Takes an `arguments` parameter (dict, optional)
   - Uses arguments to replace placeholders in text
   - Validates that required arguments are present

4. **Create at least 2 prompts with arguments**:
   - `code_review`: Takes `language` (required) and `code` (required)
   - `summary`: Takes `topic` (required) and `length` (optional, default "short")

## Hints

- Use `.format()` or f-strings to replace arguments
- Validate required arguments before generating the message
- If a required argument is missing, raise `ValueError`

## Test

Use `python test.py` to verify that prompts with arguments work.
