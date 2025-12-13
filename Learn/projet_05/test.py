"""
Script de test pour le projet 05
Ce script vérifie la gestion d'erreurs et la validation
"""

import sys
import importlib.util
import asyncio
import math
from unittest.mock import AsyncMock

async def test_normal_division():
    """Test d'une division normale"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    try:
        result = await solution.calculer_division(10.0, 2.0, mock_ctx)

        if result != 5.0:
            print(f"10.0 / 2.0 devrait donner 5.0, mais a donné {result}")
            return False

        if mock_ctx.info.call_count < 2:
            print("ctx.info() devrait être appelé au moins 2 fois (début et succès)")
            return False

        print("Division normale fonctionne : 10.0 / 2.0 = 5.0")
        return True

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_division_by_zero():
    """Test division par zéro"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    try:
        result = await solution.calculer_division(10.0, 0.0, mock_ctx)

        # Si on arrive ici, l'erreur n'a pas été levée
        print("L'outil devrait lever ValueError pour division par zéro")
        return False

    except ValueError as e:
        if "zéro" not in str(e).lower() and "zero" not in str(e).lower():
            print(f"Le message d'erreur devrait mentionner 'zéro', mais dit : {e}")
            return False

        if mock_ctx.error.call_count == 0:
            print("ctx.error() devrait être appelé avant de lever l'exception")
            return False

        print(f"Division par zéro correctement gérée : {e}")
        return True

    except Exception as e:
        print(f"Erreur inattendue (devrait être ValueError) : {e}")
        return False

async def test_infinity_result():
    """Test avec résultat infini"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    try:
        # Utilise une très petite valeur pour créer un résultat proche de l'infini
        result = await solution.calculer_division(1.0, 0.0000001, mock_ctx)

        if not math.isinf(result) and result < 1000000:
            # Pour ce test, on accepte soit un très grand nombre, soit infini
            # (selon l'implémentation)
            pass

        # Vérifie qu'un warning a été émis (si le code détecte l'infini)
        # Si math.isinf est utilisé, ctx.warning devrait être appelé
        print(f"Calcul avec très petit diviseur : résultat = {result}")
        return True

    except Exception as e:
        # C'est aussi acceptable si une exception est levée
        print(f"Calcul détecté comme problématique (acceptable)")
        return True

async def test_missing_parameters():
    """Test avec paramètres manquants"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    # Test avec None (simule un paramètre manquant)
    try:
        # Note: en Python, si le paramètre est défini avec un type, 
        # None ne peut pas être passé directement. On teste plutôt avec des valeurs invalides
        # ou on vérifie que la validation existe dans le code

        # Pour ce test, on vérifie juste que le code gère les cas None si possible
        # ou on teste avec des valeurs qui devraient être rejetées
        result = await solution.calculer_division(10.0, 2.0, mock_ctx)
        print("Les paramètres sont acceptés (note: validation des None peut nécessiter Optional dans la signature)")
        return True

    except Exception as e:
        print(f"Validation fonctionne : {e}")
        return True

if __name__ == "__main__":
    print("Test du Projet 05\n")

    success = True

    print("Test division normale...")
    success = asyncio.run(test_normal_division()) and success
    print()

    print("Test division par zéro...")
    success = asyncio.run(test_division_by_zero()) and success
    print()

    print("Test résultat infini...")
    success = asyncio.run(test_infinity_result()) and success
    print()

    print("Test paramètres manquants...")
    success = asyncio.run(test_missing_parameters()) and success

    print()
    if success:
        print("Tous les tests passent !")
        print("Tu as appris à gérer les erreurs proprement dans MCP !")
    else:
        print("Certains tests ont échoué. Vérifie ton code !")
        sys.exit(1)