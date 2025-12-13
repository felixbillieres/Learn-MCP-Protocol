# Instructions - Project 35 (Malware Analyzer)

## Your Mission

Create a malware analysis system with YARA rule generation.

## Steps to Follow

1. **Create Pydantic Models**:
   - `MalwareSample`:
     - `id` : int
     - `filename` : str
     - `file_hash` : str (MD5 or SHA256)
     - `file_size` : int
     - `file_type` : str
     - `uploaded_at` : str
   - `AnalysisResult`:
     - `sample_id` : int
     - `suspicious_score` : float (0.0 to 1.0)
     - `indicators` : List[str]
     - `strings` : List[str] (extracted strings)
     - `behavior` : Dict[str, Any] | None
     - `threat_intel_matches` : List[str]
   - `YaraRule`:
     - `id` : str
     - `name` : str
     - `rule_text` : str
     - `description` : str

2. **Create Tools**:
   - `analyser_fichier` : Analyze a file (uses elicitation for confirmation)
   - `extraire_strings` : Extract strings from file
   - `comparer_threat_intel` : Compare with threat intelligence
   - `generer_yara_rule` : Generate YARA rule (uses prompts)

3. **Create Resources**:
   - `analysis://{sample_id}` : Get analysis results
   - `yara://rules` : List YARA rules

4. **Create Prompts**:
   - `generer_yara_rule` : Generate YARA rule based on analysis

5. **Use Elicitation**:
   - Confirm before analyzing potentially dangerous files
   - Ask for analysis type (static/dynamic)

## Hints

- Store samples: `samples: List[MalwareSample] = []`
- Store results: `results: Dict[int, AnalysisResult] = {}`
- Store rules: `yara_rules: List[YaraRule] = []`
- Simulate file analysis (don't actually execute malware)

## Test

Use `python test.py` to verify malware analysis.

