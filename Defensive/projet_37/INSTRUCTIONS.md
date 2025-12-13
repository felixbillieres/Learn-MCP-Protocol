# Instructions - Project 37 (Firewall Rules Manager)

## Your Mission

Create a firewall rules manager with validation and authorization.

## Steps to Follow

1. **Create Pydantic Models**:
   - `FirewallRule`:
     - `id` : int
     - `name` : str
     - `action` : str (enum: "allow", "deny")
     - `source_ip` : str | None
     - `dest_ip` : str | None
     - `source_port` : int | None
     - `dest_port` : int | None
     - `protocol` : str (enum: "tcp", "udp", "icmp", "any")
     - `enabled` : bool
     - `priority` : int
   - `NetworkPolicy`:
     - `id` : str
     - `name` : str
     - `rules` : List[int] (rule IDs)
     - `applied_to` : List[str] (systems)
   - `TrafficLog`:
     - `timestamp` : str
     - `source_ip` : str
     - `dest_ip` : str
     - `port` : int
     - `protocol` : str
     - `action` : str (allowed/denied)
     - `rule_id` : int | None

2. **Create Tools**:
   - `creer_regle` : Create firewall rule (validate IPs and ports)
   - `lister_regles` : List all rules
   - `modifier_regle` : Modify a rule (requires authorization)
   - `supprimer_regle` : Delete a rule (requires authorization)
   - `creer_policy` : Create network policy
   - `appliquer_policy` : Apply policy to systems

3. **Create Resources**:
   - `firewall://rules` : List all rules
   - `firewall://policy/{policy_id}` : Get policy

4. **Add Authorization**:
   - Protect rule modifications
   - Validate tokens
   - Use scopes: `["firewall:read", "firewall:write"]`

5. **Add Validation**:
   - Validate IP addresses (IPv4/IPv6)
   - Validate port ranges (1-65535)
   - Validate protocol names

## Hints

- Store rules: `rules: List[FirewallRule] = []`
- Store policies: `policies: Dict[str, NetworkPolicy] = {}`
- Use regex or ipaddress library for IP validation

## Test

Use `python test.py` to verify firewall rule management.

