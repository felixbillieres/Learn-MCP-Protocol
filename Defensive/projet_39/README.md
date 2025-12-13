# Project 39 : Secrets Manager

## Objective

Create an MCP server to securely manage secrets (passwords, tokens, keys) with strict access control.

## Concepts to Learn

### Secrets Management

Secrets require:
- **Encryption** : Protect at rest and in transit
- **Access Control** : Who can access what
- **Audit Logging** : Track all access
- **Rotation** : Regular secret updates

### MCP Architecture

- **Tools** : CRUD for secrets
- **Resources** : Expose secrets (with masking)
- **Authorization** : Strict token and scope validation
- **Elicitation** : Confirm access requests

## Use Cases

- Store passwords and API keys
- Manage encryption keys
- Control access to secrets
- Audit secret access

