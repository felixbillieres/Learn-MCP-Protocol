from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Crée le serveur MCP
mcp_server = FastMCP(
    "MonServeurElicitationURL",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# Configuration (simulée)
AUTH_URL = "https://auth.example.com/login"
API_KEY_URL = "https://auth.example.com/api-keys"

# TODO: Crée l'outil authentifier avec URL mode
@mcp_server.tool()
async def authentifier(ctx: Context) -> dict[str, Any]:
    """
    Authentifie l'utilisateur via URL mode pour la sécurité.
    
    Returns:
        Dict avec message de confirmation
    """
    # TODO: Utilise ctx.elicitation.create() avec mode="url"
    # Format: {
    #     "mode": "url",
    #     "message": "Veuillez vous authentifier via l'URL suivante",
    #     "url": "https://..."
    # }
    
    # TODO: Après l'authentification (simulée), retourne un message
    pass

# TODO: Crée l'outil configurer_api_key avec URL mode
@mcp_server.tool()
async def configurer_api_key(ctx: Context) -> dict[str, Any]:
    """
    Configure une clé API via URL mode (données sensibles).
    
    Returns:
        Dict avec confirmation
    """
    # TODO: Utilise URL mode pour rediriger vers la page de configuration
    # TODO: Retourne une confirmation
    pass


def main():
    print("Mon serveur MCP avec elicitation URL mode démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

