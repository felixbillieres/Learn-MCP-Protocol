"""
Script de test pour le projet 27
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_models_exist():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Erreur : {e}")
        return False
    if not hasattr(solution, 'Payload'):
        print("Le modèle 'Payload' n'existe pas")
        return False
    print("Les modèles existent")
    return True

async def test_creer_payload():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    if hasattr(solution, 'payloads'):
        solution.payloads.clear()
    mock_ctx = AsyncMock()
    try:
        result = await solution.creer_payload(
            "test", "shell", "linux", "x64", "#!/bin/bash\nwhoami",
            None, [], mock_ctx
        )
        if not isinstance(result, solution.Payload):
            return False
        print("creer_payload fonctionne")
        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False

if __name__ == "__main__":
    print("Test du Projet 27\n")
    success = test_models_exist()
    print()
    success = asyncio.run(test_creer_payload()) and success
    print()
    if success:
        print("Tests passent !")
    else:
        print("Tests échoués")
        sys.exit(1)

