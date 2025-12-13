# Instructions - Projet 19

## Ta mission

Créer un workflow agentique avec sampling et outils.

## Étapes à suivre

1. **Crée un serveur FastMCP** avec des outils de base

2. **Crée des outils simples** :
   - `calculer` : Prend `expression` (str), évalue et retourne le résultat
   - `rechercher_info` : Prend `terme` (str), retourne des infos (simulé)
   - `convertir_unite` : Prend `valeur`, `unite_source`, `unite_cible`, convertit

3. **Crée un outil `agent_resolveur`** :
   - Prend `question` (str) et `ctx: Context`
   - Utilise sampling avec les outils définis
   - Permet au LLM d'utiliser les outils pour résoudre la question
   - Retourne la réponse finale

4. **Définis les outils pour le LLM** :
   - Crée des définitions d'outils au format MCP
   - Inclus-les dans la requête de sampling avec `tools`

## Indices

- Pour sampling avec outils, utilise `tools` dans create_message
- Chaque outil a `name`, `description`, `inputSchema` (JSON Schema)
- Le LLM décidera quand utiliser quels outils
- Le client gère l'exécution des outils automatiquement

## Test

Le test vérifiera que les outils sont bien définis.

