"""
Script de test pour le projet 03
Ce script vérifie que les modèles Pydantic sont bien définis et fonctionnent
"""

import sys
import importlib.util
import asyncio
from pydantic import ValidationError

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

    # Vérifie que les modèles existent
    if not hasattr(solution, 'Message'):
        print("La classe 'Message' n'existe pas")
        return False

    if not hasattr(solution, 'MessageResponse'):
        print("La classe 'MessageResponse' n'existe pas")
        return False

    # Vérifie que ce sont des modèles Pydantic
    from pydantic import BaseModel

    if not issubclass(solution.Message, BaseModel):
        print("'Message' doit hériter de BaseModel")
        return False

    if not issubclass(solution.MessageResponse, BaseModel):
        print("'MessageResponse' doit hériter de BaseModel")
        return False

    print("Les modèles Pydantic sont bien définis !")
    return True

def test_message_validation():
    """Test que le modèle Message valide correctement"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Test création valide
    try:
        msg = solution.Message(
            expediteur="Alice",
            destinataire="Bob",
            contenu="Hello !"
        )
        if msg.priorite != "normale":
            print(f"La priorité par défaut devrait être 'normale', mais c'est '{msg.priorite}'")
            return False
        print("Message créé avec succès (priorité par défaut)")
    except Exception as e:
        print(f"Erreur lors de la création d'un Message valide : {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test avec priorité explicite
    try:
        msg = solution.Message(
            expediteur="Alice",
            destinataire="Bob",
            contenu="Urgent !",
            priorite="haute"
        )
        if msg.priorite != "haute":
            print(f"La priorité devrait être 'haute', mais c'est '{msg.priorite}'")
            return False
        print("Message créé avec priorité explicite")
    except Exception as e:
        print(f"Erreur lors de la création avec priorité : {e}")
        return False

    # Test validation (champs manquants)
    try:
        msg = solution.Message(expediteur="Alice")  # Manque destinataire et contenu
        print("Le modèle devrait rejeter un message incomplet")
        return False
    except ValidationError:
        print("Validation fonctionne : rejette les messages incomplets")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return False

    return True

async def test_tool_execution():
    """Test que l'outil fonctionne"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Crée un message
    message = solution.Message(
        expediteur="Alice",
        destinataire="Bob",
        contenu="Test message",
        priorite="haute"
    )

    # Appelle l'outil
    try:
        result = await solution.envoyer_message(message)

        # Vérifie le type
        if not isinstance(result, solution.MessageResponse):
            print(f"Le résultat devrait être un MessageResponse, mais c'est {type(result)}")
            return False

        # Vérifie les champs
        if not hasattr(result, 'message_id') or not isinstance(result.message_id, int):
            print("'message_id' devrait être un int")
            return False

        if result.expediteur != "Alice":
            print(f"L'expéditeur devrait être 'Alice', mais c'est '{result.expediteur}'")
            return False

        if result.destinataire != "Bob":
            print(f"Le destinataire devrait être 'Bob', mais c'est '{result.destinataire}'")
            return False

        if not hasattr(result, 'date_envoi') or not isinstance(result.date_envoi, str):
            print("'date_envoi' devrait être une string")
            return False

        print(f"L'outil fonctionne ! Message ID: {result.message_id}, Date: {result.date_envoi}")
        return True

    except Exception as e:
        print(f"Erreur lors de l'exécution de l'outil : {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test du Projet 03\n")

    success = True
    success = test_models_exist() and success
    print()

    success = test_message_validation() and success
    print()

    print("Test d'exécution de l'outil...")
    success = asyncio.run(test_tool_execution()) and success

    print()
    if success:
        print("Tous les tests passent !")
        print("Tu as appris à utiliser Pydantic avec MCP !")
    else:
        print("Certains tests ont échoué. Vérifie ton code !")
        sys.exit(1)