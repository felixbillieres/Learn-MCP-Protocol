# Instructions - Projet 11

## Ta mission

Créer un serveur MCP qui expose des prompts (templates de messages).

## Étapes à suivre

1. **Crée un serveur FastMCP** avec support des prompts :
   ```python
   capabilities={"prompts": {}}
   ```

2. **Crée `list_prompts`** décorée avec `@mcp_server.list_prompts()` :
   - Retourne une liste de prompts disponibles
   - Chaque prompt doit avoir :
     - `name` : Identifiant unique (ex: "greeting")
     - `title` : Titre lisible (optionnel)
     - `description` : Description du prompt

3. **Crée `get_prompt`** décorée avec `@mcp_server.get_prompt()` :
   - Prend un paramètre `name` (str)
   - Retourne un dict avec :
     - `messages` : Liste de messages (format pour LLM)
     - Chaque message a `role` ("user" ou "assistant") et `content` avec `type: "text"` et `text: "..."`

4. **Crée au moins 2 prompts** :
   - `greeting` : Un message de salutation
   - `help` : Un message d'aide

## Indices

- Les fonctions doivent être `async`
- Pour `get_prompt`, retourne des messages formatés pour un LLM
- Format d'un message : `{"role": "user", "content": {"type": "text", "text": "..."}}`

## Test

Utilise `python test.py` pour vérifier que les prompts sont listés et récupérables.

