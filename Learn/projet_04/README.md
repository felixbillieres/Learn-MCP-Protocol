# Projet 04 : Utiliser le Context pour le logging

## Objectif

Apprendre à utiliser le `Context` MCP pour logger des informations (info, warning, error) pendant l'exécution des outils.

## Concepts à apprendre

### Qu'est-ce que le Context ?

Le `Context` est un objet passé automatiquement aux outils MCP qui permet de :
- **Logger des informations** (`ctx.info()`, `ctx.warning()`, `ctx.error()`)
- **Suivre l'exécution** de l'outil en temps réel
- **Informer le client** de ce qui se passe

### Méthodes du Context

```python
@mcp_server.tool()
async def mon_outil(ctx: Context):
    await ctx.info("Début de l'opération")
    await ctx.warning("Attention, ceci est un avertissement")
    await ctx.error("Une erreur s'est produite")
```

**Important** : Ces méthodes sont `async` ! Il faut utiliser `await`.

### Pourquoi utiliser le Context ?

- Permet au client de voir ce qui se passe en temps réel
- Utile pour le débogage
- Donne de la visibilité sur l'exécution
- Peut informer l'utilisateur de problèmes sans arrêter l'exécution

## Exemple dans Exegol-MCP

Regarde `src/assets/tools_container.py` :

```23:24:Exegol-MCP/src/assets/tools_container.py
    await ctx.info(f"Executing command '{command}' in container {container_name}")
    await check_exegol_readiness(ctx)
```

Et aussi :

```29:30:Exegol-MCP/src/assets/tools_container.py
        await ctx.error(f"Container '{container_name}' not found")
        raise ValueError(f"Container '{container_name}' not found")
```

Et :

```44:46:Exegol-MCP/src/assets/tools_container.py
    if exit_code == 0:
        await ctx.info(f"Command executed successfully")
    else:
```

## Ce que tu vas créer

Dans ce projet, tu vas créer un outil qui :
- Utilise le Context pour logger les étapes
- Affiche des messages info, warning et error selon le contexte
- Montre comment le logging aide à comprendre ce qui se passe

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !