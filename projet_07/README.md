# Projet 07 : Projet final - Mini serveur MCP complet

## Objectif

Créer un mini serveur MCP complet qui combine tous les concepts appris ! Ce projet sera inspiré de la structure d'Exegol-MCP mais simplifié.

## Ce que tu vas créer

Un serveur MCP pour gérer une liste de tâches (todo list) avec :
- Des modèles Pydantic pour les tâches
- Des outils pour CRUD (Create, Read, Update, Delete)
- Une gestion d'erreurs complète
- Du logging avec Context
- Des filtres et des statistiques

## Concepts récapitulatifs

Tu vas utiliser :
-  FastMCP pour créer le serveur
-  Des outils avec `@mcp_server.tool()`
-  Des modèles Pydantic pour structurer les données
-  Le Context pour le logging
-  La gestion d'erreurs avec validation
-  Des types complexes (listes, optionnels)

## Inspiration : Exegol-MCP

Regarde comment Exegol-MCP est structuré :
- `src/mcp_app.py` : Configuration du serveur
- `src/models/container.py` : Modèles de données
- `src/assets/tools_*.py` : Outils organisés par catégorie
- `src/main.py` : Point d'entrée

## Structure attendue

Ton projet final devrait avoir :
```
projet_07/
├── solution.py        # Tout ton code (pour simplifier)
├── README.md
├── INSTRUCTIONS.md
└── test.py
```

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois créer exactement !