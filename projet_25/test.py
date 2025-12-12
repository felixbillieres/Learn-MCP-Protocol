"""Tests pour projet 25 (FINAL)"""
import sys
import importlib.util
import asyncio

async def test_complete_server():
    """Test que le serveur est complet."""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Vérifie que le serveur existe
    if not hasattr(solution, 'mcp_server'):
        print("❌ Le serveur n'existe pas")
        return False
    
    print("✅ Le serveur existe")
    print("🎉 PROJET FINAL ! Utilise toutes les fonctionnalités que tu as apprises !")
    return True

if __name__ == "__main__":
    asyncio.run(test_complete_server())

