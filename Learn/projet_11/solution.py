from mcp.server.fastmcp import FastMCP
from typing import Any

# TODO: Crée le serveur MCP avec support des prompts
mcp_server = FastMCP(
    "MonServeurPrompts",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Ajoute capabilities={"prompts": {}}
)

# Définitions des prompts
PROMPTS = {
    "greeting": {
        "title": "Salutation",
        "description": "Un message de salutation amical",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "Salut ! Comment puis-je t'aider aujourd'hui ?"
                }
            }
        ]
    },
    "help": {
        "title": "Aide",
        "description": "Obtenir de l'aide sur le système",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "J'ai besoin d'aide. Peux-tu me donner des informations sur les fonctionnalités disponibles ?"
                }
            }
        ]
    }
}

# TODO: Crée la fonction list_prompts
@mcp_server.list_prompts()
async def list_prompts() -> list[dict[str, Any]]:
    """
    Liste tous les prompts disponibles.
    
    Returns:
        Liste de prompts avec name, title, description
    """
    pass

# TODO: Crée la fonction get_prompt
@mcp_server.get_prompt()
async def get_prompt(name: str) -> dict[str, Any]:
    """
    Récupère un prompt par son nom.
    
    Args:
        name: Le nom du prompt
        
    Returns:
        Dict avec 'messages' contenant les messages formatés
        
    Raises:
        ValueError: Si le prompt n'existe pas
    """
    pass


def main():
    print("Mon serveur MCP avec prompts démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

