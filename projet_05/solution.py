from mcp.server.fastmcp import FastMCP, Context

# TODO: Importe math pour math.isinf()

# Crée le serveur MCP
mcp_server = FastMCP(
    "MonPremierServeur",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Crée l'outil calculer_division avec gestion d'erreurs complète
@mcp_server.tool()
async def calculer_division(
    dividende: float,
    diviseur: float,
    ctx: Context
) -> float:
    """
    Divise deux nombres avec validation et gestion d'erreurs.

    Args:
        dividende: Le nombre à diviser
        diviseur: Le nombre par lequel diviser
        ctx: Le contexte MCP pour le logging

    Returns:
        Le résultat de la division

    Raises:
        ValueError: Si les paramètres sont invalides ou si division par zéro
    """
    # TODO: Implémente :
    # 1. Validation des paramètres (None, etc.)
    # 2. Validation division par zéro
    # 3. Logging avec ctx.info() au début
    # 4. Calcul de la division
    # 5. Vérification si résultat infini (ctx.warning())
    # 6. Logging du succès
    # 7. Retourner le résultat
    pass


def main():
    print("Mon serveur MCP avec gestion d'erreurs démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()