"""Tests pour projet 21"""
import sys
import importlib.util
import asyncio

async def test_validation():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Test scope requis
    result = solution.valider_token("Bearer token123", required_scopes=["read:data"])
    if result is None:
        print("❌ Token avec bon scope devrait être accepté")
        return False
    print("✅ Validation avec scopes fonctionne")
    return True

if __name__ == "__main__":
    asyncio.run(test_validation())

