"""
Script de test pour le projet 04
Ce script vérifie que le Context est bien utilisé pour le logging
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_context_import():
    """Test que Context est importé"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Erreur lors de l'import : {e}")
        import traceback
        traceback.print_exc()
        return False

    # Vérifie que Context est disponible
    try:
        from mcp.server.fastmcp import Context
        print("Context est bien importable")
    except ImportError:
        print("Impossible d'importer Context")
        return False

    return True

async def test_tool_with_context():
    """Test que l'outil utilise bien le Context"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Crée un mock Context
    mock_ctx = AsyncMock()

    # Test avec un fichier valide
    try:
        result = await solution.traiter_fichier("test.txt", mock_ctx)

        # Vérifie que ctx.info a été appelé
        if mock_ctx.info.call_count < 2:
            print(f"ctx.info() devrait être appelé au moins 2 fois, mais a été appelé {mock_ctx.info.call_count} fois")
            return False

        # Vérifie que le résultat est un dict
        if not isinstance(result, dict):
            print(f"Le résultat devrait être un dict, mais c'est {type(result)}")
            return False

        # Vérifie les clés du résultat
        if "fichier" not in result or "statut" not in result:
            print(f"Le résultat devrait contenir 'fichier' et 'statut'")
            return False

        print(f"L'outil fonctionne avec Context ! Résultat : {result}")
        print(f"  ctx.info() appelé {mock_ctx.info.call_count} fois")

    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

async def test_tool_with_warning():
    """Test que l'outil utilise ctx.warning() quand nécessaire"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    # Test avec un fichier non-.txt (devrait générer un warning)
    try:
        result = await solution.traiter_fichier("test.pdf", mock_ctx)

        # Vérifie que ctx.warning a été appelé
        if mock_ctx.warning.call_count == 0:
            print("ctx.warning() devrait être appelé pour un fichier non-.txt")
            return False

        print("ctx.warning() est bien utilisé pour les fichiers non-.txt")

    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")
        return False

    return True

async def test_tool_with_error():
    """Test que l'outil utilise ctx.error() et lève une exception"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    # Test avec le fichier "erreur.txt" (devrait générer une erreur)
    try:
        result = await solution.traiter_fichier("erreur.txt", mock_ctx)

        # Si on arrive ici, l'erreur n'a pas été levée
        print("L'outil devrait lever une ValueError pour 'erreur.txt'")
        return False

    except ValueError:
        # C'est ce qu'on attend !
        # Vérifie que ctx.error a été appelé
        if mock_ctx.error.call_count == 0:
            print("ctx.error() devrait être appelé avant de lever l'exception")
            return False

        print("ctx.error() est bien utilisé et l'exception est levée correctement")
        return True

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test du Projet 04\n")

    success = True
    success = test_context_import() and success
    print()

    print("Test d'exécution avec Context...")
    success = asyncio.run(test_tool_with_context()) and success
    print()

    print("Test avec warning...")
    success = asyncio.run(test_tool_with_warning()) and success
    print()

    print("Test avec error...")
    success = asyncio.run(test_tool_with_error()) and success

    print()
    if success:
        print("Tous les tests passent !")
        print("Tu as appris à utiliser le Context pour le logging !")
    else:
        print("Certains tests ont échoué. Vérifie ton code !")
        sys.exit(1)