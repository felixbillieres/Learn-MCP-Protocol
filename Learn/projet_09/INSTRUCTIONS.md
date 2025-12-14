# Instructions - Project 09

## Your mission

Create resources with URI templates to access configuration files dynamically.

## Steps to follow

1. **Create a FastMCP server** with resource support

2. **Implement `list_resources`** for static resources:
   - Returns a static resource: `info://server/about` with server info

3. **Create `list_resource_templates`** decorated with `@mcp_server.list_resource_templates()`:
   - Returns a list of templates
   - Each template must have:
     - `uriTemplate`: The URI template (e.g., `"config://{section}/{key}"`)
     - `name`: Template name
     - `description`: Description
     - `mimeType`: MIME type

4. **Adapt `read_resource`** to handle templates:
   - If the URI matches a template (e.g., `config://database/host`), extract the parameters
   - Return the appropriate content
   - If the URI doesn't match any template, raise `ValueError`

5. **Templates to create**:
   - `config://{section}/{key}`: Access configurations by section/key
   - `file://{filename}`: Access virtual files

## Hints

- Use `re` or `urllib.parse` to parse URIs and extract parameters
- Store simulated configuration data in a dict
- For `config://{section}/{key}`, parse the URI to extract `section` and `key`

## Test

Use `python test.py` to verify that templates work.
