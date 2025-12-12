from mcp.server.fastmcp import FastMCP, Context
from typing import Any
import re

# TODO: Crée le serveur MCP
mcp_server = FastMCP(
    "MonServeurElicitationSchemas",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Crée l'outil inscription avec schéma détaillé
@mcp_server.tool()
async def inscription(ctx: Context) -> dict[str, Any]:
    """
    Inscrit un nouvel utilisateur avec validation via elicitation.
    
    Returns:
        Dict avec message de confirmation
    """
    # TODO: Crée le schéma avec :
    # - username: string, minLength 3, maxLength 20, pattern alphanumeric
    # - email: string, format email
    # - age: integer, minimum 13, maximum 120
    # - newsletter: boolean, défaut false
    
    schema = {
        "type": "object",
        "properties": {
            # TODO: Ajoute les propriétés avec leurs contraintes
        },
        "required": []  # TODO: Ajoute les champs requis
    }
    
    # TODO: Utilise ctx.elicitation.create() avec le schéma
    # TODO: Valide les données reçues (double validation pour sécurité)
    # TODO: Retourne un message de confirmation
    pass

# TODO: Fonction de validation
def validate_username(username: str) -> bool:
    """Valide le username selon les règles."""
    if len(username) < 3 or len(username) > 20:
        return False
    if not re.match(r"^[a-zA-Z0-9]+$", username):
        return False
    return True

def validate_email(email: str) -> bool:
    """Valide le format email."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# TODO: Crée l'outil commander_produit avec enum
@mcp_server.tool()
async def commander_produit(ctx: Context) -> dict[str, Any]:
    """
    Commande un produit avec sélection via enum.
    
    Returns:
        Dict avec résumé de commande
    """
    # TODO: Crée le schéma avec :
    # - produit: enum ["basic", "premium", "enterprise"]
    # - quantite: integer, min 1, max 100
    # - livraison_express: boolean
    
    # TODO: Utilise ctx.elicitation.create()
    # TODO: Retourne un résumé
    pass


def main():
    print("Mon serveur MCP avec elicitation et schémas démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

