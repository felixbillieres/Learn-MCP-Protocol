# Project 16: Elicitation URL mode

## Objective

Learn to use URL mode elicitation for sensitive interactions that should not go through the MCP client.

## Concepts to learn

### URL mode vs Form mode

- **Form mode**: Data collection via MCP client (for non-sensitive data)
- **URL mode**: Redirect to an external URL (for sensitive data like credentials)

### When to use URL mode?

URL mode is **required** for:
- Credentials (passwords, API tokens)
- Payment information
- Sensitive personal data
- OAuth authentication

### Security

URL mode ensures that sensitive data never passes through the MCP client, but is collected directly on the authorization server.

## What you will create

In this project, you will create a tool that uses URL mode elicitation for authentication.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
