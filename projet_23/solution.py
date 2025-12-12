from mcp.server.fastmcp import FastMCP, Context
from typing import List
import os

mcp_server = FastMCP("MonServeurRoots", host="127.0.0.1", port=8000)

def get_authorized_roots(ctx: Context) -> List[str]:
    """Récupère les roots autorisés."""
    # TODO: Utilise ctx.roots.list() pour obtenir les roots
    # Note: FastMCP peut avoir des limitations, simule si nécessaire
    pass

def is_path_authorized(path: str, roots: List[str]) -> bool:
    """Vérifie qu'un chemin est dans un root autorisé."""
    # TODO: Vérifie que le chemin est sous un des roots
    pass

@mcp_server.tool()
async def lister_fichiers(ctx: Context) -> List[str]:
    """Liste les fichiers dans les roots autorisés."""
    # TODO: Obtient les roots, liste les fichiers
    pass

@mcp_server.tool()
async def lire_fichier(chemin: str, ctx: Context) -> str:
    """Lit un fichier s'il est autorisé."""
    # TODO: Vérifie que le chemin est autorisé, lit le fichier
    pass

def main():
    print("Serveur avec roots démarre !")
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    main()

