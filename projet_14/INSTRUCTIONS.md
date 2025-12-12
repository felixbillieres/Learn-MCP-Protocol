# Instructions - Projet 14

## Ta mission

Créer un outil qui utilise l'elicitation pour demander des informations à l'utilisateur.

## Étapes à suivre

1. **Crée un serveur FastMCP** basique

2. **Crée un outil `creer_profil`** :
   - Ne prend pas de paramètres (ou seulement `ctx: Context`)
   - Utilise `await ctx.elicitation.create()` pour demander :
     - Nom (string)
     - Age (integer)
     - Email (string, optionnel)
   - Retourne un dict avec les informations collectées

3. **Crée un outil `configurer_preferences`** :
   - Demande via elicitation :
     - Thème préféré (enum: "dark", "light", "auto")
     - Notifications activées (boolean)
   - Retourne les préférences

## Indices

- L'elicitation nécessite un schéma JSON pour définir les champs demandés
- Utilise `ctx.elicitation.create()` avec `message` et `requested_schema`
- Le schéma suit le format JSON Schema (type, title, description, etc.)
- La réponse est un dict avec les valeurs fournies

## Test

Note: L'elicitation nécessite un vrai client MCP pour être testée. Le test vérifiera que l'outil peut être appelé.

