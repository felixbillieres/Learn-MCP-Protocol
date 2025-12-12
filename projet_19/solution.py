from mcp.server.fastmcp import FastMCP, Context
from typing import Any

# TODO: Crée le serveur MCP
mcp_server = FastMCP(
    "MonServeurAgentique",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Crée des outils simples que le LLM pourra utiliser
@mcp_server.tool()
async def calculer(expression: str, ctx: Context) -> float:
    """
    Évalue une expression mathématique simple.
    
    Args:
        expression: Expression à évaluer (ex: "2 + 2")
        ctx: Context MCP
        
    Returns:
        Le résultat du calcul
    """
    # TODO: Évalue l'expression (utilise eval avec précaution ou une bibliothèque sécurisée)
    # Pour ce projet, on peut utiliser eval() mais en production utilise une bibliothèque sécurisée
    pass

@mcp_server.tool()
async def rechercher_info(terme: str, ctx: Context) -> str:
    """
    Recherche des informations sur un terme (simulé).
    
    Args:
        terme: Le terme à rechercher
        ctx: Context MCP
        
    Returns:
        Informations sur le terme
    """
    # TODO: Simule une recherche (retourne des infos hardcodées)
    pass

@mcp_server.tool()
async def convertir_unite(
    valeur: float,
    unite_source: str,
    unite_cible: str,
    ctx: Context
) -> float:
    """
    Convertit une valeur d'une unité à une autre.
    
    Args:
        valeur: La valeur à convertir
        unite_source: Unité source (ex: "km", "m", "kg")
        unite_cible: Unité cible
        ctx: Context MCP
        
    Returns:
        La valeur convertie
    """
    # TODO: Implémente des conversions basiques (km->m, kg->g, etc.)
    pass

# Définitions des outils pour le LLM (format MCP)
TOOLS_FOR_LLM = [
    {
        "name": "calculer",
        "description": "Évalue une expression mathématique simple",
        "inputSchema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Expression mathématique à évaluer"
                }
            },
            "required": ["expression"]
        }
    },
    # TODO: Ajoute les définitions pour rechercher_info et convertir_unite
]

# TODO: Crée l'outil agent_resolveur
@mcp_server.tool()
async def agent_resolveur(
    question: str,
    ctx: Context
) -> str:
    """
    Utilise un agent LLM avec outils pour résoudre une question complexe.
    
    Args:
        question: La question à résoudre
        ctx: Context MCP
        
    Returns:
        La réponse de l'agent
    """
    # TODO: Utilise ctx.sampling.create_message() avec :
    # - messages: [{"role": "user", "content": {"type": "text", "text": question}}]
    # - tools: TOOLS_FOR_LLM
    # - max_tokens: 500
    
    # Le LLM pourra appeler les outils automatiquement
    pass


def main():
    print("Mon serveur MCP avec workflows agentiques démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

