# Projet 05 : Gestion d'erreurs et validation

## Objectif

Apprendre à gérer les erreurs proprement dans tes outils MCP, avec validation des données et messages d'erreur clairs.

## Concepts à apprendre

### Pourquoi gérer les erreurs ?

Dans MCP, il faut :
- **Valider les entrées** avant de les utiliser
- **Gérer les cas d'erreur** proprement
- **Retourner des messages clairs** au client
- **Utiliser le Context** pour logger les erreurs

### Types d'erreurs en Python

```python
# ValueError : valeur invalide
if age < 0:
    raise ValueError("L'âge ne peut pas être négatif")

# RuntimeError : erreur d'exécution
if not ressource_disponible:
    raise RuntimeError("La ressource n'est pas disponible")

# KeyError, TypeError, etc. : erreurs Python natives
```

### Bonne pratique : Valider tôt, logger toujours

```python
@mcp_server.tool()
async def mon_outil(param: str, ctx: Context):
    # 1. Valider les entrées
    if not param:
        await ctx.error("Le paramètre ne peut pas être vide")
        raise ValueError("param est vide")

    # 2. Logger le début
    await ctx.info(f"Traitement de {param}")

    # 3. Essayer l'opération
    try:
        result = faire_operation(param)
    except SpecificError as e:
        await ctx.error(f"Erreur lors de l'opération : {e}")
        raise RuntimeError(f"Impossible de traiter {param}") from e

    # 4. Retourner le résultat
    return result
```

## Exemple dans Exegol-MCP

Regarde `src/assets/tools_container.py` :

```26:31:Exegol-MCP/src/assets/tools_container.py
    # 1. Check if container exists
    container = get_container_by_name(container_name)
    if not container:
        await ctx.error(f"Container '{container_name}' not found")
        raise ValueError(f"Container '{container_name}' not found")
```

Et aussi :

```33:39:Exegol-MCP/src/assets/tools_container.py
    # 2. Check if container is running
    if not container.isRunning():
        error_msg = (
            f"Container '{container_name}' is not running. "
            f"Please start it first using the 'start_container' tool."
        )
        await ctx.error(error_msg)
        raise RuntimeError(error_msg)
```

## Ce que tu vas créer

Dans ce projet, tu vas créer un outil qui :
- Valide les paramètres d'entrée
- Gère différents cas d'erreur
- Utilise le Context pour logger les erreurs
- Retourne des messages d'erreur clairs

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !