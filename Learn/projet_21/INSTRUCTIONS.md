# Instructions - Projet 21

## Ta mission

Créer une validation de tokens avec scopes et audiences.

## Étapes à suivre

1. **Crée un serveur FastMCP**

2. **Améliore `valider_token`** pour accepter :
   - `required_scopes` : Liste de scopes requis (optionnel)
   - `required_audience` : Audience requise (optionnel)

3. **Ajoute des tokens avec scopes et audiences** :
   - Token avec scopes : "read:data", "write:data"
   - Token avec audience : "api.example.com"

4. **Crée des outils qui nécessitent des scopes** :
   - `lire_donnees` : Nécessite scope "read:data"
   - `ecrire_donnees` : Nécessite scope "write:data"

