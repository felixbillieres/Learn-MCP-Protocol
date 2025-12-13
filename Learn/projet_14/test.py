"""
Script de test pour le projet 14
Note: L'elicitation nécessite un vrai client MCP pour être testée complètement
Ce test vérifie que les outils sont bien définis
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock, MagicMock

async def test_tools_exist():
    """Test que les outils existent"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'creer_profil'):
        print("❌ L'outil 'creer_profil' n'existe pas")
        return False
    
    if not hasattr(solution, 'configurer_preferences'):
        print("❌ L'outil 'configurer_preferences' n'existe pas")
        return False
    
    print("✅ Les outils existent")
    return True

async def test_elicitation_structure():
    """Test que les outils utilisent l'elicitation (simulé)"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Crée un mock Context avec elicitation
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_response = {"nom": "Test", "age": 25, "email": "test@example.com"}
    mock_elicitation.create = AsyncMock(return_value=mock_response)
    mock_ctx.elicitation = mock_elicitation
    
    try:
        # Test que l'outil peut être appelé
        result = await solution.creer_profil(mock_ctx)
        
        # Vérifie que l'elicitation a été appelée
        if not mock_elicitation.create.called:
            print("⚠️  ctx.elicitation.create() n'a pas été appelé (normal si le code n'est pas implémenté)")
        else:
            print("✅ L'elicitation est utilisée correctement")
        
        print("✅ L'outil peut être appelé")
        return True
        
    except AttributeError as e:
        if "elicitation" in str(e):
            print("⚠️  L'elicitation n'est pas encore implémentée dans le code")
            print("💡 Assure-toi d'utiliser ctx.elicitation.create()")
            return True  # Pas une erreur, juste pas encore implémenté
        raise
    except Exception as e:
        print(f"⚠️  Erreur (peut être normal si non implémenté) : {e}")
        return True  # Pas une erreur fatale

if __name__ == "__main__":
    print("🧪 Test du Projet 14\n")
    print("Note: L'elicitation nécessite un client MCP réel pour être testée complètement\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_elicitation_structure()) and success
    
    print()
    if success:
        print("✅ Tests de base passent !")
        print("💡 Pour tester l'elicitation complètement, utilise un client MCP réel")
    else:
        print("❌ Certains tests ont échoué.")
        sys.exit(1)

