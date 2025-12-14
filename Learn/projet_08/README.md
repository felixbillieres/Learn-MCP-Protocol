# Project 08: Create your first resource

## Objective

Learn to expose resources with MCP. Resources allow you to expose data that clients can read.

## Concepts to learn

### What is a resource?

A **resource** is a data source that the MCP server exposes to clients. Unlike tools (which are executed), resources are data that the client can read to get context.

**Key difference**:
- **Tools**: Actions the AI can **execute** (modify, create, delete)
- **Resources**: Data the AI can **read** to understand context

### Examples of resources

- File contents
- Database schemas
- System configuration
- Logs
- API data

### How FastMCP handles resources

In FastMCP, you must directly assign the functions:
- `mcp_server.list_resources = list_resources`: Lists available resources
- `mcp_server.read_resource = read_resource`: Reads resource content

**Note**: Unlike tools (`@mcp_server.tool()`), resources use direct assignment, not decorators.

## MCP Documentation

Resources are identified by unique **URIs**:
- Format: `[protocol]://[host]/[path]`
- Example: `file:///home/user/config.json`
- Example: `config://app/settings`

## What you will create

In this project, you will create a server that exposes simple configuration resources.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
