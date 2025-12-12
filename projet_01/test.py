"""
Script de test pour le projet 01
Ce script vérifie que le serveur MCP est bien configuré
"""

import sys
import importlib.util

def test_server_creation():
    """Test que le serveur est bien créé"""

    # Importe le module solution
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Erreur lors de l'import : {e}")
        return False

    # Vérifie que mcp_server existe
    if not hasattr(solution, 'mcp_server'):
        print("La variable 'mcp_server' n'existe pas")
        return False

    # Vérifie que c'est une instance FastMCP
    from mcp.server.fastmcp import FastMCP
    if not isinstance(solution.mcp_server, FastMCP):
        print("'mcp_server' n'est pas une instance de FastMCP")
        return False

    # Vérifie la configuration
    if solution.mcp_server.name != "MonPremierServeur":
        print(f"Le nom du serveur devrait être 'MonPremierServeur', mais c'est '{solution.mcp_server.name}'")
        return False

    print("Serveur MCP correctement créé !")
    print(f"  Nom: {solution.mcp_server.name}")
    
    # Vérifie les variables host et port si elles existent
    if hasattr(solution, 'mcp_host'):
        print(f"  Host: {solution.mcp_host}")
    else:
        print(f"  Host: (non défini comme variable)")
    
    if hasattr(solution, 'mcp_port'):
        print(f"  Port: {solution.mcp_port}")
    else:
        print(f"  Port: (non défini comme variable)")
    
    return True

def test_main_exists():
    """Test que la fonction main existe"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Erreur lors de l'import : {e}")
        return False

    if not hasattr(solution, 'main'):
        print("La fonction 'main()' n'existe pas")
        return False

    if not callable(solution.main):
        print("'main' n'est pas une fonction")
        return False

    print("La fonction main() existe !")
    return True

if __name__ == "__main__":
    print("Test du Projet 01\n")

    success = True
    success = test_server_creation() and success
    print()
    success = test_main_exists() and success

    print()
    if success:
        print("Tous les tests passent !")
        print("Tu peux maintenant lancer 'python solution.py' pour démarrer ton serveur")
    else:
        print("Certains tests ont échoué. Vérifie ton code !")
        sys.exit(1)