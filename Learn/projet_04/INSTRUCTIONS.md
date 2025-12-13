# Instructions - Projet 04

## Ta mission

Créer un outil qui utilise le Context pour logger des informations pendant son exécution.

## Étapes à suivre

1. **Crée un outil `traiter_fichier`** qui :
   - Prend un paramètre `nom_fichier` (str) et `ctx: Context`
   - Simule le traitement d'un fichier avec plusieurs étapes
   - Utilise le Context pour logger chaque étape

2. **Étapes de traitement** :
   - **Étape 1** : `ctx.info()` : "Début du traitement du fichier {nom_fichier}"
   - **Étape 2** : Vérifie si le fichier existe (simule avec `nom_fichier.endswith(".txt")`)
     - Si oui : `ctx.info()` : "Fichier trouvé"
     - Si non : `ctx.warning()` : "Attention : le fichier ne semble pas être un .txt"
   - **Étape 3** : `ctx.info()` : "Lecture du contenu..."
   - **Étape 4** : Simule une erreur si `nom_fichier == "erreur.txt"`
     - Si erreur : `ctx.error()` : "Erreur lors de la lecture du fichier" puis `raise ValueError(...)`
   - **Étape 5** : `ctx.info()` : "Traitement terminé avec succès"
   - **Retourne** : un dict avec `{"fichier": nom_fichier, "statut": "traité", "lignes": 42}`

3. **Important** :
   - N'oublie pas d'importer `Context` depuis `mcp.server.fastmcp`
   - Utilise `await` pour toutes les méthodes du Context
   - Le paramètre `ctx` doit être le dernier paramètre de la fonction

## Indices

- Importe `Context` : `from mcp.server.fastmcp import Context`
- Utilise `await ctx.info(...)`, `await ctx.warning(...)`, `await ctx.error(...)`
- Le paramètre `ctx: Context` est généralement placé en dernier
- Tu peux utiliser `time.sleep(0.1)` pour simuler un traitement qui prend du temps

## Test

Utilise `python test.py` pour vérifier que :
- L'outil logge correctement les informations
- Les différents niveaux de log fonctionnent

## Résultat attendu

Quand tu appelles l'outil :
- Tu devrais voir des messages de log à chaque étape
- Les messages devraient être adaptés au contexte (info, warning, error)