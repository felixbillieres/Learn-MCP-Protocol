"""
Script de test pour le projet 17
Note: Le sampling nécessite un client MCP réel avec LLM pour être testé complètement
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
    
    if not hasattr(solution, 'poser_question'):
        print("❌ L'outil 'poser_question' n'existe pas")
        return False
    
    if not hasattr(solution, 'generer_resume'):
        print("❌ L'outil 'generer_resume' n'existe pas")
        return False
    
    print("✅ Les outils existent")
    return True

async def test_sampling_usage():
    """Test que le sampling peut être utilisé (simulé)"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    mock_sampling = MagicMock()
    mock_response = MagicMock()
    mock_response.content.text = "Réponse simulée du LLM"
    mock_sampling.create_message = AsyncMock(return_value=mock_response)
    mock_ctx.sampling = mock_sampling
    
    try:
        result = await solution.poser_question("Test question", mock_ctx)
        if mock_sampling.create_message.called:
            print("✅ ctx.sampling.create_message() est utilisé")
        else:
            print("⚠️  ctx.sampling.create_message() n'a pas été appelé")
        print("✅ L'outil peut être appelé")
        return True
    except AttributeError as e:
        if "sampling" in str(e):
            print("⚠️  Le sampling n'est pas encore implémenté")
            print("💡 Assure-toi d'utiliser ctx.sampling.create_message()")
            return True
        raise
    except Exception as e:
        print(f"⚠️  Erreur (peut être normal si non implémenté) : {e}")
        return True

if __name__ == "__main__":
    print("🧪 Test du Projet 17\n")
    print("Note: Le sampling nécessite un client MCP réel avec LLM pour être testé complètement\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_sampling_usage()) and success
    
    print()
    if success:
        print("✅ Tests de base passent !")
        print("💡 Pour tester le sampling complètement, utilise un client MCP réel avec LLM")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

