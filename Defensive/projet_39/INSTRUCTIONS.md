# Instructions - Project 39 (Secrets Manager)

## Your Mission

Create a secrets manager with strict authorization and access control.

## Steps to Follow

1. **Create Pydantic Models**:
   - `Secret`:
     - `id` : str
     - `name` : str
     - `type` : str (enum: "password", "token", "key", "certificate")
     - `encrypted_value` : str (simulated encryption)
     - `tags` : List[str]
     - `created_at` : str
     - `updated_at` : str
   - `AccessLog`:
     - `id` : int
     - `secret_id` : str
     - `user` : str
     - `action` : str (enum: "read", "write", "delete")
     - `timestamp` : str
   - `SecretPolicy`:
     - `secret_id` : str
     - `allowed_users` : List[str]
     - `required_scopes` : List[str]
     - `rotation_interval` : int | None (days)

2. **Create Server with Authorization**:
   ```python
   capabilities={"authorization": {}}
   ```

3. **Create Tools** (all require authorization):
   - `create_secret` : Create new secret (requires secrets:write)
   - `get_secret` : Get secret (requires secrets:read, uses elicitation)
   - `modifier_secret` : Update secret (requires secrets:write)
   - `supprimer_secret` : Delete secret (requires secrets:delete)
   - `list_secrets` : List secrets (masked, requires secrets:read)
   - `consulter_logs` : View access logs (requires secrets:audit)

4. **Create Resources**:
   - `secret://list` : List secrets (masked)
   - `secret://{secret_id}` : Get secret (requires authorization)

5. **Add Authorization**:
   - Validate tokens for all operations
   - Check scopes: `["secrets:read", "secrets:write", "secrets:delete", "secrets:audit"]`
   - Use elicitation to confirm access

6. **Implement Masking**:
   - Mask secrets in listings (show only first/last chars)
   - Full value only with proper authorization

## Hints

- Store secrets: `secrets: Dict[str, Secret] = {}`
- Store logs: `access_logs: List[AccessLog] = []`
- Store policies: `policies: Dict[str, SecretPolicy] = {}`
- Simulate encryption (don't use real encryption for simplicity)

## Test

Use `python test.py` to verify secrets management and authorization.

