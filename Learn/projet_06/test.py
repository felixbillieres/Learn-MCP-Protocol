"""
Script de test pour le projet 06
Ce script vérifie les outils avec paramètres complexes
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_models_exist():
    """Test que les modèles existent"""

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
    if not hasattr(solution, 'Utilisateur'):
        print("Le modèle 'Utilisateur' n'existe pas")
        return False

    if not hasattr(solution, 'StatistiquesUtilisateurs'):
        print("Le modèle 'StatistiquesUtilisateurs' n'existe pas")
        return False

    print("Les modèles existent")
    return True

def test_utilisateur_model():
    """Test que le modèle Utilisateur fonctionne"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        # Test création avec tous les champs
        user = solution.Utilisateur(
            id=1,
            nom="Alice",
            email="alice@example.com",
            tags=["admin", "premium"],
            score=95.5
        )

        if user.nom != "Alice":
            print("Le nom n'est pas correctement assigné")
            return False

        if user.score != 95.5:
            print("Le score n'est pas correctement assigné")
            return False

        # Test avec valeurs par défaut
        user2 = solution.Utilisateur(
            id=2,
            nom="Bob",
            tags=[]
        )

        if user2.score != 0.0:
            print(f"Le score par défaut devrait être 0.0, mais c'est {user2.score}")
            return False

        print("Le modèle Utilisateur fonctionne correctement")
        return True

    except Exception as e:
        print(f"Erreur lors de la création du modèle : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_ajouter_utilisateur():
    """Test l'outil ajouter_utilisateur"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Réinitialise la liste
    if hasattr(solution, 'utilisateurs'):
        solution.utilisateurs.clear()

    mock_ctx = AsyncMock()

    user = solution.Utilisateur(
        id=1,
        nom="Alice",
        tags=["admin"]
    )

    try:
        result = await solution.ajouter_utilisateur(user, mock_ctx)

        if not isinstance(result, solution.Utilisateur):
            print(f"Le résultat devrait être un Utilisateur, mais c'est {type(result)}")
            return False

        if len(solution.utilisateurs) != 1:
            print(f"L'utilisateur devrait être ajouté, mais la liste contient {len(solution.utilisateurs)} éléments")
            return False

        print("ajouter_utilisateur fonctionne")
        return True

    except Exception as e:
        print(f"Erreur lors de l'ajout : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_lister_utilisateurs():
    """Test l'outil lister_utilisateurs"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Réinitialise et ajoute des utilisateurs
    if hasattr(solution, 'utilisateurs'):
        solution.utilisateurs.clear()

    mock_ctx = AsyncMock()

    # Ajoute quelques utilisateurs
    user1 = solution.Utilisateur(id=1, nom="Alice", tags=["admin", "premium"])
    user2 = solution.Utilisateur(id=2, nom="Bob", tags=["user"])
    user3 = solution.Utilisateur(id=3, nom="Charlie", tags=["admin"])

    await solution.ajouter_utilisateur(user1, mock_ctx)
    await solution.ajouter_utilisateur(user2, mock_ctx)
    await solution.ajouter_utilisateur(user3, mock_ctx)

    try:
        # Liste tous
        tous = await solution.lister_utilisateurs(mock_ctx, None)
        if len(tous) != 3:
            print(f"Devrait retourner 3 utilisateurs, mais a retourné {len(tous)}")
            return False

        # Filtre par tag
        admins = await solution.lister_utilisateurs(mock_ctx, "admin")
        if len(admins) != 2:
            print(f"Devrait retourner 2 admins, mais a retourné {len(admins)}")
            return False

        print("lister_utilisateurs fonctionne avec filtrage")
        return True

    except Exception as e:
        print(f"Erreur lors de la liste : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_obtenir_statistiques():
    """Test l'outil obtenir_statistiques"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Réinitialise et ajoute des utilisateurs
    if hasattr(solution, 'utilisateurs'):
        solution.utilisateurs.clear()

    mock_ctx = AsyncMock()

    # Ajoute des utilisateurs avec différents scores et tags
    await solution.ajouter_utilisateur(
        solution.Utilisateur(id=1, nom="Alice", tags=["admin"], score=90.0),
        mock_ctx
    )
    await solution.ajouter_utilisateur(
        solution.Utilisateur(id=2, nom="Bob", tags=["user"], score=80.0),
        mock_ctx
    )
    await solution.ajouter_utilisateur(
        solution.Utilisateur(id=3, nom="Charlie", tags=["admin"], score=95.0),
        mock_ctx
    )

    try:
        stats = await solution.obtenir_statistiques(mock_ctx)

        if not isinstance(stats, solution.StatistiquesUtilisateurs):
            print(f"Le résultat devrait être StatistiquesUtilisateurs, mais c'est {type(stats)}")
            return False

        if stats.total != 3:
            print(f"Le total devrait être 3, mais c'est {stats.total}")
            return False

        if stats.score_moyen != (90.0 + 80.0 + 95.0) / 3:
            print(f"Le score moyen devrait être ~88.33, mais c'est {stats.score_moyen}")
            return False

        if "admin" not in stats.par_tag or stats.par_tag["admin"] != 2:
            print(f"Il devrait y avoir 2 admins, mais par_tag dit : {stats.par_tag}")
            return False

        print(f"obtenir_statistiques fonctionne : total={stats.total}, moyenne={stats.score_moyen:.2f}")
        return True

    except Exception as e:
        print(f"Erreur lors des statistiques : {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test du Projet 06\n")

    success = True
    success = test_models_exist() and success
    print()

    success = test_utilisateur_model() and success
    print()

    print("Test ajouter_utilisateur...")
    success = asyncio.run(test_ajouter_utilisateur()) and success
    print()

    print("Test lister_utilisateurs...")
    success = asyncio.run(test_lister_utilisateurs()) and success
    print()

    print("Test obtenir_statistiques...")
    success = asyncio.run(test_obtenir_statistiques()) and success

    print()
    if success:
        print("Tous les tests passent !")
        print("Tu as appris à gérer des types complexes dans MCP !")
    else:
        print("Certains tests ont échoué. Vérifie ton code !")
        sys.exit(1)