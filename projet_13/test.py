"""
Script de test pour le projet 13
"""

import sys
import importlib.util
import asyncio

async def test_multiple_messages():
    """Test que tutorial retourne plusieurs messages"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.get_prompt("tutorial", arguments={"topic": "MCP"})
        
        if not isinstance(result, dict) or "messages" not in result:
            print("❌ Le résultat doit contenir 'messages'")
            return False
        
        messages = result["messages"]
        if len(messages) < 2:
            print(f"❌ tutorial devrait retourner au moins 2 messages, mais a retourné {len(messages)}")
            return False
        
        print(f"✅ tutorial retourne {len(messages)} messages !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_resource_reference():
    """Test que code_analysis référence une resource"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.get_prompt(
            "code_analysis",
            arguments={"code": "def test(): pass"}
        )
        
        if not isinstance(result, dict) or "messages" not in result:
            print("❌ Le résultat doit contenir 'messages'")
            return False
        
        # Vérifie qu'une resource est référencée
        messages = result["messages"]
        has_resource = False
        for msg in messages:
            content = msg.get("content", {})
            if isinstance(content, dict) and content.get("type") == "resource":
                has_resource = True
                break
        
        if not has_resource:
            print("❌ code_analysis devrait référencer une resource")
            return False
        
        print("✅ code_analysis référence correctement une resource !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Test du Projet 13\n")
    
    success = True
    success = asyncio.run(test_multiple_messages()) and success
    print()
    success = asyncio.run(test_resource_reference()) and success
    
    print()
    if success:
        print("🎉 Tous les tests passent !")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

