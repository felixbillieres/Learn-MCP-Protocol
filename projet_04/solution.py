from mcp.server.fastmcp import FastMCP

# TODO: Importe Context depuis mcp.server.fastmcp

# Crée le serveur MCP
mcp_server = FastMCP(
    "MonPremierServeur",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Crée l'outil traiter_fichier
# Prend nom_fichier (str) et ctx (Context)
# Logge les étapes avec ctx.info(), ctx.warning(), ctx.error()
# Retourne un dict avec les informations du traitement
@mcp_server.tool()
async def traiter_fichier(
    nom_fichier: str,
    ctx  # TODO: Ajoute le type Context ici
) -> dict:
    """
    Traite un fichier et logge les étapes du traitement.

    Args:
        nom_fichier: Le nom du fichier à traiter
        ctx: Le contexte MCP pour le logging

    Returns:
        Un dictionnaire avec les informations du traitement

    Raises:
        ValueError: Si le fichier cause une erreur
    """
    # TODO: Implémente le traitement avec logging
    # 1. ctx.info() : début
    # 2. Vérifier si .txt -> ctx.info() ou ctx.warning()
    # 3. ctx.info() : lecture
    # 4. Si nom_fichier == "erreur.txt" -> ctx.error() puis raise ValueError
    # 5. ctx.info() : succès
    # 6. Retourner le dict
    pass


def main():
    print("Mon serveur MCP avec logging démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()