# Instructions - Project 33 (SIEM MCP)

## Your Mission

Create a SIEM system with real-time event collection and alerting.

## Steps to Follow

1. **Create Pydantic Models**:
   - `SecurityEvent`:
     - `id` : int
     - `timestamp` : str
     - `source` : str (IP or hostname)
     - `event_type` : str (enum: "login", "file_access", "network", "process")
     - `severity` : str (enum: "low", "medium", "high", "critical")
     - `details` : Dict[str, Any]
   - `Alert`:
     - `id` : int
     - `rule_id` : str
     - `events` : List[SecurityEvent]
     - `severity` : str
     - `message` : str
     - `created_at` : str
   - `Rule`:
     - `id` : str
     - `name` : str
     - `pattern` : str (description of what to detect)
     - `severity` : str
     - `enabled` : bool

2. **Create Server with Subscriptions**:
   ```python
   capabilities={"resources": {"subscribe": True}}
   ```

3. **Create Tools**:
   - `collect_event` : Collect a security event
   - `analyze_events` : Analyze events for patterns
   - `create_rule` : Create a detection rule
   - `list_alerts` : List active alerts

4. **Create Resources**:
   - `event://recent` : Recent security events
   - `alert://active` : Active alerts

5. **Implement Subscriptions**:
   - Subscribe to new events
   - Subscribe to alerts
   - Notify when rules trigger

6. **Create Prompts**:
   - `generate_detection_rule` : Generate detection rules using sampling

## Hints

- Store events: `events: List[SecurityEvent] = []`
- Store alerts: `alerts: List[Alert] = []`
- Store rules: `rules: Dict[str, Rule] = {}`
- Use subscriptions for real-time notifications

## Test

Use `python test.py` to verify event collection and alerting.

