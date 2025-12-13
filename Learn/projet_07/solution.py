# PROJET FINAL - Gestionnaire de tâches MCP
# 
# TODO: Crée un serveur MCP complet pour gérer une liste de tâches
# Utilise TOUS les concepts appris dans les projets précédents !

# TODO: Imports nécessaires
# - FastMCP, Context depuis mcp.server.fastmcp
# - BaseModel, Field depuis pydantic
# - List, Dict, Optional depuis typing
# - datetime depuis datetime

# TODO: Crée le serveur MCP
# mcp_server = FastMCP(...)

# TODO: Liste globale pour stocker les tâches
# taches = []

# TODO: Modèle Tache
class Tache:
    pass

# TODO: Modèle StatistiquesTaches
class StatistiquesTaches:
    pass

# TODO: Fonction utilitaire pour trouver une tâche par ID
# def trouver_tache_par_id(tache_id: int) -> Tache | None:
#     ...

# TODO: Outil creer_tache
@mcp_server.tool()
async def creer_tache(...):
    pass

# TODO: Outil lister_taches
@mcp_server.tool()
async def lister_taches(...):
    pass

# TODO: Outil obtenir_tache
@mcp_server.tool()
async def obtenir_tache(...):
    pass

# TODO: Outil modifier_tache
@mcp_server.tool()
async def modifier_tache(...):
    pass

# TODO: Outil marquer_termine
@mcp_server.tool()
async def marquer_termine(...):
    pass

# TODO: Outil supprimer_tache
@mcp_server.tool()
async def supprimer_tache(...):
    pass

# TODO: Outil obtenir_statistiques
@mcp_server.tool()
async def obtenir_statistiques(...):
    pass


def main():
    print("Mon serveur MCP de gestion de tâches démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()