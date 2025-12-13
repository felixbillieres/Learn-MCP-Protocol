# Projet 18 : Sampling avancé avec préférences et paramètres

## Objectif

Apprendre à utiliser les préférences de modèle et les paramètres avancés du sampling.

## Concepts à apprendre

### Préférences de modèle

Les serveurs peuvent suggérer des préférences pour le choix du modèle :
- `hints` : Suggestions de modèles (ex: "claude-3-sonnet")
- `intelligencePriority` : Priorité sur les capacités (0-1)
- `speedPriority` : Priorité sur la vitesse (0-1)
- `costPriority` : Priorité sur le coût (0-1)

### Paramètres de sampling

- `temperature` : Créativité (0-2)
- `max_tokens` : Nombre maximum de tokens
- `stop_sequences` : Séquences qui arrêtent la génération

### Messages multiples

On peut envoyer plusieurs messages pour créer une conversation avec contexte.

## Ce que tu vas créer

Dans ce projet, tu vas créer des outils qui utilisent les paramètres avancés du sampling.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

