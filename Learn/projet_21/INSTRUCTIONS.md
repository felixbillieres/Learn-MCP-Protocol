# Instructions - Project 21

## Your mission

Create token validation with scopes and audiences.

## Steps to follow

1. **Create a FastMCP server**

2. **Enhance `validate_token`** to accept:
   - `required_scopes`: List of required scopes (optional)
   - `required_audience`: Required audience (optional)

3. **Add tokens with scopes and audiences**:
   - Token with scopes: "read:data", "write:data"
   - Token with audience: "api.example.com"

4. **Create tools that require scopes**:
   - `read_data`: Requires scope "read:data"
   - `write_data`: Requires scope "write:data"
