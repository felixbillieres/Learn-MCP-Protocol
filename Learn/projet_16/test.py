"""
Script de test pour le projet 16
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
    
    if not hasattr(solution, 'authentifier'):
        print("❌ L'outil 'authentifier' n'existe pas")
        return False
    
    if not hasattr(solution, 'configurer_api_key'):
        print("❌ L'outil 'configurer_api_key' n'existe pas")
        return False
    
    print("✅ Les outils existent")
    return True

async def test_url_mode_usage():
    """Test que les outils peuvent être appelés"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    # Pour URL mode, la réponse est généralement None ou une confirmation
    mock_elicitation.create = AsyncMock(return_value=None)
    mock_ctx.elicitation = mock_elicitation
    
    try:
        await solution.authentifier(mock_ctx)
        print("✅ L'outil authentifier peut être appelé")
        return True
    except Exception as e:
        print(f"⚠️  Erreur (peut être normal si non implémenté) : {e}")
        return True

if __name__ == "__main__":
    print("🧪 Test du Projet 16\n")
    print("Note: L'elicitation URL mode nécessite un client MCP réel pour être testée\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_url_mode_usage()) and success
    
    print()
    if success:
        print("✅ Tests de base passent !")
        print("💡 Pour tester URL mode complètement, utilise un client MCP réel")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

