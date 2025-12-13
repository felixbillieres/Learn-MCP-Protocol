# Instructions - Projet 09

## Ta mission

Créer des resources avec templates URI pour accéder à des fichiers de configuration dynamiquement.

## Étapes à suivre

1. **Crée un serveur FastMCP** avec support des resources

2. **Implémente `list_resources`** pour les resources statiques :
   - Retourne une ressource statique : `info://server/about` avec les infos du serveur

3. **Crée `list_resource_templates`** décorée avec `@mcp_server.list_resource_templates()` :
   - Retourne une liste de templates
   - Chaque template doit avoir :
     - `uriTemplate` : Le template URI (ex: `"config://{section}/{key}"`)
     - `name` : Nom du template
     - `description` : Description
     - `mimeType` : Type MIME

4. **Adapte `read_resource`** pour gérer les templates :
   - Si l'URI correspond à un template (ex: `config://database/host`), extraire les paramètres
   - Retourner le contenu approprié
   - Si l'URI ne correspond à aucun template, lancer `ValueError`

5. **Templates à créer** :
   - `config://{section}/{key}` : Accès à des configurations par section/clé
   - `file://{filename}` : Accès à des fichiers virtuels

## Indices

- Utilise `re` ou `urllib.parse` pour parser les URIs et extraire les paramètres
- Stocke des données de configuration simulées dans un dict
- Pour `config://{section}/{key}`, parse l'URI pour extraire `section` et `key`

## Test

Utilise `python test.py` pour vérifier que les templates fonctionnent.