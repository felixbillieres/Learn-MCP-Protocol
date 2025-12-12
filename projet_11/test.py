"""
Script de test pour le projet 11
"""

import sys
import importlib.util
import asyncio

async def test_list_prompts():
    """Test que list_prompts fonctionne"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.list_prompts()
        
        if not isinstance(result, list):
            print(f"❌ list_prompts devrait retourner une liste")
            return False
        
        if len(result) < 2:
            print(f"❌ Il devrait y avoir au moins 2 prompts, mais il y en a {len(result)}")
            return False
        
        # Vérifie la structure
        for prompt in result:
            if "name" not in prompt:
                print("❌ Chaque prompt doit avoir un champ 'name'")
                return False
        
        print(f"✅ list_prompts fonctionne ! {len(result)} prompts trouvés")
        return True
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_prompt():
    """Test que get_prompt fonctionne"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.get_prompt("greeting")
        
        if not isinstance(result, dict):
            print("❌ get_prompt devrait retourner un dict")
            return False
        
        if "messages" not in result:
            print("❌ Le résultat doit contenir 'messages'")
            return False
        
        messages = result["messages"]
        if not isinstance(messages, list) or len(messages) == 0:
            print("❌ 'messages' doit être une liste non vide")
            return False
        
        # Vérifie le format d'un message
        msg = messages[0]
        if "role" not in msg or "content" not in msg:
            print("❌ Chaque message doit avoir 'role' et 'content'")
            return False
        
        print("✅ get_prompt fonctionne !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_invalid_prompt():
    """Test que get_prompt lève une erreur pour un prompt invalide"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        await solution.get_prompt("nonexistent")
        print("❌ get_prompt devrait lever ValueError pour un prompt inexistant")
        return False
    except ValueError:
        print("✅ get_prompt lève correctement ValueError pour prompt inexistant")
        return True
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        return False

if __name__ == "__main__":
    print("🧪 Test du Projet 11\n")
    
    success = True
    success = asyncio.run(test_list_prompts()) and success
    print()
    success = asyncio.run(test_get_prompt()) and success
    print()
    success = asyncio.run(test_get_invalid_prompt()) and success
    
    print()
    if success:
        print("🎉 Tous les tests passent !")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

