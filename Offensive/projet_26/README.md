# Projet 26 : Scanner de Ports MCP

## Objectif

Créer un serveur MCP pour scanner des ports et analyser les services, avec génération de rapports de vulnérabilités.

## Concepts à apprendre

### Scanner de ports en cybersécurité

Un scanner de ports est un outil fondamental en sécurité offensive qui permet de :
- Découvrir les ports ouverts sur une cible
- Identifier les services qui écoutent sur ces ports
- Détecter les versions des services
- Analyser les vulnérabilités potentielles

### Architecture MCP pour le scanning

Dans ce projet, tu vas utiliser :
- **Tools** : Pour exécuter les scans et analyses
- **Resources** : Pour exposer les résultats de scan en temps réel
- **Prompts** : Pour générer des rapports de vulnérabilités
- **Modèles Pydantic** : Pour structurer les données de scan

### Modèles de données

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

## Cas d'usage

- **Reconnaissance** : Identifier les services exposés
- **Analyse de surface d'attaque** : Comprendre quels ports sont accessibles
- **Détection de vulnérabilités** : Analyser les versions de services
- **Rapport de sécurité** : Générer des rapports pour les clients

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

