"""
Script de test pour le projet 20
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

async def test_validate_token():
    """Test que valider_token fonctionne"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Test token valide
    result = solution.valider_token("Bearer token123")
    if result is None:
        print("❌ Un token valide devrait être accepté")
        return False
    
    if "username" not in result:
        print("❌ Le résultat devrait contenir username")
        return False
    
    # Test token invalide
    result = solution.valider_token("Bearer invalid")
    if result is not None:
        print("❌ Un token invalide devrait être rejeté")
        return False
    
    print("✅ valider_token fonctionne")
    return True

async def test_info_utilisateur():
    """Test que info_utilisateur fonctionne"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.info_utilisateur("Bearer token123", mock_ctx)
        
        if not isinstance(result, dict):
            print("❌ Le résultat devrait être un dict")
            return False
        
        if "username" not in result:
            print("❌ Le résultat devrait contenir username")
            return False
        
        print("✅ info_utilisateur fonctionne")
        return True
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_invalid_token():
    """Test qu'un token invalide lève une erreur"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    try:
        await solution.info_utilisateur("Bearer invalid", mock_ctx)
        print("❌ Devrait lever ValueError pour token invalide")
        return False
    except ValueError:
        print("✅ ValueError levé correctement pour token invalide")
        return True
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        return False

if __name__ == "__main__":
    print("🧪 Test du Projet 20\n")
    
    success = True
    success = asyncio.run(test_validate_token()) and success
    print()
    success = asyncio.run(test_info_utilisateur()) and success
    print()
    success = asyncio.run(test_invalid_token()) and success
    
    print()
    if success:
        print("✅ Tous les tests passent !")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

