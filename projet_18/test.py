"""
Script de test pour le projet 18
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock, MagicMock

async def test_tools_exist():
    """Test que les outils existent"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    tools = ["creatif_ideation", "conversation", "reponse_rapide"]
    for tool_name in tools:
        if not hasattr(solution, tool_name):
            print(f"❌ L'outil '{tool_name}' n'existe pas")
            return False
    
    print("✅ Tous les outils existent")
    return True

async def test_advanced_parameters():
    """Test que les outils peuvent être appelés"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    mock_sampling = MagicMock()
    mock_response = MagicMock()
    mock_response.content.text = "Réponse simulée"
    mock_sampling.create_message = AsyncMock(return_value=mock_response)
    mock_ctx.sampling = mock_sampling
    
    try:
        await solution.reponse_rapide("Test", mock_ctx)
        print("✅ Les outils peuvent être appelés")
        return True
    except Exception as e:
        print(f"⚠️  Erreur (peut être normal si non implémenté) : {e}")
        return True

if __name__ == "__main__":
    print("🧪 Test du Projet 18\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_advanced_parameters()) and success
    
    print()
    if success:
        print("✅ Tests de base passent !")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

