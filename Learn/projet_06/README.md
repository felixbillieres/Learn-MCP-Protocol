# Projet 06 : Outils avec paramètres complexes

## Objectif

Créer des outils plus avancés avec des paramètres complexes (listes, dictionnaires, modèles Pydantic imbriqués).

## Concepts à apprendre

### Types complexes en MCP

Les outils MCP peuvent accepter :
- **Types de base** : `str`, `int`, `float`, `bool`
- **Listes** : `List[str]`, `List[int]`, etc.
- **Dictionnaires** : `Dict[str, str]`, etc.
- **Modèles Pydantic** : Tes propres classes
- **Types optionnels** : `str | None`, `Optional[str]`

### Exemple avec liste

```python
from typing import List

@mcp_server.tool()
async def traiter_liste(items: List[str], ctx: Context) -> List[str]:
    """Traite une liste d'items"""
    return [item.upper() for item in items]
```

### Exemple avec modèle Pydantic imbriqué

```python
from pydantic import BaseModel, Field
from typing import List

class Adresse(BaseModel):
    rue: str
    ville: str

class Personne(BaseModel):
    nom: str
    age: int
    adresses: List[Adresse]  # Liste de modèles !
```

## Exemple dans Exegol-MCP

Regarde `src/models/container.py` :

```6:21:Exegol-MCP/src/models/container.py
class ContainerInfo(BaseModel):
    """Container information from Exegol SDK"""
    name: str
    creation_date: str
    image_name: str
    image_version: str
    status: str
    network_driver: Optional[str]
    network_name: Optional[str]
    features: List[str]
    devices: List[str]
    vpn: Optional[str]
    env: List[str]
    is_privileged: bool
    capabilities: List[str]
    comment: Optional[str]
```

Et son utilisation avec une liste :

```11:22:Exegol-MCP/src/assets/tools_orchestractor.py
@mcp_server.tool()
async def list_exegol_containers(ctx: Context) -> List[ContainerInfo]:
    """List all available Exegol containers with their status.
        Returns a list of Exegol containers configured on the system
        with their detailed information (name, status, image, network_driver etc...) in a chart.
        Returns:
            List of Exegol containers with their metadata
        Raises:
            RuntimeError: If Exegol is not ready or configured
    """
    await ctx.info("Starting action: Listing Exegol containers")
    await check_exegol_readiness(ctx)
    return await get_exegol_container()
```

## Ce que tu vas créer

Dans ce projet, tu vas créer :
1. Un modèle `Utilisateur` avec des listes et des champs optionnels
2. Un outil qui manipule des listes d'utilisateurs
3. Un outil qui retourne des données complexes

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !