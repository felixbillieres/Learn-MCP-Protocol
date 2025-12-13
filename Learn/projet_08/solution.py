from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Crée le serveur MCP avec support des resources
mcp_server = FastMCP(
    "MonServeurResources",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Ajoute capabilities={"resources": {}}
)

# Données des ressources (stockage en mémoire)
RESOURCES = {
    "config://app/settings": {
        "name": "Paramètres de l'application",
        "description": "Configuration principale de l'application",
        "mimeType": "application/json",
        "content": '{"theme": "dark", "language": "fr", "notifications": true}'
    },
    "info://server/version": {
        "name": "Version du serveur",
        "description": "Informations sur la version du serveur MCP",
        "mimeType": "text/plain",
        "content": "Version 1.0.0\nBuild: 2024-01-15"
    }
}

# TODO: Crée la fonction list_resources
async def list_resources() -> list[dict[str, Any]]:
    """
    Liste toutes les ressources disponibles.

    Returns:
        Liste de dictionnaires avec uri, name, description, mimeType
    """
    pass

# TODO: Enregistre la fonction avec FastMCP
# mcp_server.list_resources = list_resources

# TODO: Crée la fonction read_resource
async def read_resource(uri: str, ctx: Context = None) -> dict[str, Any]:
    """
    Lit le contenu d'une ressource.

    Args:
        uri: L'URI de la ressource à lire

    Returns:
        Dict avec 'contents' contenant une liste de contenus

    Raises:
        ValueError: Si l'URI n'existe pas
    """
    pass

# TODO: Enregistre la fonction avec FastMCP
# mcp_server.read_resource = read_resource

def main():
    print("Mon serveur MCP avec resources démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
