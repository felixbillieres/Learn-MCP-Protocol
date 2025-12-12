"""
Script de test pour le projet 08
"""

import sys
import importlib.util
import asyncio

async def test_list_resources():
    """Test que list_resources fonctionne"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.list_resources()

        if not isinstance(result, list):
            print(f"list_resources devrait retourner une liste, mais a retourné {type(result)}")
            return False

        if len(result) < 2:
            print(f"Il devrait y avoir au moins 2 ressources, mais il y en a {len(result)}")
            return False

        # Vérifie la structure
        for res in result:
            if "uri" not in res:
                print("Chaque ressource doit avoir un champ 'uri'")
                return False
            if "name" not in res:
                print("Chaque ressource doit avoir un champ 'name'")
                return False

        print(f"list_resources fonctionne ! {len(result)} ressources trouvées")
        return True

    except Exception as e:
        print(f"Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_resource():
    """Test que read_resource fonctionne"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.read_resource("config://app/settings")

        if not isinstance(result, dict):
            print(f"read_resource devrait retourner un dict")
            return False

        if "contents" not in result:
            print("Le résultat doit contenir 'contents'")
            return False

        contents = result["contents"]
        if not isinstance(contents, list) or len(contents) == 0:
            print("'contents' doit être une liste non vide")
            return False

        print("read_resource fonctionne !")
        return True

    except Exception as e:
        print(f"Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_invalid_resource():
    """Test que read_resource lève une erreur pour URI invalide"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        await solution.read_resource("invalid://uri/does/not/exist")
        print("read_resource devrait lever ValueError pour URI invalide")
        return False
    except ValueError:
        print("read_resource lève correctement ValueError pour URI invalide")
        return True
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return False

if __name__ == "__main__":
    print("Test du Projet 08\n")

    success = True
    success = asyncio.run(test_list_resources()) and success
    print()
    success = asyncio.run(test_read_resource()) and success
    print()
    success = asyncio.run(test_read_invalid_resource()) and success

    print()
    if success:
        print("Tous les tests passent !")
    else:
        print("Certains tests ont échoué.")
        sys.exit(1)