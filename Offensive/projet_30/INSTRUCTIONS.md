# Instructions - Project 30 (Exploitation Framework)

## Your Mission

Create an exploitation framework that chains exploits together with intelligent payload generation.

## Steps to Follow

1. **Create Pydantic Models**:
   - `TargetInfo`:
     - `ip` : str
     - `os` : str
     - `services` : List[Dict[str, str]] (port, service, version)
     - `vulnerabilities` : List[str] (CVE IDs)
   - `Exploit`:
     - `id` : str
     - `name` : str
     - `cve` : str | None
     - `target_os` : str
     - `payload_template` : str
   - `ExploitChain`:
     - `id` : int
     - `target` : TargetInfo
     - `exploits` : List[Exploit]
     - `status` : str (enum: "pending", "in_progress", "completed", "failed")
     - `results` : List[Dict[str, Any]]
   - `ExploitResult`:
     - `exploit_id` : str
     - `success` : bool
     - `output` : str
     - `session_created` : bool

2. **Create Tools**:
   - `analyze_target` : Analyze target and collect information (uses elicitation)
   - `create_chain` : Create an exploit chain for a target
   - `execute_chain` : Execute the exploit chain
   - `generate_payload` : Use sampling to generate custom payload

3. **Create Elicitation**:
   - `analyze_target` should use elicitation to ask for:
     - Target IP/hostname
     - OS information
     - Known vulnerabilities
     - Services detected

4. **Create Sampling Tool**:
   - `generate_payload` uses sampling with:
     - `temperature`: 0.7 (creative but controlled)
     - Generates payload based on target info and exploit

5. **Create Resources**:
   - `exploit://list` : List available exploits
   - `chain://{chain_id}` : Get exploit chain status

6. **Create Prompts**:
   - `workflow_exploitation` : Guides through exploitation steps

## Hints

- Store chains: `chains: List[ExploitChain] = []`
- Store exploits: `exploits: List[Exploit] = []`
- Use elicitation schema for target info collection
- Use sampling to generate payloads dynamically

## Test

Use `python test.py` to verify exploit chaining and payload generation.

