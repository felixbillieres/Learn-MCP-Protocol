# Instructions - Projet 06

## Ta mission

Créer des outils avec des paramètres et retours complexes (listes, modèles imbriqués).

## Étapes à suivre

1. **Crée un modèle Pydantic `Utilisateur`** :
   - `id` : int (obligatoire)
   - `nom` : str (obligatoire)
   - `email` : str | None (optionnel)
   - `tags` : List[str] (liste de tags, peut être vide)
   - `score` : float (obligatoire, valeur par défaut 0.0)
   - Utilise `Field()` pour les descriptions

2. **Crée un modèle `StatistiquesUtilisateurs`** :
   - `total` : int (nombre total d'utilisateurs)
   - `par_tag` : Dict[str, int] (nombre d'utilisateurs par tag)
   - `score_moyen` : float (score moyen)

3. **Crée l'outil `ajouter_utilisateur`** :
   - Prend un paramètre `utilisateur` (type `Utilisateur`) et `ctx: Context`
   - Simule l'ajout d'un utilisateur (stocke dans une liste en mémoire)
   - Retourne l'utilisateur avec son ID assigné
   - Logge avec `ctx.info()`

4. **Crée l'outil `lister_utilisateurs`** :
   - Prend `ctx: Context`
   - Prend un paramètre optionnel `tag_filtre` : str | None
   - Si `tag_filtre` est fourni, retourne seulement les utilisateurs ayant ce tag
   - Sinon, retourne tous les utilisateurs
   - Retourne `List[Utilisateur]`
   - Logge avec `ctx.info()`

5. **Crée l'outil `obtenir_statistiques`** :
   - Prend `ctx: Context`
   - Retourne `StatistiquesUtilisateurs`
   - Calcule le total, les stats par tag, et le score moyen
   - Logge avec `ctx.info()`

## Indices

- Utilise `from typing import List, Dict, Optional`
- Pour stocker les utilisateurs, utilise une liste globale : `utilisateurs = []`
- Pour compter par tag, itère sur les utilisateurs et leurs tags
- Pour calculer la moyenne : `sum(u.score for u in utilisateurs) / len(utilisateurs)` si la liste n'est pas vide

## Test

Utilise `python test.py` pour vérifier que :
- Les modèles fonctionnent avec des listes
- Les outils manipulent correctement les données complexes
- Les filtres fonctionnent

## Résultat attendu

- Ajouter plusieurs utilisateurs avec différents tags
- Lister tous les utilisateurs
- Filtrer par tag
- Obtenir les statistiques