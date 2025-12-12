from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Crée le serveur MCP
mcp_server = FastMCP(
    "MonServeurSamplingAvance",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Crée l'outil creatif_ideation
@mcp_server.tool()
async def creatif_ideation(
    sujet: str,
    ctx: Context
) -> str:
    """
    Génère des idées créatives sur un sujet.
    
    Args:
        sujet: Le sujet pour l'idéation
        ctx: Context MCP
        
    Returns:
        Les idées générées
    """
    # TODO: Utilise ctx.sampling.create_message() avec :
    # - temperature: 0.9
    # - model_preferences: {"intelligencePriority": 0.8}
    # - messages: demande des idées créatives
    
    pass

# TODO: Crée l'outil conversation
@mcp_server.tool()
async def conversation(
    messages_historique: list[dict[str, Any]],
    nouveau_message: str,
    ctx: Context
) -> str:
    """
    Continue une conversation avec historique.
    
    Args:
        messages_historique: Liste des messages précédents
        nouveau_message: Le nouveau message
        ctx: Context MCP
        
    Returns:
        La réponse du LLM
    """
    # TODO: Construit la liste complète de messages
    # TODO: Utilise max_tokens: 500
    # TODO: Appelle le sampling
    
    pass

# TODO: Crée l'outil reponse_rapide
@mcp_server.tool()
async def reponse_rapide(
    question: str,
    ctx: Context
) -> str:
    """
    Génère une réponse rapide (optimisée pour la vitesse).
    
    Args:
        question: La question
        ctx: Context MCP
        
    Returns:
        Une réponse courte et rapide
    """
    # TODO: Utilise sampling avec :
    # - speedPriority élevé
    # - max_tokens: 100
    
    pass


def main():
    print("Mon serveur MCP avec sampling avancé démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

