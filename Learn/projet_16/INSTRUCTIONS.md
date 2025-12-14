# Instructions - Project 16

## Your mission

Create a tool that uses URL mode elicitation for secure authentication.

## Steps to follow

1. **Create a basic FastMCP server**

2. **Create an `authenticate` tool**:
   - Uses `ctx.elicitation.create()` with `mode="url"`
   - Requests an authentication URL (e.g., `https://auth.example.com/login`)
   - Returns a message indicating the user must authenticate via the URL

3. **Create a `configure_api_key` tool**:
   - Also uses URL mode
   - Redirects to a page to configure an API key
   - Returns a confirmation

4. **Important**:
   - For URL mode, use `mode="url"` in elicitation
   - The provided URL must be complete (with https://)
   - The server must clearly explain why the URL is necessary

## Hints

- URL mode uses the same API but with `mode: "url"` and a `url` instead of `requested_schema`
- The format is: `{"mode": "url", "message": "...", "url": "https://..."}`
- The user will be redirected to the URL to complete the action

## Test

The test will verify that tools use URL mode correctly.
