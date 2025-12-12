# Projet 08 : Créer ta première ressource

## Objectif

Apprendre à exposer des ressources (resources) avec MCP. Les ressources permettent d'exposer des données que les clients peuvent lire.

## Concepts à apprendre

### Qu'est-ce qu'une ressource ?

Une **ressource** est une source de données que le serveur MCP expose aux clients. Contrairement aux outils (qui sont exécutés), les ressources sont des données que le client peut lire pour obtenir du contexte.

**Différence clé** :
- **Tools** : Actions que l'IA peut **exécuter** (modifier, créer, supprimer)
- **Resources** : Données que l'IA peut **lire** pour comprendre le contexte

### Exemples de ressources

- Contenu de fichiers
- Schémas de base de données
- Configuration système
- Logs
- Données d'API

### Comment FastMCP gère les ressources

Dans FastMCP, tu utilises des décorateurs :
- `@mcp_server.list_resources()` : Liste les ressources disponibles
- `@mcp_server.read_resource()` : Lit le contenu d'une ressource

## Documentation MCP

Les ressources sont identifiées par des **URIs** uniques :
- Format : `[protocol]://[host]/[path]`
- Exemple : `file:///home/user/config.json`
- Exemple : `config://app/settings`

## Ce que tu vas créer

Dans ce projet, tu vas créer un serveur qui expose des ressources de configuration simples.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !