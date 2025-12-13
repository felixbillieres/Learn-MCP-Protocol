"""
Script de test pour le projet 07 (PROJET FINAL)
Ce script teste toutes les fonctionnalités du gestionnaire de tâches
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_basic_structure():
    """Test que la structure de base est correcte"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Erreur lors de l'import : {e}")
        import traceback
        traceback.print_exc()
        return False

    # Vérifie les modèles
    if not hasattr(solution, 'Tache'):
        print("Le modèle 'Tache' n'existe pas")
        return False

    if not hasattr(solution, 'StatistiquesTaches'):
        print("Le modèle 'StatistiquesTaches' n'existe pas")
        return False

    # Vérifie la liste
    if not hasattr(solution, 'taches'):
        print("La liste 'taches' n'existe pas")
        return False

    print("Structure de base correcte")
    return True

async def test_creer_tache():
    """Test création de tâche"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Réinitialise
    solution.taches.clear()
    mock_ctx = AsyncMock()

    try:
        result = await solution.creer_tache(
            titre="Ma première tâche",
            description="Description de test",
            priorite="haute",
            tags=["test", "important"],
            ctx=mock_ctx
        )

        if not isinstance(result, solution.Tache):
            print(f"Le résultat devrait être une Tache, mais c'est {type(result)}")
            return False

        if result.titre != "Ma première tâche":
            print("Le titre n'est pas correct")
            return False

        if len(solution.taches) != 1:
            print(f"La tâche devrait être ajoutée, mais la liste contient {len(solution.taches)} éléments")
            return False

        print("creer_tache fonctionne")
        return True

    except Exception as e:
        print(f"Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_lister_taches():
    """Test liste et filtres"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    solution.taches.clear()
    mock_ctx = AsyncMock()

    # Crée quelques tâches
    t1 = await solution.creer_tache("Tâche 1", None, "haute", ["a"], mock_ctx)
    t2 = await solution.creer_tache("Tâche 2", None, "normale", ["b"], mock_ctx)
    t3 = await solution.creer_tache("Tâche 3", None, "haute", ["a"], mock_ctx)

    await solution.marquer_termine(t1.id, True, mock_ctx)

    try:
        # Liste toutes
        toutes = await solution.lister_taches(None, None, None, mock_ctx)
        if len(toutes) != 3:
            print(f"Devrait retourner 3 tâches, mais a retourné {len(toutes)}")
            return False

        # Filtre par terminé
        terminees = await solution.lister_taches(True, None, None, mock_ctx)
        if len(terminees) != 1:
            print(f"Devrait retourner 1 tâche terminée, mais a retourné {len(terminees)}")
            return False

        # Filtre par priorité
        hautes = await solution.lister_taches(None, "haute", None, mock_ctx)
        if len(hautes) != 2:
            print(f"Devrait retourner 2 tâches haute priorité, mais a retourné {len(hautes)}")
            return False

        # Filtre par tag
        tag_a = await solution.lister_taches(None, None, "a", mock_ctx)
        if len(tag_a) != 2:
            print(f"Devrait retourner 2 tâches avec tag 'a', mais a retourné {len(tag_a)}")
            return False

        print("lister_taches avec filtres fonctionne")
        return True

    except Exception as e:
        print(f"Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_statistiques():
    """Test statistiques"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    solution.taches.clear()
    mock_ctx = AsyncMock()

    # Crée des tâches variées
    t1 = await solution.creer_tache("T1", None, "haute", ["a"], mock_ctx)
    t2 = await solution.creer_tache("T2", None, "haute", ["b"], mock_ctx)
    t3 = await solution.creer_tache("T3", None, "normale", ["a"], mock_ctx)

    await solution.marquer_termine(t1.id, True, mock_ctx)

    try:
        stats = await solution.obtenir_statistiques(mock_ctx)

        if stats.total != 3:
            print(f"Total devrait être 3, mais c'est {stats.total}")
            return False

        if stats.terminees != 1:
            print(f"Terminées devrait être 1, mais c'est {stats.terminees}")
            return False

        if stats.par_priorite.get("haute", 0) != 2:
            print(f"Devrait avoir 2 tâches haute priorité, mais c'est {stats.par_priorite}")
            return False

        print("obtenir_statistiques fonctionne")
        return True

    except Exception as e:
        print(f"Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test du Projet 07 (FINAL)\n")

    success = True
    success = test_basic_structure() and success
    print()

    print("Test création de tâche...")
    success = asyncio.run(test_creer_tache()) and success
    print()

    print("Test liste et filtres...")
    success = asyncio.run(test_lister_taches()) and success
    print()

    print("Test statistiques...")
    success = asyncio.run(test_statistiques()) and success

    print()
    if success:
        print("FÉLICITATIONS ! Tous les tests passent !")
        print("Tu as terminé tous les projets et maîtrisé MCP en Python !")
    else:
        print("Certains tests ont échoué. Vérifie ton code !")
        sys.exit(1)