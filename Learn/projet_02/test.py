"""
Script de test pour le projet 02
Ce script vérifie que les outils sont bien enregistrés et fonctionnent
"""

import sys
import importlib.util
import asyncio
import os
import json
from pathlib import Path

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

def setup_claude_desktop():
    """Configure automatiquement Claude Desktop pour ce serveur MCP"""
    try:
        # Détecte le projet actuel
        current_dir = Path(__file__).parent.absolute()
        project_name = current_dir.name
        solution_path = current_dir / "solution.py"
        
        if not solution_path.exists():
            print(f"⚠️  solution.py introuvable dans {current_dir}")
            return False
        
        # Crée un script wrapper pour garantir que PYTHONPATH est bien défini
        import shutil
        python_cmd = shutil.which("python3.12") or "/usr/bin/python3.12"
        
        # Trouve le chemin du venv pour PYTHONPATH
        venv_site_packages = current_dir.parent / "venv" / "lib" / "python3.12" / "site-packages"
        pythonpath = str(venv_site_packages) if venv_site_packages.exists() else None
        
        # Crée un script wrapper
        wrapper_script = current_dir / "run_mcp.sh"
        if pythonpath:
            wrapper_content = f"""#!/bin/bash
# Wrapper pour lancer le serveur MCP avec le bon PYTHONPATH
export PYTHONPATH="{pythonpath}:$PYTHONPATH"
exec {python_cmd} "$(dirname "$0")/solution.py" "$@"
"""
            with open(wrapper_script, 'w', encoding='utf-8') as f:
                f.write(wrapper_content)
            import stat
            wrapper_script.chmod(wrapper_script.stat().st_mode | stat.S_IEXEC)
            use_wrapper = True
        else:
            use_wrapper = False
        
        # Chemins possibles pour la config Claude Desktop
        home = Path.home()
        config_paths = [
            home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json",  # macOS
            home / ".config" / "Claude" / "claude_desktop_config.json",  # Linux
            Path(os.environ.get("APPDATA", "")) / "Claude" / "claude_desktop_config.json",  # Windows
        ]
        
        config_path = None
        for path in config_paths:
            if path.parent.exists() or path.exists():
                config_path = path
                break
        
        if not config_path:
            # Crée le répertoire pour Linux
            linux_path = home / ".config" / "Claude"
            linux_path.mkdir(parents=True, exist_ok=True)
            config_path = linux_path / "claude_desktop_config.json"
        
        # Charge ou crée la configuration
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        else:
            config = {}
        
        if "mcpServers" not in config:
            config["mcpServers"] = {}
        
        # Ajoute ou met à jour ce serveur
        server_name = project_name.replace("_", "-")
        
        if use_wrapper:
            # Utilise le script wrapper (plus fiable pour PYTHONPATH)
            server_config = {
                "command": str(wrapper_script),
                "args": []
            }
        else:
            # Fallback : utilise python directement avec PYTHONPATH dans env
            server_config = {
                "command": python_cmd,
                "args": [str(solution_path)]
            }
            if pythonpath:
                server_config["env"] = {
                    "PYTHONPATH": pythonpath
                }
        
        config["mcpServers"][server_name] = server_config
        
        # Sauvegarde la configuration
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Serveur MCP '{server_name}' ajouté à Claude Desktop !")
        print(f"   Fichier de config : {config_path}")
        print(f"   Redémarre Claude Desktop pour activer le serveur.")
        return True
        
    except Exception as e:
        print(f"\n⚠️  Erreur lors de la configuration Claude Desktop : {e}")
        import traceback
        traceback.print_exc()
        return False

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
        # Configure automatiquement Claude Desktop
        setup_claude_desktop()
    else:
        print("Certains tests ont échoué. Vérifie ton code !")
        sys.exit(1)