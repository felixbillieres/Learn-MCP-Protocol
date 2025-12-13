# Instructions - Project 31 (C2 Manager)

## Your Mission

Create a C2 server manager with strict authorization and real-time notifications.

## Steps to Follow

1. **Create Pydantic Models**:
   - `Beacon`:
     - `id` : str (unique identifier)
     - `hostname` : str
     - `ip` : str
     - `os` : str
     - `last_checkin` : str (timestamp)
     - `status` : str (enum: "active", "lost", "sleeping")
     - `tasks` : List[Task]
   - `Task`:
     - `id` : int
     - `beacon_id` : str
     - `command` : str
     - `status` : str (enum: "pending", "executing", "completed", "failed")
     - `output` : str | None
     - `created_at` : str
   - `Command`:
     - `type` : str (enum: "shell", "download", "upload", "screenshot")
     - `args` : Dict[str, Any]

2. **Create Server with Authorization**:
   ```python
   capabilities={"authorization": {}}
   ```

3. **Create Tools** (all require authorization):
   - `lister_beacons` : List all beacons
   - `creer_task` : Create a task for a beacon
   - `obtenir_tasks` : Get tasks for a beacon
   - `obtenir_response` : Get task output

4. **Create Resources**:
   - `beacon://list` : List all beacons
   - `beacon://{beacon_id}` : Get beacon details

5. **Implement Subscriptions**:
   - Subscribe to beacon check-ins
   - Notify when new beacons appear
   - Notify when tasks complete

6. **Add Authorization**:
   - Validate tokens for all operations
   - Use scopes: `["beacons:read", "beacons:write", "tasks:execute"]`
   - Protect sensitive operations

7. **Create Prompts**:
   - `generer_commande` : Generate command templates

## Hints

- Store beacons: `beacons: Dict[str, Beacon] = {}`
- Store tasks: `tasks: List[Task] = []`
- Validate tokens before operations
- Use subscriptions for real-time updates

## Test

Use `python test.py` to verify C2 management and authorization.

