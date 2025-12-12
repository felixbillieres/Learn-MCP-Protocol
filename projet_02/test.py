"""
Script de test pour le projet 02
Ce script vérifie que les outils sont bien enregistrés et fonctionnent
"""

import sys
import importlib.util
import asyncio

def test_tools_registered():
    """Test que les outils sont bien enregistrés"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Erreur lors de l'import : {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test que les fonctions existent
    if not hasattr(solution, 'dire_bonjour'):
        print("La fonction 'dire_bonjour' n'existe pas")
        return False

    if not hasattr(solution, 'calculer_somme'):
        print("La fonction 'calculer_somme' n'existe pas")
        return False

    # Test que ce sont des fonctions async
    dire_bonjour = solution.dire_bonjour
    calculer_somme = solution.calculer_somme

    if not asyncio.iscoroutinefunction(dire_bonjour):
        print("'dire_bonjour' doit être une fonction async")
        return False

    if not asyncio.iscoroutinefunction(calculer_somme):
        print("'calculer_somme' doit être une fonction async")
        return False

    print("Les fonctions sont bien définies et async !")
    return True

async def test_tools_execution():
    """Test que les outils fonctionnent correctement"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Test dire_bonjour
    try:
        result = await solution.dire_bonjour("Test")
        if not isinstance(result, str):
            print(f"'dire_bonjour' devrait retourner une string, mais a retourné {type(result)}")
            return False
        if "Test" not in result:
            print(f"'dire_bonjour' devrait contenir le nom, mais a retourné: {result}")
            return False
        print(f"'dire_bonjour' fonctionne : {result}")
    except Exception as e:
        print(f"Erreur lors de l'exécution de 'dire_bonjour' : {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test calculer_somme
    try:
        result = await solution.calculer_somme(5, 3)
        if not isinstance(result, int):
            print(f"'calculer_somme' devrait retourner un int, mais a retourné {type(result)}")
            return False
        if result != 8:
            print(f"'calculer_somme(5, 3)' devrait retourner 8, mais a retourné {result}")
            return False
        print(f"'calculer_somme' fonctionne : 5 + 3 = {result}")
    except Exception as e:
        print(f"Erreur lors de l'exécution de 'calculer_somme' : {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

def test_tools_listed():
    """Test que les outils sont listés par le serveur"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Importe après avoir chargé solution (pour que les décorateurs s'appliquent)
    import asyncio

    async def check_tools():
        try:
            tools = await solution.mcp_server.list_tools()
            tool_names = {tool.name for tool in tools}

            if "dire_bonjour" not in tool_names:
                print("L'outil 'dire_bonjour' n'est pas enregistré sur le serveur")
                return False

            if "calculer_somme" not in tool_names:
                print("L'outil 'calculer_somme' n'est pas enregistré sur le serveur")
                return False

            print(f"Les outils sont bien enregistrés : {tool_names}")
            return True
        except Exception as e:
            print(f"Erreur lors de la vérification des outils : {e}")
            import traceback
            traceback.print_exc()
            return False

    return asyncio.run(check_tools())

if __name__ == "__main__":
    print("Test du Projet 02\n")

    success = True
    success = test_tools_registered() and success
    print()

    print("Test d'exécution des outils...")
    success = asyncio.run(test_tools_execution()) and success
    print()

    print("Test d'enregistrement sur le serveur...")
    success = test_tools_listed() and success

    print()
    if success:
        print("Tous les tests passent !")
        print("Tu peux maintenant lancer 'python solution.py' pour démarrer ton serveur avec les outils")
    else:
        print("Certains tests ont échoué. Vérifie ton code !")
        sys.exit(1)