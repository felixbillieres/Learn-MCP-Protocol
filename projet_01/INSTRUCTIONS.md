# Instructions - Projet 01

## Ta mission

Crée un serveur MCP basique qui affiche un message de démarrage.

## Étapes à suivre

1. **Crée un serveur FastMCP** dans `solution.py` :
   - Nom du serveur : `"MonPremierServeur"`
   - Host : `"127.0.0.1"`
   - Port : `8000`
   - Options : `stateless_http=True` et `json_response=True`

2. **Crée une fonction `main()`** qui :
   - Affiche un message : `" Mon premier serveur MCP démarre !"`
   - Affiche l'URL du serveur : `"URL: http://127.0.0.1:8000/mcp"`
   - Démarre le serveur avec `mcp_server.run(transport="streamable-http")`

3. **Ajoute le point d'entrée** `if __name__ == "__main__": main()`

## Indices

- Importe `FastMCP` depuis `mcp.server.fastmcp`
- Suis le modèle d'Exegol-MCP (`src/mcp_app.py` et `src/main.py`)
- Ne t'inquiète pas si le serveur ne fait rien d'autre pour l'instant, c'est normal !

## Test

Une fois terminé, lance `python solution.py` et vérifie que :
- Le message s'affiche
- Le serveur démarre (il va rester en écoute, c'est normal)

Pour tester, tu peux aussi utiliser `python test.py` qui vérifie que le serveur est bien créé.

## Résultat attendu

Quand tu lances le serveur, tu devrais voir :
```
 Mon premier serveur MCP démarre !
URL: http://127.0.0.1:8000/mcp
```

Le serveur reste ensuite en écoute (appuie sur Ctrl+C pour l'arrêter).