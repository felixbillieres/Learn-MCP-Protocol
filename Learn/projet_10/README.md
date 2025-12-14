# Project 10: Resources with subscriptions

## Objective

Learn to implement subscriptions for resources, allowing clients to be notified when a resource changes.

## Concepts to learn

### What is a subscription?

A **subscription** allows a client to subscribe to changes in a resource. When the resource is modified, the server sends a notification to the client.

### Subscription flow

1. Client sends `resources/subscribe` with a URI
2. Server accepts the subscription
3. When the resource changes, server sends `notifications/resources/updated`
4. Client can send `resources/unsubscribe` to unsubscribe

### Required capabilities

To support subscriptions, the server must declare:
```json
{
  "capabilities": {
    "resources": {
      "subscribe": true
    }
  }
}
```

## What you will create

In this project, you will create a server with resources that can be modified and that notify subscribed clients.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
