# Instructions - Projet 17

## Ta mission

Créer un outil qui utilise le sampling pour demander une complétion LLM.

## Étapes à suivre

1. **Crée un serveur FastMCP** basique

2. **Crée un outil `poser_question`** :
   - Prend un paramètre `question` (str) et `ctx: Context`
   - Utilise `await ctx.sampling.create_message()` pour demander une réponse au LLM
   - Construis un message avec role "user" et content avec type "text"
   - Retourne la réponse du LLM

3. **Crée un outil `generer_resume`** :
   - Prend un paramètre `texte` (str) et `ctx: Context`
   - Demande au LLM de générer un résumé du texte
   - Utilise un system prompt pour guider le LLM
   - Retourne le résumé

## Indices

- Utilise `ctx.sampling.create_message()` avec une liste de `messages`
- Chaque message a `role` ("user" ou "system") et `content` avec `type: "text"` et `text: "..."`
- Pour system prompt, utilise `system_prompt` en paramètre ou un message avec role "system"
- La réponse contient `role`, `content`, et peut-être `model` et `stop_reason`

## Test

Note: Le sampling nécessite un vrai client MCP avec LLM. Le test vérifiera que l'outil peut être appelé.

