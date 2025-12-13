from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Crée le serveur MCP
mcp_server = FastMCP(
    "MonServeurElicitation",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Crée l'outil creer_profil
@mcp_server.tool()
async def creer_profil(ctx: Context) -> dict[str, Any]:
    """
    Crée un profil utilisateur en demandant les informations via elicitation.
    
    Returns:
        Dict avec les informations du profil créé
    """
    # TODO: Utilise ctx.elicitation.create() pour demander:
    # - nom (string, requis)
    # - age (integer, requis)
    # - email (string, optionnel)
    # 
    # Schema exemple pour un champ:
    # {
    #     "type": "object",
    #     "properties": {
    #         "nom": {"type": "string", "title": "Nom", "description": "Votre nom"}
    #     },
    #     "required": ["nom"]
    # }
    
    # TODO: Retourne les informations collectées
    pass

# TODO: Crée l'outil configurer_preferences
@mcp_server.tool()
async def configurer_preferences(ctx: Context) -> dict[str, Any]:
    """
    Configure les préférences utilisateur via elicitation.
    
    Returns:
        Dict avec les préférences configurées
    """
    # TODO: Utilise ctx.elicitation.create() pour demander:
    # - theme (enum: "dark", "light", "auto")
    # - notifications (boolean)
    
    # TODO: Retourne les préférences
    pass


def main():
    print("Mon serveur MCP avec elicitation démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

