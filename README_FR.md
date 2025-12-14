# Apprentissage MCP en Python

Bienvenue dans ce guide d'apprentissage progressif pour comprendre le Model Context Protocol (MCP) en Python.

## Structure d'apprentissage

Ce dépôt contient **40 mini-projets progressifs** qui te permettront de maîtriser MCP du niveau débutant au niveau avancé, avec des spécialisations en cybersécurité offensive et défensive.

Les projets sont organisés en trois catégories :
- **Learn** (Projets 01-25) : Concepts fondamentaux de MCP
- **Offensive** (Projets 26-32) : Outils et techniques de sécurité offensive
- **Defensive** (Projets 33-40) : Outils défensifs et réponse aux incidents

## Parcours d'apprentissage

### Projets - Niveau Débutant (01-07)

1. **Projet 01** - Créer un serveur MCP basique avec FastMCP
2. **Projet 02** - Ajouter un premier outil (tool) simple
3. **Projet 03** - Utiliser les modèles Pydantic pour structurer les données
4. **Projet 04** - Utiliser le Context pour le logging (info, error, warning)
5. **Projet 05** - Gestion d'erreurs et validation
6. **Projet 06** - Outils avec paramètres complexes et types avancés
7. **Projet 07** - Projet final débutant : Mini serveur complet

### Projets - Resources (08-10)

8. **Projet 08** - Créer ta première ressource (exposer des données)
9. **Projet 09** - Resources avec templates et URIs dynamiques
10. **Projet 10** - Resources avancées : subscriptions et notifications

### Projets - Prompts (11-13)

11. **Projet 11** - Créer ton premier prompt (template de message)
12. **Projet 12** - Prompts avec arguments dynamiques
13. **Projet 13** - Prompts avancés : chaînage et workflows complexes

### Projets - Elicitation (14-16)

14. **Projet 14** - Utiliser l'elicitation pour demander des informations
15. **Projet 15** - Elicitation avec schémas JSON et validation
16. **Projet 16** - Elicitation URL mode pour les interactions sensibles

### Projets - Sampling (17-19)

17. **Projet 17** - Utiliser le sampling pour demander des complétions LLM
18. **Projet 18** - Sampling avec préférences de modèle et paramètres
19. **Projet 19** - Sampling avancé : workflows agentiques complexes

### Projets - Authorization & Security (20-22)

20. **Projet 20** - Introduction à l'autorisation OAuth 2.1
21. **Projet 21** - Implémenter l'authentification avec tokens
22. **Projet 22** - Sécurité avancée : validation des audiences et scopes

### Projets - Concepts Avancés (23-25)

23. **Projet 23** - Utiliser Roots pour définir les limites d'accès
24. **Projet 24** - Transports personnalisés et optimisations
25. **Projet 25** - PROJET FINAL AVANCÉ : Serveur MCP complet avec toutes les fonctionnalités

### Projets - Sécurité Offensive (26-32)

26. **Projet 26** - Scanner de Ports MCP : Scanner les ports et analyser les services
27. **Projet 27** - Gestionnaire de Payloads : Gérer les exploits, shells et shellcodes
28. **Projet 28** - Analyseur de Vulnérabilités : Analyser les CVE et générer des advisories
29. **Projet 29** - Gestionnaire de Sessions Pentest : Gérer les sessions d'exploitation
30. **Projet 30** - Framework d'Exploitation : Chaîner les exploits avec payloads intelligents
31. **Projet 31** - Gestionnaire C2 : Simulation de serveur Command & Control
32. **Projet 32** - Automatisation de Pentest : Orchestrer des workflows de pentest complets

### Projets - Sécurité Défensive (33-40)

33. **Projet 33** - SIEM MCP : Security Information and Event Management
34. **Projet 34** - Gestionnaire d'Incidents : Gérer les incidents de sécurité avec triage
35. **Projet 35** - Analyseur de Malware : Analyser les fichiers suspects et générer des règles YARA
36. **Projet 36** - Gestionnaire de Patchs : Suivre et déployer les patchs de sécurité
37. **Projet 37** - Gestionnaire de Règles Firewall : Gérer les règles firewall avec validation
38. **Projet 38** - Détecteur d'Anomalies : Détecter les anomalies avec baselines et ML
39. **Projet 39** - Gestionnaire de Secrets : Gérer de manière sécurisée mots de passe, tokens et clés
40. **Projet 40** - PROJET FINAL AVANCÉ : Plateforme de sécurité complète (offensive + défensive)

## Structure du dépôt

Le dépôt est organisé en trois répertoires principaux :

```
Learn/
├── projet_01/       # Projets d'apprentissage MCP (01-25)
├── projet_02/
└── ...

Offensive/
├── projet_26/       # Projets sécurité offensive (26-32)
├── projet_27/
└── ...

Defensive/
├── projet_33/       # Projets sécurité défensive (33-40)
├── projet_34/
└── ...
```

## Comment utiliser ces projets

Pour chaque projet :

1. **Lis** le fichier `README.md` pour comprendre la théorie
2. **Lis** le fichier `INSTRUCTIONS.md` pour voir ce que tu dois faire
3. **Écris** ton code dans `solution.py` (fichier à compléter)
4. **Teste** avec `test.py` pour vérifier que ça fonctionne
5. **Demande-moi de corriger** si tu as besoin d'aide !

## Prérequis

- Python 3.10+
- Compréhension basique de Python (fonctions, classes, imports)
- Aucune connaissance de MCP requise (on apprend tout ici !)

## Installation

```bash
pip install mcp pydantic
```

Ou avec `uv` :

```bash
uv pip install mcp pydantic
```

## Objectifs d'apprentissage

À la fin de ces projets, tu sauras :

- ✅ Créer un serveur MCP avec FastMCP
- ✅ Déclarer et implémenter des outils (tools)
- ✅ Utiliser Pydantic pour valider les données
- ✅ Gérer les logs et le contexte
- ✅ Gérer les erreurs proprement
- ✅ Structurer un projet MCP professionnellement
- ✅ **Outils sécurité offensive** : Scan de ports, exploitation, gestion C2
- ✅ **Outils sécurité défensive** : SIEM, réponse aux incidents, analyse malware
- ✅ **Plateformes de sécurité complètes** : Combiner capacités offensive et défensive

## Statut des traductions

**Note :**
- **Projets Learn (01-25)** : Documentation en français (README.md et INSTRUCTIONS.md)
- **Projets Offensive (26-32)** : Documentation en anglais
- **Projets Defensive (33-40)** : Documentation en anglais

Le code, les fichiers de test et les noms de variables utilisent les conventions anglaises dans tous les projets.

## Notes importantes

- Les projets sont **progressifs** : commence par le 01 et avance dans l'ordre
- Chaque projet reprend les concepts des projets précédents
- N'hésite pas à regarder des implémentations MCP réelles pour référence
- Je suis là pour t'aider et corriger tes solutions !

## Ressources

- [Spécification MCP](https://modelcontextprotocol.io)
- [Documentation FastMCP](https://github.com/jlowin/fastmcp)
- [Documentation Pydantic](https://docs.pydantic.dev)

---

**Bonne chance !**
