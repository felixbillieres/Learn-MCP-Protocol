"""
Script de test pour le projet 26
Ce script vérifie le scanner de ports
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_models_exist():
    """Test que les modèles existent"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Erreur lors de l'import : {e}")
        import traceback
        traceback.print_exc()
        return False
    
    if not hasattr(solution, 'PortInfo'):
        print("Le modèle 'PortInfo' n'existe pas")
        return False
    
    if not hasattr(solution, 'ScanResult'):
        print("Le modèle 'ScanResult' n'existe pas")
        return False
    
    print("Les modèles existent")
    return True

async def test_scanner_ports():
    """Test l'outil scanner_ports"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'scans'):
        solution.scans.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.scanner_ports("192.168.1.1", None, "quick", mock_ctx)
        
        if not isinstance(result, solution.ScanResult):
            print(f"Le résultat devrait être un ScanResult, mais c'est {type(result)}")
            return False
        
        if result.target != "192.168.1.1":
            print(f"La cible devrait être '192.168.1.1', mais c'est '{result.target}'")
            return False
        
        if len(result.ports) == 0:
            print("Le scan devrait détecter au moins un port")
            return False
        
        print("scanner_ports fonctionne")
        return True
    
    except Exception as e:
        print(f"Erreur lors du scan : {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_analyser_services():
    """Test l'outil analyser_services"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'scans'):
        solution.scans.clear()
    
    mock_ctx = AsyncMock()
    
    # Crée un scan d'abord
    await solution.scanner_ports("192.168.1.1", None, "quick", mock_ctx)
    
    try:
        result = await solution.analyser_services(0, mock_ctx)
        
        if not isinstance(result, dict):
            print(f"Le résultat devrait être un dict, mais c'est {type(result)}")
            return False
        
        print("analyser_services fonctionne")
        return True
    
    except Exception as e:
        print(f"Erreur lors de l'analyse : {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test du Projet 26\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Test scanner_ports...")
    success = asyncio.run(test_scanner_ports()) and success
    print()
    
    print("Test analyser_services...")
    success = asyncio.run(test_analyser_services()) and success
    print()
    
    if success:
        print("Tous les tests passent !")
        print("Tu as créé un scanner de ports fonctionnel !")
    else:
        print("Certains tests ont échoué. Vérifie ton code !")
        sys.exit(1)

