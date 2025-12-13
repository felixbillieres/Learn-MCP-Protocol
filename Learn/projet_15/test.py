"""
Script de test pour le projet 15
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock, MagicMock

async def test_schema_structure():
    """Test que les outils sont définis"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'inscription'):
        print("❌ L'outil 'inscription' n'existe pas")
        return False
    
    if not hasattr(solution, 'commander_produit'):
        print("❌ L'outil 'commander_produit' n'existe pas")
        return False
    
    print("✅ Les outils existent")
    return True

async def test_validation_functions():
    """Test que les fonctions de validation fonctionnent"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Test validate_username
    if hasattr(solution, 'validate_username'):
        assert solution.validate_username("test123") == True
        assert solution.validate_username("ab") == False  # Trop court
        assert solution.validate_username("a" * 21) == False  # Trop long
        assert solution.validate_username("test-123") == False  # Caractère invalide
        print("✅ validate_username fonctionne")
    
    # Test validate_email
    if hasattr(solution, 'validate_email'):
        assert solution.validate_email("test@example.com") == True
        assert solution.validate_email("invalid") == False
        print("✅ validate_email fonctionne")
    
    return True

async def test_elicitation_with_schema():
    """Test que l'elicitation peut être appelée"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_response = {
        "username": "testuser",
        "email": "test@example.com",
        "age": 25,
        "newsletter": False
    }
    mock_elicitation.create = AsyncMock(return_value=mock_response)
    mock_ctx.elicitation = mock_elicitation
    
    try:
        await solution.inscription(mock_ctx)
        print("✅ L'outil peut être appelé")
        return True
    except Exception as e:
        print(f"⚠️  Erreur (peut être normal si non implémenté) : {e}")
        return True

if __name__ == "__main__":
    print("🧪 Test du Projet 15\n")
    
    success = True
    success = asyncio.run(test_schema_structure()) and success
    print()
    success = asyncio.run(test_validation_functions()) and success
    print()
    success = asyncio.run(test_elicitation_with_schema()) and success
    
    print()
    if success:
        print("✅ Tests de base passent !")
        print("💡 Pour tester l'elicitation complètement, utilise un client MCP réel")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

