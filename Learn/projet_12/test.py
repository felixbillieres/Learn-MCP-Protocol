"""
Script de test pour le projet 12
"""

import sys
import importlib.util
import asyncio

async def test_prompt_with_args():
    """Test que get_prompt fonctionne avec des arguments"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        # Test avec tous les arguments
        result = await solution.get_prompt(
            "code_review",
            arguments={"language": "python", "code": "def hello(): pass"}
        )
        
        if not isinstance(result, dict) or "messages" not in result:
            print("❌ Le résultat doit contenir 'messages'")
            return False
        
        # Vérifie que les arguments ont été remplacés
        msg_text = result["messages"][0]["content"]["text"]
        if "python" not in msg_text.lower():
            print("❌ Les arguments devraient être remplacés dans le message")
            return False
        
        print("✅ get_prompt avec arguments fonctionne !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_missing_required_arg():
    """Test qu'une erreur est levée si un argument requis manque"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        await solution.get_prompt("code_review", arguments={"language": "python"})
        # Manque "code" qui est requis
        print("❌ Devrait lever ValueError pour argument requis manquant")
        return False
    except ValueError:
        print("✅ ValueError levé correctement pour argument manquant")
        return True
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        return False

async def test_optional_arg():
    """Test qu'un argument optionnel utilise sa valeur par défaut"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.get_prompt(
            "summary",
            arguments={"topic": "MCP"}
        )
        # length est optionnel, devrait utiliser "short" par défaut
        
        if not isinstance(result, dict):
            print("❌ Le résultat doit être un dict")
            return False
        
        print("✅ Arguments optionnels fonctionnent !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Test du Projet 12\n")
    
    success = True
    success = asyncio.run(test_prompt_with_args()) and success
    print()
    success = asyncio.run(test_missing_required_arg()) and success
    print()
    success = asyncio.run(test_optional_arg()) and success
    
    print()
    if success:
        print("🎉 Tous les tests passent !")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

