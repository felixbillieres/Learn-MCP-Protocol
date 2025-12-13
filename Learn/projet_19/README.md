# Projet 19 : Sampling avec outils et workflows agentiques

## Objectif

Apprendre à utiliser le sampling avec des outils pour créer des workflows agentiques où le LLM peut appeler des fonctions.

## Concepts à apprendre

### Sampling avec outils

Le sampling peut inclure des outils que le LLM peut utiliser pendant la génération. Cela permet de créer des agents qui peuvent :
- Appeler des fonctions
- Recevoir des résultats
- Continuer le raisonnement
- Itérer jusqu'à résoudre la tâche

### Flow agentique

1. Serveur envoie une requête avec outils disponibles
2. LLM décide d'appeler un outil
3. Client exécute l'outil
4. Client retourne le résultat au LLM
5. LLM continue avec le résultat
6. Répète jusqu'à ce que le LLM termine

### Déclaration des outils

Les outils sont déclarés dans la requête de sampling avec :
- `name` : Nom de l'outil
- `description` : Description
- `inputSchema` : Schéma JSON des paramètres

## Ce que tu vas créer

Dans ce projet, tu vas créer un workflow agentique où le LLM peut utiliser des outils pour résoudre des tâches complexes.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !

