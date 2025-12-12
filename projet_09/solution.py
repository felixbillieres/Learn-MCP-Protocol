from mcp.server.fastmcp import FastMCP
from typing import Any
import re

# TODO: Crée le serveur MCP avec support des resources
mcp_server = FastMCP(
    "MonServeurResourcesTemplates",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Ajoute capabilities={"resources": {}}
)

# Configuration simulée
CONFIG_DATA = {
    "database": {
        "host": "localhost",
        "port": "5432",
        "name": "mydb"
    },
    "app": {
        "name": "MonApp",
        "version": "1.0.0",
        "debug": "false"
    }
}

# Fichiers virtuels simulés
VIRTUAL_FILES = {
    "readme.txt": "Ceci est un fichier README\nVersion 1.0",
    "license.txt": "MIT License\nCopyright 2024",
    "changelog.txt": "Version 1.0.0\n- Initial release"
}

# TODO: Implémente list_resources pour les resources statiques
@mcp_server.list_resources()
async def list_resources() -> list[dict[str, Any]]:
    """
    Liste les resources statiques disponibles.

    Returns:
        Liste de resources statiques
    """
    pass

# TODO: Crée list_resource_templates
@mcp_server.list_resource_templates()
async def list_resource_templates() -> list[dict[str, Any]]:
    """
    Liste les templates de resources disponibles.

    Returns:
        Liste de templates avec uriTemplate, name, description, mimeType
    """
    pass

# TODO: Adapte read_resource pour gérer les templates
@mcp_server.read_resource()
async def read_resource(uri: str) -> dict[str, Any]:
    """
    Lit une resource, supporte les templates.

    Args:
        uri: URI de la resource (peut être un template résolu)

    Returns:
        Dict avec 'contents'

    Raises:
        ValueError: Si l'URI n'est pas valide
    """
    # TODO: Gère les resources statiques (info://server/about)
    # TODO: Gère config://{section}/{key}
    # TODO: Gère file://{filename}
    pass


def main():
    print("Mon serveur MCP avec resource templates démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()