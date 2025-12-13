"""
Script de test pour le projet 09
"""

import sys
import importlib.util
import asyncio

async def test_list_resource_templates():
    """Test que list_resource_templates fonctionne"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.list_resource_templates()

        if not isinstance(result, list):
            print(f"list_resource_templates devrait retourner une liste")
            return False

        if len(result) == 0:
            print("Il devrait y avoir au moins un template")
            return False

        # Vérifie la structure
        for template in result:
            if "uriTemplate" not in template:
                print("Chaque template doit avoir 'uriTemplate'")
                return False
            if "{" in template["uriTemplate"] and "}" in template["uriTemplate"]:
                print(f"Template trouvé : {template['uriTemplate']}")

        print(f"list_resource_templates fonctionne ! {len(result)} templates trouvés")
        return True

    except Exception as e:
        print(f"Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_template_resource():
    """Test que read_resource gère les templates"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        # Test avec config template
        result = await solution.read_resource("config://database/host")

        if not isinstance(result, dict) or "contents" not in result:
            print("Le résultat doit contenir 'contents'")
            return False

        print("read_resource gère les templates config://")
        return True

    except Exception as e:
        print(f"Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_file_template():
    """Test avec file template"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.read_resource("file://readme.txt")

        if not isinstance(result, dict) or "contents" not in result:
            print("Le résultat doit contenir 'contents'")
            return False

        print("read_resource gère les templates file://")
        return True

    except Exception as e:
        print(f"Erreur : {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test du Projet 09\n")

    success = True
    success = asyncio.run(test_list_resource_templates()) and success
    print()
    success = asyncio.run(test_read_template_resource()) and success
    print()
    success = asyncio.run(test_read_file_template()) and success

    print()
    if success:
        print("Tous les tests passent !")
    else:
        print("Certains tests ont échoué.")
        sys.exit(1)