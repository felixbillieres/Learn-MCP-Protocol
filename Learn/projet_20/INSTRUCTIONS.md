# Instructions - Projet 20

## Ta mission

Créer un serveur qui simule la validation de tokens OAuth.

## Étapes à suivre

1. **Crée un serveur FastMCP** basique

2. **Crée une fonction `valider_token`** :
   - Prend un token (str)
   - Simule la validation (vérifie format, expiration, etc.)
   - Retourne un dict avec user info si valide
   - Retourne None si invalide

3. **Crée un outil `info_utilisateur`** :
   - Nécessite un token valide (simulé via paramètre `token`)
   - Valide le token
   - Retourne les infos de l'utilisateur

4. **Crée un outil `donnees_sensibles`** :
   - Nécessite aussi un token valide
   - Simule l'accès à des données sensibles
   - Retourne les données si autorisé

## Indices

- Pour ce projet, on simule l'autorisation (pas de vrai OAuth)
- Dans un vrai serveur, FastMCP gère automatiquement les tokens HTTP
- Tu peux stocker des tokens valides dans un dict pour simulation
- Valide le format du token (ex: doit commencer par "Bearer ")

## Test

Le test vérifiera que la validation fonctionne.

