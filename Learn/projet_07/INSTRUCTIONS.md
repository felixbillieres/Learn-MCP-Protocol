# Instructions - Projet 07 (PROJET FINAL)

## Ta mission

Créer un serveur MCP complet pour gérer une liste de tâches (todo list), en utilisant TOUS les concepts appris !

## Fonctionnalités à implémenter

### 1. Modèles Pydantic

**Crée `Tache`** :
- `id` : int (obligatoire)
- `titre` : str (obligatoire, min 1 caractère)
- `description` : str | None (optionnel)
- `termine` : bool (défaut False)
- `priorite` : str (défaut "normale", valeurs possibles: "basse", "normale", "haute", "urgente")
- `tags` : List[str] (liste de tags, peut être vide)
- `date_creation` : str (date au format "YYYY-MM-DD HH:MM:SS")

**Crée `StatistiquesTaches`** :
- `total` : int
- `terminees` : int
- `en_cours` : int
- `par_priorite` : Dict[str, int]
- `par_tag` : Dict[str, int]

### 2. Outils à créer

#### `creer_tache`
- Paramètres : `titre` (str), `description` (str | None), `priorite` (str, défaut "normale"), `tags` (List[str], défaut []), `ctx: Context`
- Valide que le titre n'est pas vide
- Génère un ID unique (compteur ou random)
- Crée la date de création
- Ajoute la tâche à la liste
- Retourne : `Tache`
- Logge avec `ctx.info()`

#### `lister_taches`
- Paramètres : `termine` (bool | None, optionnel pour filtrer), `priorite` (str | None, optionnel), `tag` (str | None, optionnel), `ctx: Context`
- Retourne : `List[Tache]`
- Filtre selon les paramètres fournis
- Logge avec `ctx.info()`

#### `obtenir_tache`
- Paramètres : `tache_id` (int), `ctx: Context`
- Retourne : `Tache`
- Valide que la tâche existe
- Si non trouvée : `ctx.error()` + `raise ValueError`
- Logge avec `ctx.info()`

#### `modifier_tache`
- Paramètres : `tache_id` (int), `titre` (str | None), `description` (str | None), `priorite` (str | None), `tags` (List[str] | None), `ctx: Context`
- Retourne : `Tache` (modifiée)
- Valide que la tâche existe
- Met à jour seulement les champs fournis (pas None)
- Valide la priorité si fournie
- Logge avec `ctx.info()`

#### `marquer_termine`
- Paramètres : `tache_id` (int), `termine` (bool, défaut True), `ctx: Context`
- Retourne : `Tache`
- Valide que la tâche existe
- Change le statut `termine`
- Logge avec `ctx.info()`

#### `supprimer_tache`
- Paramètres : `tache_id` (int), `ctx: Context`
- Retourne : `bool` (True si supprimée)
- Valide que la tâche existe
- Supprime la tâche de la liste
- Logge avec `ctx.warning()` (car c'est une action destructive)
- Si non trouvée : `ctx.error()` + `raise ValueError`

#### `obtenir_statistiques`
- Paramètres : `ctx: Context`
- Retourne : `StatistiquesTaches`
- Calcule toutes les statistiques
- Logge avec `ctx.info()`

### 3. Structure du code

```python
# Imports
from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

# Serveur MCP
mcp_server = FastMCP(...)

# Liste globale pour stocker les tâches
taches = []

# Modèles Pydantic
class Tache(BaseModel):
    ...

class StatistiquesTaches(BaseModel):
    ...

# Outils
@mcp_server.tool()
async def creer_tache(...):
    ...

# etc.

def main():
    ...

if __name__ == "__main__":
    main()
```

## Conseils

1. **Organise ton code** : modèles d'abord, puis outils
2. **Valide tôt** : vérifie les paramètres au début de chaque fonction
3. **Logge toujours** : utilise `ctx.info()`, `ctx.warning()`, `ctx.error()`
4. **Messages clairs** : les erreurs doivent être compréhensibles
5. **Réutilise la logique** : crée peut-être une fonction `trouver_tache(id)` pour éviter la duplication

## Test

Utilise `python test.py` pour tester toutes les fonctionnalités.

## Résultat attendu

Un serveur MCP fonctionnel qui permet de :
- Créer des tâches
- Lister et filtrer les tâches
- Modifier et supprimer des tâches
- Obtenir des statistiques

C'est ton projet final ! Montre-moi ce que tu as créé !