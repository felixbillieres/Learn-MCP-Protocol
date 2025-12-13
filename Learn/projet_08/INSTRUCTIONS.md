# Instructions - Projet 08

## Ta mission

Créer un serveur MCP qui expose des ressources de configuration.

## Étapes à suivre

1. **Crée un serveur FastMCP** basique

2. **Crée un serveur FastMCP** basique (le support des resources est détecté automatiquement)

3. **Crée une fonction `list_resources`** et enregistre-la avec FastMCP :
   ```python
   async def list_resources() -> list[dict[str, Any]]:
       # Implémente la logique
       pass
   
   # Enregistre la fonction
   mcp_server.list_resources = list_resources
   ```
   - Retourne une liste de ressources
   - Chaque ressource doit avoir :
     - `uri` : L'URI unique (ex: `"config://app/settings"`)
     - `name` : Un nom court
     - `description` : Description de la ressource
     - `mimeType` : Type MIME (ex: `"application/json"` ou `"text/plain"`)

4. **Crée une fonction `read_resource`** et enregistre-la avec FastMCP :
   ```python
   async def read_resource(uri: str, ctx: Context = None) -> dict[str, Any]:
       # Implémente la logique
       pass
   
   # Enregistre la fonction
   mcp_server.read_resource = read_resource
   ```
   - Prend un paramètre `uri` (str)
   - Retourne le contenu de la ressource
   - Si l'URI n'existe pas, lève une `ValueError`

5. **Expose au moins 2 ressources** :
   - `config://app/settings` : Configuration de l'app (JSON)
   - `info://server/version` : Version du serveur (texte)

## Indices

- Les fonctions doivent être `async`
- **Important** : Dans FastMCP, tu dois assigner directement les fonctions (`mcp_server.list_resources = list_resources`) au lieu d'utiliser des décorateurs
- Pour `read_resource`, retourne un dict avec `contents` qui contient une liste
- Chaque contenu a : `uri`, `mimeType`, et soit `text` (pour texte) soit `blob` (pour binaire base64)

## Test

Utilise `python test.py` pour vérifier que les ressources sont listées et lisibles.