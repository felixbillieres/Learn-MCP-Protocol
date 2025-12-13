# Instructions - Projet 02

## Ta mission

Ajoute deux outils simples à ton serveur MCP.

## Étapes à suivre

1. **Utilise le serveur du projet 01** comme base (ou crée-en un nouveau)

2. **Crée l'outil `dire_bonjour`** :
   - Prend un paramètre `nom` (type `str`)
   - Retourne une string avec un message : `f"Bonjour, {nom} ! Comment vas-tu ?"`
   - Ajoute une docstring descriptive
   - Utilise le décorateur `@mcp_server.tool()`
   - La fonction doit être `async`

3. **Crée l'outil `calculer_somme`** :
   - Prend deux paramètres `a` et `b` (type `int`)
   - Retourne un `int` : la somme de a et b
   - Ajoute une docstring descriptive
   - Utilise le décorateur `@mcp_server.tool()`
   - La fonction doit être `async`

## Indices

- N'oublie pas le `async` devant `def` !
- N'oublie pas le décorateur `@mcp_server.tool()` juste avant la fonction
- La docstring est importante pour décrire l'outil
- Les types de paramètres et de retour sont importants (MCP les utilise)

## Test

Utilise `python test.py` pour vérifier que :
- Les outils sont bien enregistrés
- Les outils fonctionnent correctement

## Résultat attendu

Quand tu lances le serveur et qu'un client l'appelle :
- `dire_bonjour("Alice")` devrait retourner `"Bonjour, Alice ! Comment vas-tu ?"`
- `calculer_somme(5, 3)` devrait retourner `8`