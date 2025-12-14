# Instructions - Project 20

## Your mission

Create a server that simulates OAuth token validation.

## Steps to follow

1. **Create a basic FastMCP server**

2. **Create a `validate_token` function**:
   - Takes a token (str)
   - Simulates validation (checks format, expiration, etc.)
   - Returns a dict with user info if valid
   - Returns None if invalid

3. **Create a `user_info` tool**:
   - Requires a valid token (simulated via `token` parameter)
   - Validates the token
   - Returns user info

4. **Create a `sensitive_data` tool**:
   - Also requires a valid token
   - Simulates access to sensitive data
   - Returns data if authorized

## Hints

- For this project, we simulate authorization (not real OAuth)
- In a real server, FastMCP automatically handles HTTP tokens
- You can store valid tokens in a dict for simulation
- Validate token format (e.g., must start with "Bearer ")

## Test

The test will verify that validation works.
