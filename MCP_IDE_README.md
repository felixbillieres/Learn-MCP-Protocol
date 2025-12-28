# 🚀 MCP Learning IDE

Une interface terminal interactive pour naviguer dans votre parcours d'apprentissage MCP, visualiser les exercices, exécuter des tests et suivre votre progression.

## ✨ Fonctionnalités

### 🧭 Navigation Structurée
- **Navigation par catégories** : Learn (01-25), Offensive (26-32), Defensive (33-40)
- **Vue d'ensemble** : Liste de tous les projets avec statut de progression
- **Exploration détaillée** : Accès aux fichiers MCP et exercices Python

### 📖 Visualisation du Code
- **Lecteur de code intégré** : Syntax highlighting pour Python
- **Navigation dans les fichiers** : Instructions, solutions, exercices Python
- **Affichage paginé** : Contenu lisible même pour les fichiers longs

### 🧪 Exécution de Tests
- **Tests individuels** : Exécution de tests spécifiques par projet
- **Tests en lot** : Exécution de tous les tests disponibles
- **Rapports détaillés** : Résultats avec output complet des tests

### 📊 Suivi de Progression
- **Système de completion** : Marquer les exercices comme terminés
- **Tableaux de bord** : Vue d'ensemble de la progression
- **Persistance** : Sauvegarde automatique dans `.mcp_progress.json`

## 🚀 Démarrage Rapide

### Prérequis
```bash
pip3 install rich
```

### Lancement
```bash
cd /path/to/learn-mcp-protocol
python3 mcp_ide.py
```

## 🎮 Utilisation

### Menu Principal
```
1. Browse MCP Projects (Learn 01-25)     # Projets fondamentaux
2. Browse Offensive Projects (26-32)      # Cybersécurité offensive
3. Browse Defensive Projects (33-40)      # Cybersécurité défensive
4. View Progress Details                   # Détails de progression
5. Run All Tests                          # Exécuter tous les tests
6. Exit                                   # Quitter
```

### Navigation dans un Projet
Une fois un projet sélectionné :
```
1. View MCP Instructions      # Voir les instructions du projet MCP
2. View MCP Solution         # Voir la solution MCP
3. View Python Exercise Code # Explorer les exercices Python
4. Run Python Tests          # Exécuter les tests Python
5. Mark MCP as Completed     # Marquer le projet MCP comme terminé
6. Mark Python Exercise as Completed  # Marquer l'exercice Python comme terminé
7. Back to Project List      # Retour à la liste des projets
```

## 📁 Structure des Fichiers

```
learn-mcp-protocol/
├── mcp_ide.py                    # Interface principale
├── .mcp_progress.json           # Sauvegarde de progression (auto-généré)
├── Learn/                       # Projets Learn (01-25)
│   └── projet_01/
│       ├── INSTRUCTIONS.md      # Instructions du projet MCP
│       ├── solution.py          # Solution MCP
│       └── python_exercises/    # Exercices Python préparatoires
│           ├── exercise_01.py   # Code de l'exercice
│           ├── test_exercise_01.py  # Tests de validation
│           └── README.md        # Guide pédagogique
├── Offensive/                   # Projets Offensive (26-32)
└── Defensive/                   # Projets Defensive (33-40)
```

## 🎯 Workflow d'Apprentissage

### 1. Découverte
- Lancez l'IDE et explorez les projets disponibles
- Lisez les instructions MCP pour comprendre l'objectif
- Consultez les exercices Python préparatoires

### 2. Pratique
- Implémentez les exercices Python pour maîtriser les concepts
- Exécutez les tests pour valider votre compréhension
- Marquer comme terminé une fois réussi

### 3. Application
- Implémentez la solution MCP selon les instructions
- Comparez avec la solution fournie si nécessaire
- Marquer le projet MCP comme terminé

### 4. Progression
- Suivez votre avancement dans "View Progress Details"
- Utilisez "Run All Tests" pour un bilan général
- Célébrez vos progrès ! 🎉

