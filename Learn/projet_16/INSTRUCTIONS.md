# Instructions - Projet 16

## Ta mission

Créer un outil qui utilise l'elicitation URL mode pour l'authentification sécurisée.

## Étapes à suivre

1. **Crée un serveur FastMCP** basique

2. **Crée un outil `authentifier`** :
   - Utilise `ctx.elicitation.create()` avec `mode="url"`
   - Demande une URL d'authentification (ex: `https://auth.example.com/login`)
   - Retourne un message indiquant que l'utilisateur doit s'authentifier via l'URL

3. **Crée un outil `configurer_api_key`** :
   - Utilise aussi URL mode
   - Redirige vers une page pour configurer une clé API
   - Retourne une confirmation

4. **Important** :
   - Pour URL mode, utilise `mode="url"` dans l'elicitation
   - L'URL fournie doit être complète (avec https://)
   - Le serveur doit expliquer clairement pourquoi l'URL est nécessaire

## Indices

- URL mode utilise la même API mais avec `mode: "url"` et une `url` au lieu de `requested_schema`
- Le format est : `{"mode": "url", "message": "...", "url": "https://..."}`
- L'utilisateur sera redirigé vers l'URL pour compléter l'action

## Test

Le test vérifiera que les outils utilisent bien URL mode.

