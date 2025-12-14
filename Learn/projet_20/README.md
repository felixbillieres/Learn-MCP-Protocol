# Project 20: Introduction to OAuth 2.1 authorization

## Objective

Understand the basic concepts of OAuth 2.1 authorization in MCP.

## Concepts to learn

### Why authorization?

Authorization secures access to sensitive resources and operations. It allows you to:
- Protect user data
- Control who can do what
- Audit actions
- Implement per-user quotas

### OAuth 2.1 in MCP

MCP uses OAuth 2.1 for authorization:
- Client obtains an access token
- Token is included in each HTTP request
- Server validates the token before processing the request

### Authorization flow

1. Client requests authorization from authorization server
2. User authenticates
3. Authorization server returns a token
4. Client uses the token for requests
5. MCP server validates the token

### Important

For this project, we will **simulate** authorization as implementing full OAuth is complex. The goal is to understand the concepts.

## What you will create

In this project, you will create a server that simulates token validation.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
