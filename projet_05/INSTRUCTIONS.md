# Instructions - Projet 05

## Ta mission

Créer un outil avec une gestion d'erreurs robuste et une validation des données.

## Étapes à suivre

1. **Crée un outil `calculer_division`** qui :
   - Prend deux paramètres : `dividende` (float) et `diviseur` (float)
   - Prend aussi `ctx: Context`
   - Divise le dividende par le diviseur

2. **Validations à implémenter** :
   - Si `dividende` est None ou non fourni → `ctx.error()` + `raise ValueError("Le dividende est requis")`
   - Si `diviseur` est None ou non fourni → `ctx.error()` + `raise ValueError("Le diviseur est requis")`
   - Si `diviseur == 0` → `ctx.error()` + `raise ValueError("Division par zéro impossible")`
   - Si le résultat est infini → `ctx.warning()` (mais retourne quand même le résultat)

3. **Logging** :
   - Au début : `ctx.info()` : "Calcul de {dividende} / {diviseur}"
   - En cas de succès : `ctx.info()` : "Résultat : {resultat}"
   - En cas d'erreur : logger avec `ctx.error()` avant de lever l'exception

4. **Retourne** : un float (le résultat de la division)

## Indices

- Valide les paramètres **avant** de faire le calcul
- Utilise `math.isinf()` pour vérifier si le résultat est infini
- Les messages d'erreur doivent être clairs et informatifs
- Toujours logger avec `ctx.error()` avant de lever une exception

## Test

Utilise `python test.py` pour vérifier que :
- Les validations fonctionnent
- Les erreurs sont bien gérées
- Les messages sont clairs

## Résultat attendu

- Division normale : retourne le résultat
- Division par zéro : lève ValueError avec message clair
- Paramètres manquants : lève ValueError avec message clair
- Tous les cas sont loggés dans le Context