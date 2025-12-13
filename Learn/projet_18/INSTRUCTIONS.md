# Instructions - Projet 18

## Ta mission

Créer des outils qui utilisent les paramètres avancés du sampling.

## Étapes à suivre

1. **Crée un serveur FastMCP** basique

2. **Crée un outil `creatif_ideation`** :
   - Prend `sujet` (str) et `ctx: Context`
   - Utilise sampling avec :
     - `temperature`: 0.9 (créatif)
     - `model_preferences`: intelligencePriority élevé
     - Demande des idées créatives sur le sujet
   - Retourne les idées

3. **Crée un outil `conversation`** :
   - Prend `messages_historique` (list de dict) et `nouveau_message` (str) et `ctx: Context`
   - Construit une conversation avec l'historique
   - Utilise `max_tokens`: 500
   - Retourne la réponse

4. **Crée un outil `reponse_rapide`** :
   - Prend `question` (str) et `ctx: Context`
   - Utilise sampling avec :
     - `speed_priority`: élevé
     - `max_tokens`: 100 (courte réponse)
   - Retourne une réponse rapide

## Indices

- Utilise `model_preferences` avec `intelligencePriority`, `speedPriority`, etc.
- `temperature` contrôle la créativité (0 = déterministe, 2 = très créatif)
- Pour les conversations, passe tous les messages dans la liste

## Test

Le test vérifiera que les outils utilisent les paramètres avancés.

