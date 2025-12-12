from mcp.server.fastmcp import FastMCP, Context
from typing import Optional
import time

# TODO: Crée le serveur MCP
mcp_server = FastMCP(
    "MonServeurAuth",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# Tokens valides simulés (en production, ceci serait en base de données)
VALID_TOKENS = {
    "Bearer token123": {
        "user_id": "user1",
        "username": "alice",
        "email": "alice@example.com",
        "expires_at": time.time() + 3600  # Expire dans 1h
    },
    "Bearer token456": {
        "user_id": "user2",
        "username": "bob",
        "email": "bob@example.com",
        "expires_at": time.time() + 3600
    }
}

# TODO: Crée la fonction valider_token
def valider_token(token: str) -> Optional[dict]:
    """
    Valide un token et retourne les infos utilisateur.
    
    Args:
        token: Le token à valider (format "Bearer ...")
        
    Returns:
        Dict avec user info si valide, None sinon
    """
    # TODO: Vérifie que le token commence par "Bearer "
    # TODO: Vérifie que le token existe dans VALID_TOKENS
    # TODO: Vérifie que le token n'est pas expiré
    # TODO: Retourne les infos utilisateur si valide
    
    pass

# TODO: Crée l'outil info_utilisateur
@mcp_server.tool()
async def info_utilisateur(
    token: str,
    ctx: Context
) -> dict:
    """
    Récupère les informations de l'utilisateur authentifié.
    
    Args:
        token: Token d'autorisation
        ctx: Context MCP
        
    Returns:
        Dict avec les infos utilisateur
        
    Raises:
        ValueError: Si le token est invalide
    """
    # TODO: Valide le token
    # TODO: Si invalide, lève ValueError
    # TODO: Retourne les infos utilisateur
    
    pass

# TODO: Crée l'outil donnees_sensibles
@mcp_server.tool()
async def donnees_sensibles(
    token: str,
    ctx: Context
) -> dict:
    """
    Accède à des données sensibles (nécessite authentification).
    
    Args:
        token: Token d'autorisation
        ctx: Context MCP
        
    Returns:
        Les données sensibles
        
    Raises:
        ValueError: Si le token est invalide
    """
    # TODO: Valide le token
    # TODO: Retourne des données sensibles simulées
    
    pass


def main():
    print("Mon serveur MCP avec autorisation démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

