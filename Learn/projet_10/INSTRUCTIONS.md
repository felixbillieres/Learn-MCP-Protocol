# Instructions - Projet 10

## Ta mission

Implémenter les subscriptions pour les resources avec notifications de changements.

## Étapes à suivre

1. **Crée un serveur FastMCP** avec capabilities pour subscriptions :
   ```python
   capabilities={"resources": {"subscribe": True}}
   ```

2. **Gère les subscriptions** :
   - Stocke les subscriptions dans un dict : `subscriptions = {}` (URI -> set de callbacks)
   - Implémente `@mcp_server.subscribe_resource()` pour gérer `resources/subscribe`
   - Implémente `@mcp_server.unsubscribe_resource()` pour gérer `resources/unsubscribe`

3. **Crée une resource modifiable** :
   - Resource `status://app/current` qui peut être mise à jour
   - Outil `update_status` pour modifier cette resource

4. **Envoie des notifications** :
   - Quand la resource change, utilise `ctx.send_notification()` pour notifier les abonnés
   - Format : `notifications/resources/updated` avec `uri` et `contents`

## Indices

- FastMCP gère automatiquement les subscriptions si tu déclares la capability
- Pour notifier, tu peux utiliser le Context ou directement le serveur
- Note : FastMCP peut simplifier cela, mais tu dois comprendre le concept

## Test

Utilise `python test.py` pour vérifier que les subscriptions fonctionnent.

## Note

FastMCP peut avoir des limitations pour les notifications. L'objectif principal est de comprendre le concept de subscriptions.