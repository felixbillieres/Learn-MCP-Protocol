# Projet 16 : Elicitation URL mode

## Objectif

Apprendre à utiliser le mode URL de l'elicitation pour les interactions sensibles qui ne doivent pas passer par le client MCP.

## Concepts à apprendre

### Mode URL vs Mode Form

- **Form mode** : Collecte de données via le client MCP (pour données non sensibles)
- **URL mode** : Redirection vers une URL externe (pour données sensibles comme credentials)

### Quand utiliser URL mode ?

Le mode URL est **obligatoire** pour :
- Credentials (mots de passe, tokens API)
- Informations de paiement
- Données personnelles sensibles
- Authentification OAuth

### Sécurité

Le mode URL garantit que les données sensibles ne passent jamais par le client MCP, mais sont collectées directement sur le serveur d'autorisation.

## Ce que tu vas créer

Dans ce projet, tu vas créer un outil qui utilise l'elicitation URL mode pour l'authentification.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

