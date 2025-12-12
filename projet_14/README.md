# Projet 14 : Utiliser l'elicitation

## Objectif

Apprendre à utiliser l'elicitation pour demander des informations aux utilisateurs pendant l'exécution d'un outil.

## Concepts à apprendre

### Qu'est-ce que l'elicitation ?

L'**elicitation** permet aux serveurs MCP de demander des informations supplémentaires aux utilisateurs pendant l'exécution d'un outil. C'est un mécanisme qui permet des workflows interactifs.

### Flow d'elicitation

1. Le serveur envoie une requête d'elicitation au client
2. Le client présente la demande à l'utilisateur
3. L'utilisateur répond (ou annule)
4. Le client retourne la réponse au serveur
5. Le serveur continue avec l'information obtenue

### Modes d'elicitation

- **Form mode** : Collecte de données structurées via le client MCP (pour données non sensibles)
- **URL mode** : Redirection vers une URL externe (pour données sensibles comme credentials)

### Utilisation dans FastMCP

Dans FastMCP, tu utilises le Context pour demander une elicitation :
```python
response = await ctx.elicitation.create(
    message="Quelle est votre préférence ?",
    requested_schema={...}
)
```

## Ce que tu vas créer

Dans ce projet, tu vas créer un outil qui demande des informations à l'utilisateur via l'elicitation.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

