# Instructions - Project 15

## Your mission

Create tools with complex and validated elicitation schemas.

## Steps to follow

1. **Create a basic FastMCP server**

2. **Create a `register` tool** with a detailed schema:
   - Requests:
     - `username`: string, minLength 3, maxLength 20, alphanumeric pattern
     - `email`: string, email format
     - `age`: integer, minimum 13, maximum 120
     - `newsletter`: boolean, default false
   - Validates received data
   - Returns a confirmation message

3. **Create an `order_product` tool** with enum:
   - Requests:
     - `product`: enum with values "basic", "premium", "enterprise"
     - `quantity`: integer, minimum 1, maximum 100
     - `express_delivery`: boolean
   - Returns an order summary

4. **Validate responses**:
   - Checks that values respect schema constraints
   - Raises appropriate errors if validation fails

## Hints

- The schema must strictly follow JSON Schema
- Use `pattern` for regex validation (e.g., `"^[a-zA-Z0-9]+$"`)
- Formats like `email` are automatically validated by the client
- Also validate on the server side for security

## Test

The test will verify that schemas are correctly structured.
