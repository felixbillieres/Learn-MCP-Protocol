# Instructions - Project 28 (Vulnerability Analyzer)

## Your Mission

Create an MCP server to analyze CVEs (Common Vulnerabilities and Exposures) and generate security advisories.

## Steps to Follow

1. **Create Pydantic Models**:
   - `CVE`:
     - `id` : str (CVE identifier, e.g., "CVE-2021-44228")
     - `description` : str
     - `cvss_score` : float (0.0 to 10.0)
     - `severity` : str (enum: "low", "medium", "high", "critical")
     - `affected_products` : List[str]
     - `published_date` : str
   - `VulnerabilityAnalysis`:
     - `cve` : CVE
     - `exploit_available` : bool
     - `recommended_actions` : List[str]

2. **Create Tools**:
   - `rechercher_cve` : Search CVE by ID or product
   - `analyser_cve` : Analyze a CVE and return VulnerabilityAnalysis
   - `lister_cve_par_produit` : List CVEs for a specific product

3. **Create Resource** `cve://list/{product}`:
   - Expose CVEs filtered by product

4. **Create Prompt** `generer_advisory`:
   - Takes `cve_id` argument
   - Generates a formatted security advisory

5. **Create Sampling Tool** (optional):
   - `suggerer_exploit` : Uses sampling to suggest exploits for a CVE

## Hints

- Simulate a CVE database with a few well-known CVEs
- Use CVSS scores to determine severity
- Generate realistic advisories with mitigation steps

## Test

Use `python test.py` to verify CVE search and advisory generation.

