# Instructions - Projet 26 (Scanner de Ports)

## Ta mission

Créer un serveur MCP pour scanner des ports et analyser les services avec génération de rapports.

## Étapes à suivre

1. **Crée les modèles Pydantic** :
   - `PortInfo` :
     - `port` : int (obligatoire)
     - `state` : str (obligatoire, valeurs: "open", "closed", "filtered")
     - `service` : str | None (optionnel, ex: "ssh", "http", "mysql")
     - `version` : str | None (optionnel, version du service)
   - `ScanResult` :
     - `target` : str (obligatoire, IP ou hostname)
     - `ports` : List[PortInfo] (obligatoire)
     - `timestamp` : str (obligatoire, format ISO)
     - `scan_type` : str (obligatoire, ex: "quick", "full")

2. **Crée le serveur FastMCP** avec capabilities pour resources :
   ```python
   capabilities={"resources": {}}
   ```

3. **Crée l'outil `scanner_ports`** :
   - Paramètres : `target` (str), `ports` (List[int] | None, optionnel), `scan_type` (str, défaut "quick"), `ctx: Context`
   - Simule un scan de ports (génère des résultats aléatoires ou prédéfinis)
   - Stocke le résultat dans une liste globale `scans = []`
   - Retourne : `ScanResult`
   - Logge avec `ctx.info()`

4. **Crée l'outil `analyser_services`** :
   - Paramètres : `scan_id` (int, index dans la liste), `ctx: Context`
   - Analyse les services détectés dans un scan
   - Identifie les versions et vulnérabilités potentielles
   - Retourne : `Dict[str, Any]` avec les analyses
   - Logge avec `ctx.info()`

5. **Crée la resource `scan://results/{scan_id}`** :
   - Expose les résultats de scan via resources
   - Utilise un template URI pour accéder aux scans par ID
   - Retourne le `ScanResult` au format JSON

6. **Crée le prompt `generer_rapport_vulnerabilites`** :
   - Prend un argument `scan_id` (int)
   - Génère un rapport de vulnérabilités basé sur les résultats du scan
   - Retourne un template de rapport formaté

## Indices

- Pour simuler le scan, utilise des ports communs : `[22, 80, 443, 3306, 5432, 8080]`
- Génère des services aléatoires : `["ssh", "http", "https", "mysql", "postgresql"]`
- Pour le timestamp : `from datetime import datetime` puis `datetime.now().isoformat()`
- Stocke les scans dans une liste globale : `scans: List[ScanResult] = []`

## Test

Utilise `python test.py` pour vérifier que :
- Les scans fonctionnent
- Les resources exposent les résultats
- Les prompts génèrent des rapports

## Résultat attendu

- Scanner des ports sur une cible
- Analyser les services détectés
- Exposer les résultats via resources
- Générer des rapports de vulnérabilités

