# Projet 17 : Utiliser le sampling pour demander des complétions LLM

## Objectif

Apprendre à utiliser le sampling pour demander des complétions de modèles de langage via le client MCP.

## Concepts à apprendre

### Qu'est-ce que le sampling ?

Le **sampling** permet aux serveurs MCP de demander des complétions LLM au client. Cela permet aux serveurs d'utiliser l'IA sans avoir besoin de leurs propres clés API.

### Avantages

- Pas besoin de clé API dans le serveur
- Le client contrôle quel modèle utiliser
- L'utilisateur peut voir et modifier les prompts avant envoi
- Sécurité : contrôle côté client

### Flow de sampling

1. Serveur envoie `sampling/createMessage` avec messages et paramètres
2. Client présente la requête à l'utilisateur (qui peut modifier)
3. Client envoie au LLM
4. Client présente la réponse (qui peut être modifiée)
5. Client retourne la réponse au serveur

### Utilisation dans FastMCP

Dans FastMCP, tu utilises le Context pour demander un sampling :
```python
response = await ctx.sampling.create_message(
    messages=[...],
    max_tokens=100
)
```

## Ce que tu vas créer

Dans ce projet, tu vas créer un outil qui utilise le sampling pour obtenir une réponse d'un LLM.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

