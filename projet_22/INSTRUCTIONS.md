# Instructions - Projet 22

## Ta mission

Créer un serveur avec sécurité avancée.

## Étapes

1. **Validation stricte d'audience** : Rejette les tokens avec mauvaise audience

2. **Rate limiting** : Limite les requêtes par utilisateur (ex: 100 req/min)

3. **Logging** : Log toutes les tentatives d'accès (succès et échecs)

4. **Protection token reuse** : Détecte si un token est utilisé depuis plusieurs IPs

