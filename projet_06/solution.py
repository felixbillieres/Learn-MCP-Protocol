from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel, Field

# TODO: Importe List et Dict depuis typing

# Crée le serveur MCP
mcp_server = FastMCP(
    "MonPremierServeur",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Liste globale pour stocker les utilisateurs
# utilisateurs = []

# TODO: Crée le modèle Utilisateur avec :
# - id (int)
# - nom (str)
# - email (str | None, optionnel)
# - tags (List[str])
# - score (float, défaut 0.0)
class Utilisateur(BaseModel):
    pass

# TODO: Crée le modèle StatistiquesUtilisateurs avec :
# - total (int)
# - par_tag (Dict[str, int])
# - score_moyen (float)
class StatistiquesUtilisateurs(BaseModel):
    pass

# TODO: Crée l'outil ajouter_utilisateur
@mcp_server.tool()
async def ajouter_utilisateur(
    utilisateur: Utilisateur,
    ctx: Context
) -> Utilisateur:
    """
    Ajoute un utilisateur à la liste.

    Args:
        utilisateur: L'utilisateur à ajouter
        ctx: Le contexte MCP

    Returns:
        L'utilisateur ajouté avec son ID assigné
    """
    pass

# TODO: Crée l'outil lister_utilisateurs
@mcp_server.tool()
async def lister_utilisateurs(
    tag_filtre: str | None = None,
    ctx: Context  # Note: Context est injecté automatiquement par FastMCP
) -> list:  # TODO: Utilise List[Utilisateur] avec l'import
    """
    Liste les utilisateurs, optionnellement filtrés par tag.

    Args:
        tag_filtre: Tag pour filtrer (optionnel)
        ctx: Le contexte MCP

    Returns:
        Liste des utilisateurs correspondants
    """
    pass

# TODO: Crée l'outil obtenir_statistiques
@mcp_server.tool()
async def obtenir_statistiques(
    ctx: Context
) -> StatistiquesUtilisateurs:
    """
    Obtient des statistiques sur les utilisateurs.

    Args:
        ctx: Le contexte MCP

    Returns:
        Statistiques des utilisateurs
    """
    pass


def main():
    print("Mon serveur MCP avec types complexes démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()