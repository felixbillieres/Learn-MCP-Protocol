# Projet 12 : Prompts avec arguments dynamiques

## Objectif

Apprendre à créer des prompts qui acceptent des arguments dynamiques pour personnaliser le contenu.

## Concepts à apprendre

### Arguments dans les prompts

Les prompts peuvent accepter des **arguments** qui permettent de personnaliser le message retourné. Par exemple, un prompt de code review peut accepter un argument `language` pour adapter le message.

### Structure des arguments

Chaque argument a :
- `name` : Nom de l'argument
- `description` : Description (optionnel)
- `required` : Si l'argument est obligatoire (optionnel, défaut false)

### Utilisation

Quand un client demande un prompt avec `prompts/get`, il peut passer un dict `arguments` avec les valeurs des arguments.

## Ce que tu vas créer

Dans ce projet, tu vas créer des prompts qui utilisent des arguments pour personnaliser le contenu.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

