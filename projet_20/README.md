# Projet 20 : Introduction à l'autorisation OAuth 2.1

## Objectif

Comprendre les concepts de base de l'autorisation OAuth 2.1 dans MCP.

## Concepts à apprendre

### Pourquoi l'autorisation ?

L'autorisation sécurise l'accès aux ressources et opérations sensibles. Elle permet de :
- Protéger les données utilisateur
- Contrôler qui peut faire quoi
- Auditer les actions
- Implémenter des quotas par utilisateur

### OAuth 2.1 dans MCP

MCP utilise OAuth 2.1 pour l'autorisation :
- Le client obtient un token d'accès
- Le token est inclus dans chaque requête HTTP
- Le serveur valide le token avant de traiter la requête

### Flow d'autorisation

1. Client demande autorisation au serveur d'autorisation
2. Utilisateur s'authentifie
3. Serveur d'autorisation retourne un token
4. Client utilise le token pour les requêtes
5. Serveur MCP valide le token

### Important

Pour ce projet, on va **simuler** l'autorisation car implémenter OAuth complet est complexe. L'objectif est de comprendre les concepts.

## Ce que tu vas créer

Dans ce projet, tu vas créer un serveur qui simule la validation de tokens.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

