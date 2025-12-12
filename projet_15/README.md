# Projet 15 : Elicitation avec schémas JSON

## Objectif

Apprendre à créer des schémas JSON détaillés pour l'elicitation, avec validation et contraintes.

## Concepts à apprendre

### Schémas JSON pour l'elicitation

Les schémas permettent de définir précisément la structure des données demandées :
- Types de données (string, number, boolean, enum)
- Contraintes (minLength, maxLength, pattern, minimum, maximum)
- Formats (email, uri, date, date-time)
- Valeurs par défaut
- Champs requis vs optionnels

### Structure d'un schéma

Un schéma d'elicitation est un objet JSON Schema avec :
- `type: "object"` pour la racine
- `properties` : Définition des champs
- `required` : Liste des champs obligatoires

### Types supportés

1. **String** : avec minLength, maxLength, pattern, format
2. **Number/Integer** : avec minimum, maximum
3. **Boolean** : vrai/faux
4. **Enum** : liste de valeurs possibles (avec `enum` ou `oneOf`)

## Ce que tu vas créer

Dans ce projet, tu vas créer des schémas d'elicitation complexes avec validation.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

