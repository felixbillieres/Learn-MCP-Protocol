"""
Script de test pour le projet 10
Note: Les subscriptions sont difficiles à tester sans un vrai client MCP
Ce test vérifie la structure de base
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

async def test_list_resources():
    """Test que list_resources fonctionne"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.list_resources()
        if not isinstance(result, list):
            print("list_resources devrait retourner une liste")
            return False
        print("list_resources fonctionne")
        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False

async def test_update_status():
    """Test que update_status fonctionne"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    try:
        result = await solution.update_status("stopped", 100, mock_ctx)

        # Vérifie que le status a été mis à jour
        if solution.status_content["status"] != "stopped":
            print("Le status devrait être mis à jour")
            return False

        print("update_status fonctionne")
        return True
    except Exception as e:
        print(f"Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test du Projet 10\n")
    print("Note: Les subscriptions nécessitent un client MCP réel pour être testées complètement\n")

    success = True
    success = asyncio.run(test_list_resources()) and success
    print()
    success = asyncio.run(test_update_status()) and success

    print()
    if success:
        print("Tests de base passent !")
        print("Les subscriptions nécessitent un client MCP réel pour être testées")
    else:
        print("Certains tests ont échoué.")
        sys.exit(1)