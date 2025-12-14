# Project 26: Port Scanner MCP

## Objective

Create an MCP server to scan ports and analyze services, with vulnerability report generation.

## Concepts to Learn

### Port scanning in cybersecurity

A port scanner is a fundamental tool in offensive security that allows you to:
- Discover open ports on a target
- Identify services listening on these ports
- Detect service versions
- Analyze potential vulnerabilities

### MCP architecture for scanning

In this project, you will use:
- **Tools**: To execute scans and analyses
- **Resources**: To expose scan results in real-time
- **Prompts**: To generate vulnerability reports
- **Pydantic models**: To structure scan data

### Data models

```python
class PortInfo(BaseModel):
    port: int
    state: str  # "open", "closed", "filtered"
    service: str | None
    version: str | None

class ScanResult(BaseModel):
    target: str
    ports: List[PortInfo]
    timestamp: str
    scan_type: str
```

## Use Cases

- **Reconnaissance**: Identify exposed services
- **Attack surface analysis**: Understand which ports are accessible
- **Vulnerability detection**: Analyze service versions
- **Security reporting**: Generate reports for clients

## Next Steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
