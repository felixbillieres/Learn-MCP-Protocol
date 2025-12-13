# Projet 10 : Resources avec subscriptions

## Objectif

Apprendre à implémenter les subscriptions pour les resources, permettant aux clients d'être notifiés quand une resource change.

## Concepts à apprendre

### Qu'est-ce qu'une subscription ?

Une **subscription** permet à un client de s'abonner aux changements d'une resource. Quand la resource est modifiée, le serveur envoie une notification au client.

### Flow de subscription

1. Client envoie `resources/subscribe` avec une URI
2. Serveur accepte la subscription
3. Quand la resource change, serveur envoie `notifications/resources/updated`
4. Client peut envoyer `resources/unsubscribe` pour se désabonner

### Capacités requises

Pour supporter les subscriptions, le serveur doit déclarer :
```json
{
  "capabilities": {
    "resources": {
      "subscribe": true
    }
  }
}
```

## Ce que tu vas créer

Dans ce projet, tu vas créer un serveur avec des resources qui peuvent être modifiées et qui notifient les clients abonnés.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !