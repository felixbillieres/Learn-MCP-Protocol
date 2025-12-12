# Projet 02 : Ajouter un premier outil (tool)

## Objectif

Ajouter ton premier outil (tool) à ton serveur MCP. Les outils sont des fonctions que les clients MCP peuvent appeler !

## Concepts à apprendre

### Qu'est-ce qu'un outil (tool) ?

Un outil est une fonction Python décorée avec `@mcp_server.tool()` qui :
- Peut recevoir des paramètres
- Peut retourner des résultats
- Est automatiquement exposée par le serveur MCP
- Peut être appelée par les clients MCP (comme Claude Desktop)

### Le décorateur @mcp_server.tool()

Ce décorateur transforme une fonction Python normale en outil MCP. Exemple :

```python
@mcp_server.tool()
async def ma_fonction(param1: str, param2: int) -> str:
    """Description de l'outil"""
    return f"Résultat: {param1} et {param2}"
```

**Important** : Les outils doivent être des fonctions `async` (asynchrones) !

### Docstring = Description

La docstring de ta fonction devient la description de l'outil dans MCP. C'est ce qui sera visible par les clients !

## Exemple dans Exegol-MCP

Regarde `src/assets/tools_orchestractor.py` :

```10:22:Exegol-MCP/src/assets/tools_orchestractor.py
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

Dans ce projet, tu vas créer deux outils simples :
1. `dire_bonjour` : prend un nom en paramètre et retourne un message de salutation
2. `calculer_somme` : prend deux nombres et retourne leur somme

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !