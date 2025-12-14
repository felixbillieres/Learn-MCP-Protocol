# Instructions - Project 32 (Pentest Automation)

## Your Mission

Create a complete pentest automation framework orchestrating all phases.

## Steps to Follow

1. **Create Pydantic Models**:
   - `PentestPhase`:
     - `name` : str (enum: "recon", "weaponization", "delivery", "exploitation", "installation", "c2", "objectives")
     - `status` : str (enum: "pending", "in_progress", "completed", "failed")
     - `started_at` : str | None
     - `completed_at` : str | None
   - `Finding`:
     - `id` : int
     - `phase` : str
     - `severity` : str (enum: "low", "medium", "high", "critical")
     - `description` : str
     - `evidence` : str | None
   - `Pentest`:
     - `id` : int
     - `target` : str
     - `phases` : List[PentestPhase]
     - `findings` : List[Finding]
     - `status` : str
     - `created_at` : str
   - `Report`:
     - `pentest_id` : int
     - `executive_summary` : str
     - `findings` : List[Finding]
     - `recommendations` : List[str]

2. **Create Tools for Each Phase**:
   - `create_pentest` : Create new pentest
   - `execute_reconnaissance` : Phase 1 - Recon
   - `prepare_exploits` : Phase 2 - Weaponization
   - `deploy_payloads` : Phase 3 - Delivery
   - `execute_exploits` : Phase 4 - Exploitation
   - `establish_persistence` : Phase 5 - Installation
   - `configure_c2` : Phase 6 - C2
   - `achieve_objectives` : Phase 7 - Objectives
   - `generate_report` : Generate final report

3. **Create Resources**:
   - `pentest://list` : List all pentests
   - `pentest://{pentest_id}` : Get pentest status
   - `pentest://{pentest_id}/findings` : Get findings

4. **Create Prompts**:
   - `workflow_pentest` : Guide through all phases
   - `executive_report` : Generate executive summary

5. **Use Elicitation**:
   - Confirm before executing exploits
   - Ask for target information
   - Confirm sensitive operations

6. **Use Sampling**:
   - Generate custom reconnaissance techniques
   - Suggest exploitation methods
   - Generate report sections

## Hints

- Store pentests: `pentests: List[Pentest] = []`
- Track phase progression
- Use elicitation for confirmations
- Use sampling for creative generation

## Test

Use `python test.py` to verify pentest automation workflow.

