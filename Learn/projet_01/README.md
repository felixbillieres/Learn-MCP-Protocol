# Projet 01 : Créer un serveur MCP basique

## Objectif

Créer ton premier serveur MCP avec FastMCP. C'est la base de tout projet MCP !

## Concepts à apprendre

### Qu'est-ce que MCP ?

MCP (Model Context Protocol) est un protocole qui permet à des applications (comme Claude Desktop) de communiquer avec des serveurs qui exposent des **outils** (tools), des **ressources** (resources) et des **prompts** (prompts).

### FastMCP

FastMCP est une bibliothèque Python qui simplifie la création de serveurs MCP. C'est ce que utilise ton projet Exegol-MCP !

### Structure de base

Un serveur MCP a besoin de :
1. Une instance `FastMCP` qui représente le serveur
2. Une configuration (nom, host, port)
3. Un point d'entrée pour démarrer le serveur

## Exemple dans Exegol-MCP

Regarde `src/mcp_app.py` dans ton projet Exegol-MCP :

```1:11:Exegol-MCP/src/mcp_app.py
from mcp.server.fastmcp import FastMCP

mcp_host = "127.0.0.1"
mcp_port = 8000
mcp_server = FastMCP(
    "Exegol",
    host=mcp_host,
    port=mcp_port,
    stateless_http=True,
    json_response=True
)
```

Et dans `src/main.py` :

```21:21:Exegol-MCP/src/main.py
    mcp_server.run(transport="streamable-http")
```

## Ce que tu vas créer

Dans ce projet, tu vas créer un serveur MCP simple qui :
- S'appelle "MonPremierServeur"
- Écoute sur `127.0.0.1:8000`
- Peut être démarré et affiche un message

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !