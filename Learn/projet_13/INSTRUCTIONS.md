# Instructions - Projet 13

## Ta mission

Créer des prompts avancés avec messages multiples et références à des resources.

## Étapes à suivre

1. **Crée un serveur** avec support des prompts ET des resources

2. **Crée des resources** :
   - `doc://examples/code_sample` : Un exemple de code
   - `doc://guidelines/best_practices` : Des bonnes pratiques

3. **Crée un prompt avancé `tutorial`** :
   - Prend un argument `topic` (requis)
   - Retourne plusieurs messages :
     1. Message système expliquant le contexte
     2. Message utilisateur avec la question
     3. (Optionnel) Message assistant avec un exemple

4. **Crée un prompt `code_analysis`** :
   - Prend `code` (requis)
   - Retourne un message qui référence une resource contenant les guidelines
   - Utilise le format de resource intégrée dans le message

## Indices

- Pour les resources intégrées, utilise le format : `{"type": "resource", "resource": {...}}`
- Les messages multiples permettent de créer un contexte riche
- Combine resources et arguments pour des prompts puissants

## Test

Utilise `python test.py` pour vérifier que les prompts avancés fonctionnent.

