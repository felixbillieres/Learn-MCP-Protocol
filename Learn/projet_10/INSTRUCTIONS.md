# Instructions - Project 10

## Your mission

Implement subscriptions for resources with change notifications.

## Steps to follow

1. **Create a FastMCP server** with capabilities for subscriptions:
   ```python
   capabilities={"resources": {"subscribe": True}}
   ```

2. **Handle subscriptions**:
   - Store subscriptions in a dict: `subscriptions = {}` (URI -> set of callbacks)
   - Implement `@mcp_server.subscribe_resource()` to handle `resources/subscribe`
   - Implement `@mcp_server.unsubscribe_resource()` to handle `resources/unsubscribe`

3. **Create a modifiable resource**:
   - Resource `status://app/current` that can be updated
   - Tool `update_status` to modify this resource

4. **Send notifications**:
   - When the resource changes, use `ctx.send_notification()` to notify subscribers
   - Format: `notifications/resources/updated` with `uri` and `contents`

## Hints

- FastMCP automatically handles subscriptions if you declare the capability
- To notify, you can use Context or the server directly
- Note: FastMCP may simplify this, but you must understand the concept

## Test

Use `python test.py` to verify that subscriptions work.

## Note

FastMCP may have limitations for notifications. The main objective is to understand the concept of subscriptions.
