"""
Script de test pour le projet 19
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

async def test_tools_exist():
    """Test que tous les outils existent"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    tools = ["calculer", "rechercher_info", "convertir_unite", "agent_resolveur"]
    for tool_name in tools:
        if not hasattr(solution, tool_name):
            print(f"❌ L'outil '{tool_name}' n'existe pas")
            return False
    
    print("✅ Tous les outils existent")
    return True

async def test_tools_for_llm():
    """Test que TOOLS_FOR_LLM est défini"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'TOOLS_FOR_LLM'):
        print("❌ TOOLS_FOR_LLM n'est pas défini")
        return False
    
    if not isinstance(solution.TOOLS_FOR_LLM, list):
        print("❌ TOOLS_FOR_LLM doit être une liste")
        return False
    
    print(f"✅ TOOLS_FOR_LLM est défini avec {len(solution.TOOLS_FOR_LLM)} outils")
    return True

if __name__ == "__main__":
    print("🧪 Test du Projet 19\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_tools_for_llm()) and success
    
    print()
    if success:
        print("✅ Tests de base passent !")
        print("💡 Pour tester les workflows agentiques, utilise un client MCP réel avec LLM")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

