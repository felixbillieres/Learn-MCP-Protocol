# Instructions - Project 29 (Pentest Session Manager)

## Your Mission

Create a session manager for pentesting with subscriptions and notifications.

## Steps to Follow

1. **Create Pydantic Models**:
   - `Session`:
     - `id` : int
     - `type` : str (enum: "ssh", "winrm", "psexec", "webshell")
     - `target` : str (IP or hostname)
     - `username` : str
     - `established_at` : str (timestamp)
     - `status` : str (enum: "active", "closed")
     - `metadata` : Dict[str, Any] (optional)
   - `Credential`:
     - `username` : str
     - `password` : str | None
     - `domain` : str | None (for Windows)

2. **Create Server with Subscriptions**:
   ```python
   capabilities={"resources": {"subscribe": True}}
   ```

3. **Create Tools**:
   - `create_session` : Create a new session
   - `list_sessions` : List all active sessions
   - `close_session` : Close a session
   - `get_session` : Get session details

4. **Create Resources**:
   - `session://list` : List all sessions
   - `session://{session_id}` : Get specific session

5. **Implement Subscriptions**:
   - Store subscriptions: `subscriptions = {}`
   - When a new session is created, notify subscribers
   - Use `ctx.send_notification()` to send notifications

6. **Add Authorization**:
   - Protect session access with token validation
   - Only authorized users can view sessions

## Hints

- Use a global list: `sessions: List[Session] = []`
- Store subscriptions as: `subscriptions: Dict[str, set] = {}`
- Notify format: `notifications/resources/updated`

## Test

Use `python test.py` to verify session management and notifications.

