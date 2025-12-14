# Instructions - Project 36 (Patch Manager)

## Your Mission

Create a patch management system with deployment planning.

## Steps to Follow

1. **Create Pydantic Models**:
   - `Vulnerability`:
     - `cve_id` : str
     - `severity` : str
     - `affected_products` : List[str]
   - `Patch`:
     - `id` : str
     - `name` : str
     - `version` : str
     - `vulnerabilities` : List[str] (CVE IDs)
     - `release_date` : str
     - `affected_systems` : List[str]
   - `DeploymentPlan`:
     - `id` : int
     - `patch_id` : str
     - `systems` : List[str]
     - `scheduled_date` : str
     - `status` : str (enum: "planned", "testing", "deploying", "completed", "rolled_back")
     - `test_results` : Dict[str, Any] | None

2. **Create Tools**:
   - `list_patches` : List available patches
   - `create_deployment_plan` : Create deployment plan (uses prompts)
   - `deployer_patch` : Deploy a patch (uses elicitation for confirmation)
   - `verifier_patch` : Test a patch before deployment

3. **Create Resources**:
   - `patch://list` : List all patches
   - `patch://{patch_id}` : Get patch details
   - `deployment://{plan_id}` : Get deployment plan

4. **Create Prompts**:
   - `generate_deployment_plan` : Generate deployment plan

5. **Use Elicitation**:
   - Confirm before deploying patches
   - Ask for deployment schedule

## Hints

- Store patches: `patches: List[Patch] = []`
- Store plans: `deployment_plans: List[DeploymentPlan] = []`
- Link patches to vulnerabilities

## Test

Use `python test.py` to verify patch management.

