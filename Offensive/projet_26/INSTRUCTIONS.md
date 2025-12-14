# Instructions - Project 26 (Port Scanner)

## Your Mission

Create an MCP server to scan ports and analyze services with report generation.

## Steps to Follow

1. **Create Pydantic Models**:
   - `PortInfo`:
     - `port`: int (required)
     - `state`: str (required, values: "open", "closed", "filtered")
     - `service`: str | None (optional, e.g., "ssh", "http", "mysql")
     - `version`: str | None (optional, service version)
   - `ScanResult`:
     - `target`: str (required, IP or hostname)
     - `ports`: List[PortInfo] (required)
     - `timestamp`: str (required, ISO format)
     - `scan_type`: str (required, e.g., "quick", "full")

2. **Create FastMCP server** with capabilities for resources:
   ```python
   capabilities={"resources": {}}
   ```

3. **Create `scan_ports` tool**:
   - Parameters: `target` (str), `ports` (List[int] | None, optional), `scan_type` (str, default "quick"), `ctx: Context`
   - Simulates port scanning (generates random or predefined results)
   - Stores the result in a global list `scans = []`
   - Returns: `ScanResult`
   - Logs with `ctx.info()`

4. **Create `analyze_services` tool**:
   - Parameters: `scan_id` (int, index in the list), `ctx: Context`
   - Analyzes services detected in a scan
   - Identifies versions and potential vulnerabilities
   - Returns: `Dict[str, Any]` with analyses
   - Logs with `ctx.info()`

5. **Create resource `scan://results/{scan_id}`**:
   - Exposes scan results via resources
   - Uses a URI template to access scans by ID
   - Returns the `ScanResult` in JSON format

6. **Create prompt `generate_vulnerability_report`**:
   - Takes a `scan_id` argument (int)
   - Generates a vulnerability report based on scan results
   - Returns a formatted report template

## Hints

- To simulate scanning, use common ports: `[22, 80, 443, 3306, 5432, 8080]`
- Generate random services: `["ssh", "http", "https", "mysql", "postgresql"]`
- For timestamp: `from datetime import datetime` then `datetime.now().isoformat()`
- Store scans in a global list: `scans: List[ScanResult] = []`

## Test

Use `python test.py` to verify that:
- Scanning works
- Resources expose results
- Prompts generate reports

## Expected Result

- Scan ports on a target
- Analyze detected services
- Expose results via resources
- Generate vulnerability reports
