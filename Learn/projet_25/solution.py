# PROJET FINAL - Gestionnaire de Projet MCP Complet
# 
# TODO: Crée un serveur MCP professionnel avec TOUTES les fonctionnalités
# - Tools pour CRUD projets/tâches
# - Resources pour exposer données
# - Prompts pour workflows
# - Elicitation pour interactions
# - Authorization pour sécurité
# - Code bien structuré

from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from typing import Any, Optional, List, Dict

# TODO: Imports nécessaires
# TODO: Crée le serveur avec toutes les capabilities
mcp_server = FastMCP(
    "GestionnaireProjet",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Ajoute toutes les capabilities nécessaires
)

# TODO: Modèles Pydantic pour Projet et Tache
# TODO: Stockage (dicts ou similaire)
# TODO: Tools CRUD
# TODO: Resources
# TODO: Prompts
# TODO: Authorization
# TODO: Fonction main

def main():
    print("Gestionnaire de Projet MCP démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    main()

