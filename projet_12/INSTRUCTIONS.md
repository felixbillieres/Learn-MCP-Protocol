# Instructions - Projet 12

## Ta mission

Créer des prompts avec des arguments dynamiques pour personnaliser le contenu.

## Étapes à suivre

1. **Utilise la base du projet 11** ou crée un nouveau serveur

2. **Modifie `list_prompts`** pour inclure les arguments :
   - Chaque prompt peut avoir un champ `arguments` (liste)
   - Chaque argument a `name`, `description`, `required`

3. **Modifie `get_prompt`** pour accepter des arguments :
   - Prend un paramètre `arguments` (dict, optionnel)
   - Utilise les arguments pour remplacer des placeholders dans le texte
   - Valide que les arguments requis sont présents

4. **Crée au moins 2 prompts avec arguments** :
   - `code_review` : Prend `language` (requis) et `code` (requis)
   - `summary` : Prend `topic` (requis) et `length` (optionnel, défaut "short")

## Indices

- Utilise `.format()` ou f-strings pour remplacer les arguments
- Valide les arguments requis avant de générer le message
- Si un argument requis est manquant, lève `ValueError`

## Test

Utilise `python test.py` pour vérifier que les prompts avec arguments fonctionnent.

