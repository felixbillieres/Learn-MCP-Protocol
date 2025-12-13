# Projet 03 : Utiliser les modèles Pydantic

## Objectif

Apprendre à utiliser Pydantic pour structurer et valider les données dans tes outils MCP.

## Concepts à apprendre

### Qu'est-ce que Pydantic ?

Pydantic est une bibliothèque Python qui permet de :
- **Définir des modèles de données** avec validation automatique
- **Valider les types** automatiquement
- **Documenter les données** avec des descriptions
- **Convertir** entre Python et JSON facilement

### Pourquoi utiliser Pydantic dans MCP ?

Dans MCP, les données passent souvent en JSON. Pydantic permet de :
- S'assurer que les données sont correctes avant de les utiliser
- Avoir une documentation claire de ce que ton outil attend/retourne
- Avoir une meilleure structure de code

### Créer un modèle Pydantic

```python
from pydantic import BaseModel, Field

class Personne(BaseModel):
    nom: str = Field(description="Le nom de la personne")
    age: int = Field(description="L'âge de la personne", ge=0, le=120)
    email: str | None = Field(None, description="Email optionnel")
```

### Utiliser un modèle dans un outil

```python
@mcp_server.tool()
async def creer_personne(personne: Personne) -> Personne:
    """Crée une personne"""
    return personne  # Pydantic valide automatiquement !
```

## Exemple dans Exegol-MCP

Regarde `src/models/container.py` :

```23:25:Exegol-MCP/src/models/container.py
class ExecutionResult(BaseModel):
    exit_code: int = Field(description="Exit code of the command")
    output: str = Field(description="Command output (stdout + stderr)")
```

Et son utilisation dans `src/assets/tools_container.py` :

```9:13:Exegol-MCP/src/assets/tools_container.py
@mcp_server.tool()
async def execute_command_in_container(
        container_name: str,
        command: str,
        ctx: Context
) -> ExecutionResult:
```

## Ce que tu vas créer

Dans ce projet, tu vas :
1. Créer un modèle Pydantic `Message` pour représenter un message
2. Créer un outil qui utilise ce modèle
3. Voir comment Pydantic valide automatiquement les données

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !