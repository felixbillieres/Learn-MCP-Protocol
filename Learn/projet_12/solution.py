from mcp.server.fastmcp import FastMCP
from typing import Any, Optional

# TODO: Crée le serveur MCP avec support des prompts
mcp_server = FastMCP(
    "MonServeurPromptsArgs",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Ajoute capabilities={"prompts": {}}
)

# TODO: Définis les prompts avec leurs arguments
# Chaque prompt doit avoir : name, title, description, arguments (liste), et un template
PROMPTS = {
    # TODO: Ajoute code_review avec arguments: language (requis), code (requis)
    # TODO: Ajoute summary avec arguments: topic (requis), length (optionnel, défaut "short")
}

# TODO: Crée la fonction list_prompts avec les arguments
@mcp_server.list_prompts()
async def list_prompts() -> list[dict[str, Any]]:
    """
    Liste tous les prompts disponibles avec leurs arguments.
    
    Returns:
        Liste de prompts avec name, title, description, arguments
    """
    pass

# TODO: Crée la fonction get_prompt qui accepte des arguments
@mcp_server.get_prompt()
async def get_prompt(
    name: str,
    arguments: Optional[dict[str, Any]] = None
) -> dict[str, Any]:
    """
    Récupère un prompt par son nom avec des arguments optionnels.
    
    Args:
        name: Le nom du prompt
        arguments: Dict avec les valeurs des arguments (optionnel)
        
    Returns:
        Dict avec 'messages' contenant les messages formatés
        
    Raises:
        ValueError: Si le prompt n'existe pas ou si des arguments requis manquent
    """
    if arguments is None:
        arguments = {}
    
    # TODO: Vérifie que le prompt existe
    # TODO: Valide les arguments requis
    # TODO: Remplace les placeholders dans le template avec les arguments
    # TODO: Retourne les messages formatés
    pass


def main():
    print("Mon serveur MCP avec prompts et arguments démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

