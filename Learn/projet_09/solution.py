from mcp.server.fastmcp import FastMCP
from typing import Any
import re

# TODO: Create the MCP server with resource support
mcp_server = FastMCP(
    "ResourceTemplatesServer",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Add capabilities={"resources": {}}
)

# Simulated configuration
CONFIG_DATA = {
    "database": {
        "host": "localhost",
        "port": "5432",
        "name": "mydb"
    },
    "app": {
        "name": "MyApp",
        "version": "1.0.0",
        "debug": "false"
    }
}

# Simulated virtual files
VIRTUAL_FILES = {
    "readme.txt": "This is a README file\nVersion 1.0",
    "license.txt": "MIT License\nCopyright 2024",
    "changelog.txt": "Version 1.0.0\n- Initial release"
}

# TODO: Implement list_resources for static resources
@mcp_server.list_resources()
async def list_resources() -> list[dict[str, Any]]:
    """
    Lists available static resources.

    Returns:
        List of static resources
    """
    pass

# TODO: Create list_resource_templates
@mcp_server.list_resource_templates()
async def list_resource_templates() -> list[dict[str, Any]]:
    """
    Lists available resource templates.

    Returns:
        List of templates with uriTemplate, name, description, mimeType
    """
    pass

# TODO: Adapt read_resource to handle templates
@mcp_server.read_resource()
async def read_resource(uri: str) -> dict[str, Any]:
    """
    Reads a resource, supports templates.

    Args:
        uri: Resource URI (can be a resolved template)

    Returns:
        Dict with 'contents'

    Raises:
        ValueError: If the URI is not valid
    """
    # TODO: Handle static resources (info://server/about)
    # TODO: Handle config://{section}/{key}
    # TODO: Handle file://{filename}
    pass


def main():
    print("My MCP server with resource templates is starting!")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