## 🛠️ Fonctionnalités Avancées

### Système de Progression
- **Persistance automatique** : Sauvegarde dans `.mcp_progress.json`
- **Statuts visuels** : ✅ terminé, ❌ non commencé, ⟳ partiel
- **Métriques globales** : Comptage des exercices terminés

### Interface Utilisateur
- **Couleurs riches** : Syntax highlighting et thèmes adaptés
- **Navigation intuitive** : Menus numérotés et confirmations
- **Gestion d'erreurs** : Messages d'erreur informatifs
- **Interruption propre** : Ctrl+C pour quitter gracieusement

### Tests et Validation
- **Timeout de sécurité** : 30 secondes max par test
- **Capture complète** : stdout et stderr
- **Rapports détaillés** : Output complet pour le debugging
- **Statuts clairs** : ✅ succès, ❌ échec

## 🔧 Personnalisation

### Modifier les Couleurs
Editez les styles Rich dans `mcp_ide.py` :
```python
# Exemples de personnalisation
console.print("[bold magenta]Texte en magenta gras[/bold magenta]")
table.add_column("Colonne", style="cyan")  # Colonne en cyan
```

### Étendre les Fonctionnalités
La classe `MCPLearningIDE` est modulaire. Ajoutez des méthodes pour :
- Support de nouveaux types de fichiers
- Intégration avec des outils externes
- Nouvelles visualisations de progression
- Export de rapports de progression

## 🐛 Dépannage

### Interface Non Fonctionnelle
```bash
# Vérifier l'installation de rich
python3 -c "import rich; print('OK')"

# Installer si nécessaire
pip3 install rich
```

### Tests Qui Ne Fonctionnent Pas
- Vérifiez que les fichiers `test_*.py` existent
- Assurez-vous que Python 3 est disponible
- Vérifiez les permissions d'exécution

### Progression Non Sauvegardée
- Le fichier `.mcp_progress.json` doit être accessible en écriture
- Les modifications sont sauvegardées automatiquement

## 🎓 Exemple de Session

```
🚀 MCP Learning IDE

📊 Learning Progress
┌──────────────┬───────────┬───────┐
│ Category     │ Completed │ Total │
├──────────────┼───────────┼───────┤
│ All Exercises│ 0         │ 80    │
└──────────────┴───────────┴───────┘

1. Browse MCP Projects (Learn 01-25)
2. Browse Offensive Projects (26-32)
3. Browse Defensive Projects (33-40)
4. View Progress Details
5. Run All Tests
6. Exit

Choose an option: 1

📚 Learn Projects (01-25)
┌─────────┬─────┬────────┬─────────────┐
│ Project │ MCP │ Python │ Status      │
├─────────┼─────┼────────┼─────────────┤
│ projet_01│ ✅ │ ✅    │ ○ Not Started│
└─────────┴─────┴────────┴─────────────┘

Enter project name to explore (or 'back' to return): projet_01

Exploring: projet_01
Path: Learn/projet_01

📄 MCP Files (3): INSTRUCTIONS.md, README.md, solution.py
🐍 Python Exercises (2): exercise_01.py, test_exercise_01.py

1. View MCP Instructions
2. View MCP Solution
3. View Python Exercise Code
4. Run Python Tests
5. Mark MCP as Completed
6. Mark Python Exercise as Completed
7. Back to Project List

Choose an option: 4

Available test files:
1. test_exercise_01.py

Choose test to run: 1

Running: test_exercise_01.py
✅ Test passed!

Test Output:
All tests passed! You're ready for MCP Project 01!
```

## 🤝 Contribution

L'interface est conçue pour être extensible. N'hésitez pas à :
- Ajouter de nouvelles fonctionnalités
- Améliorer l'UX/UI
- Corriger des bugs
- Partager des améliorations

---

**Bon apprentissage avec MCP ! 🎓**
