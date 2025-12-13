# Instructions - Projet 15

## Ta mission

Créer des outils avec des schémas d'elicitation complexes et validés.

## Étapes à suivre

1. **Crée un serveur FastMCP** basique

2. **Crée un outil `inscription`** avec un schéma détaillé :
   - Demande :
     - `username` : string, minLength 3, maxLength 20, pattern alphanumeric
     - `email` : string, format email
     - `age` : integer, minimum 13, maximum 120
     - `newsletter` : boolean, défaut false
   - Valide les données reçues
   - Retourne un message de confirmation

3. **Crée un outil `commander_produit`** avec enum :
   - Demande :
     - `produit` : enum avec valeurs "basic", "premium", "enterprise"
     - `quantite` : integer, minimum 1, maximum 100
     - `livraison_express` : boolean
   - Retourne un résumé de commande

4. **Valide les réponses** :
   - Vérifie que les valeurs respectent les contraintes du schéma
   - Lève des erreurs appropriées si la validation échoue

## Indices

- Le schéma doit suivre JSON Schema strictement
- Utilise `pattern` pour la validation regex (ex: `"^[a-zA-Z0-9]+$"`)
- Les formats comme `email` sont validés automatiquement par le client
- Valide aussi côté serveur pour la sécurité

## Test

Le test vérifiera que les schémas sont correctement structurés.

