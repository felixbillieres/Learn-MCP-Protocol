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
   - `creer_pentest` : Create new pentest
   - `executer_reconnaissance` : Phase 1 - Recon
   - `preparer_exploits` : Phase 2 - Weaponization
   - `deployer_payloads` : Phase 3 - Delivery
   - `executer_exploits` : Phase 4 - Exploitation
   - `etablir_persistence` : Phase 5 - Installation
   - `configurer_c2` : Phase 6 - C2
   - `atteindre_objectifs` : Phase 7 - Objectives
   - `generer_rapport` : Generate final report

3. **Create Resources**:
   - `pentest://list` : List all pentests
   - `pentest://{pentest_id}` : Get pentest status
   - `pentest://{pentest_id}/findings` : Get findings

4. **Create Prompts**:
   - `workflow_pentest` : Guide through all phases
   - `rapport_executif` : Generate executive summary

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

