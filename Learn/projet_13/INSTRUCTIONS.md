# Instructions - Project 13

## Your mission

Create advanced prompts with multiple messages and resource references.

## Steps to follow

1. **Create a server** with support for prompts AND resources

2. **Create resources**:
   - `doc://examples/code_sample`: A code example
   - `doc://guidelines/best_practices`: Best practices

3. **Create an advanced `tutorial` prompt**:
   - Takes an argument `topic` (required)
   - Returns multiple messages:
     1. System message explaining the context
     2. User message with the question
     3. (Optional) Assistant message with an example

4. **Create a `code_analysis` prompt**:
   - Takes `code` (required)
   - Returns a message that references a resource containing guidelines
   - Uses the integrated resource format in the message

## Hints

- For integrated resources, use the format: `{"type": "resource", "resource": {...}}`
- Multiple messages allow you to create a rich context
- Combine resources and arguments for powerful prompts

## Test

Use `python test.py` to verify that advanced prompts work.
