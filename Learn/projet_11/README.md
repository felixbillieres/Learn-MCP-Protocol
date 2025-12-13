# Projet 11 : Créer ton premier prompt

## Objectif

Apprendre à créer des prompts (templates de messages) avec MCP. Les prompts permettent d'exposer des templates réutilisables que les clients peuvent utiliser.

## Concepts à apprendre

### Qu'est-ce qu'un prompt ?

Un **prompt** est un template de message prédéfini que le serveur MCP expose aux clients. Les prompts sont conçus pour être **contrôlés par l'utilisateur** - ils sont exposés pour que l'utilisateur puisse les sélectionner explicitement.

### Différence avec les outils

- **Tools** : Actions que l'IA peut exécuter (modèle contrôle)
- **Prompts** : Templates que l'utilisateur peut choisir d'utiliser (utilisateur contrôle)
- **Resources** : Données que l'IA peut lire (application contrôle)

### Structure d'un prompt

Un prompt a :
- `name` : Identifiant unique
- `title` : Nom lisible (optionnel)
- `description` : Description (optionnel)
- `arguments` : Arguments dynamiques (optionnel)

### Message retourné

Quand un client demande un prompt, le serveur retourne des messages formatés (comme des messages pour un LLM).

## Documentation MCP

Les prompts sont déclarés avec la capability `prompts` :
```json
{
  "capabilities": {
    "prompts": {}
  }
}
```

## Ce que tu vas créer

Dans ce projet, tu vas créer un serveur qui expose des prompts simples pour différentes tâches.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

