# Instructions - Projet 08

## Ta mission

Créer un serveur MCP qui expose des ressources de configuration.

## Étapes à suivre

1. **Crée un serveur FastMCP** basique

2. **Déclare le support des resources** dans les capabilities :
   ```python
   mcp_server = FastMCP(
       "MonServeur",
       capabilities={"resources": {}}  # Active le support des resources
   )
   ```

3. **Crée une fonction `list_resources`** décorée avec `@mcp_server.list_resources()` :
   - Retourne une liste de ressources
   - Chaque ressource doit avoir :
     - `uri` : L'URI unique (ex: `"config://app/settings"`)
     - `name` : Un nom court
     - `description` : Description de la ressource
     - `mimeType` : Type MIME (ex: `"application/json"` ou `"text/plain"`)

4. **Crée une fonction `read_resource`** décorée avec `@mcp_server.read_resource()` :
   - Prend un paramètre `uri` (str)
   - Retourne le contenu de la ressource
   - Si l'URI n'existe pas, lève une `ValueError`

5. **Expose au moins 2 ressources** :
   - `config://app/settings` : Configuration de l'app (JSON)
   - `info://server/version` : Version du serveur (texte)

## Indices

- Les fonctions doivent être `async`
- Pour `read_resource`, retourne un dict avec `contents` qui contient une liste
- Chaque contenu a : `uri`, `mimeType`, et soit `text` (pour texte) soit `blob` (pour binaire base64)

## Test

Utilise `python test.py` pour vérifier que les ressources sont listées et lisibles.