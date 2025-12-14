# Instructions - Project 34 (Incident Manager)

## Your Mission

Create an incident management system with triage workflows.

## Steps to Follow

1. **Create Pydantic Models**:
   - `IOC` (Indicator of Compromise):
     - `type` : str (enum: "ip", "domain", "hash", "url")
     - `value` : str
     - `source` : str
   - `Incident`:
     - `id` : int
     - `title` : str
     - `severity` : str (enum: "low", "medium", "high", "critical")
     - `status` : str (enum: "new", "triaged", "investigating", "contained", "resolved")
     - `iocs` : List[IOC]
     - `description` : str
     - `created_at` : str
     - `updated_at` : str
   - `ResponseAction`:
     - `id` : int
     - `incident_id` : int
     - `action` : str
     - `status` : str (enum: "pending", "in_progress", "completed")
     - `executed_at` : str | None

2. **Create Tools**:
   - `create_incident` : Create new incident (uses elicitation)
   - `trier_incident` : Triage an incident (uses prompts)
   - `ajouter_ioc` : Add IOC to incident
   - `create_action` : Create response action
   - `executer_action` : Execute response action
   - `resoudre_incident` : Mark incident as resolved

3. **Create Resources**:
   - `incident://list` : List all incidents
   - `incident://{incident_id}` : Get incident details

4. **Create Prompts**:
   - `workflow_triage` : Guide through triage process
   - `generate_incident_report` : Generate incident report

5. **Use Elicitation**:
   - Collect incident details when creating
   - Confirm severity assessment
   - Confirm response actions

6. **Use Sampling**:
   - Suggest response actions based on incident type
   - Generate containment strategies

## Hints

- Store incidents: `incidents: List[Incident] = []`
- Store actions: `actions: List[ResponseAction] = []`
- Use elicitation for data collection
- Use sampling for intelligent suggestions

## Test

Use `python test.py` to verify incident management.

