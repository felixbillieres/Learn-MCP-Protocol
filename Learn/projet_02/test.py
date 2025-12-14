"""
Test script for project 02
This script verifies that tools are properly registered and work
"""

import sys
import importlib.util
import asyncio
import os
import json
from pathlib import Path

def test_tools_registered():
    """Test that tools are properly registered"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error during import: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test that functions exist
    if not hasattr(solution, 'say_hello'):
        print("The function 'say_hello' does not exist")
        return False

    if not hasattr(solution, 'calculate_sum'):
        print("The function 'calculate_sum' does not exist")
        return False

    # Test that they are async functions
    say_hello = solution.say_hello
    calculate_sum = solution.calculate_sum

    if not asyncio.iscoroutinefunction(say_hello):
        print("'say_hello' must be an async function")
        return False

    if not asyncio.iscoroutinefunction(calculate_sum):
        print("'calculate_sum' must be an async function")
        return False

    print("Functions are properly defined and async!")
    return True

async def test_tools_execution():
    """Test that tools work correctly"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Test say_hello
    try:
        result = await solution.say_hello("Test")
        if not isinstance(result, str):
            print(f"'say_hello' should return a string, but returned {type(result)}")
            return False
        if "Test" not in result:
            print(f"'say_hello' should contain the name, but returned: {result}")
            return False
        print(f"'say_hello' works: {result}")
    except Exception as e:
        print(f"Error during execution of 'say_hello': {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test calculate_sum
    try:
        result = await solution.calculate_sum(5, 3)
        if not isinstance(result, int):
            print(f"'calculate_sum' should return an int, but returned {type(result)}")
            return False
        if result != 8:
            print(f"'calculate_sum(5, 3)' should return 8, but returned {result}")
            return False
        print(f"'calculate_sum' works: 5 + 3 = {result}")
    except Exception as e:
        print(f"Error during execution of 'calculate_sum': {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

def test_tools_listed():
    """Test that tools are listed by the server"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Import after loading solution (so decorators apply)
    import asyncio

    async def check_tools():
        try:
            tools = await solution.mcp_server.list_tools()
            tool_names = {tool.name for tool in tools}

            if "say_hello" not in tool_names:
                print("The tool 'say_hello' is not registered on the server")
                return False

            if "calculate_sum" not in tool_names:
                print("The tool 'calculate_sum' is not registered on the server")
                return False

            print(f"Tools are properly registered: {tool_names}")
            return True
        except Exception as e:
            print(f"Error during tool verification: {e}")
            import traceback
            traceback.print_exc()
            return False

    return asyncio.run(check_tools())

def setup_claude_desktop():
    """Automatically configure Claude Desktop for this MCP server"""
    try:
        # Detect current project
        current_dir = Path(__file__).parent.absolute()
        project_name = current_dir.name
        solution_path = current_dir / "solution.py"
        
        if not solution_path.exists():
            print(f"⚠️  solution.py not found in {current_dir}")
            return False
        
        # Create a wrapper script to ensure PYTHONPATH is properly defined
        import shutil
        python_cmd = shutil.which("python3.12") or "/usr/bin/python3.12"
        
        # Find venv path for PYTHONPATH
        venv_site_packages = current_dir.parent / "venv" / "lib" / "python3.12" / "site-packages"
        pythonpath = str(venv_site_packages) if venv_site_packages.exists() else None
        
        # Create wrapper script
        wrapper_script = current_dir / "run_mcp.sh"
        if pythonpath:
            wrapper_content = f"""#!/bin/bash
# Wrapper to run MCP server with correct PYTHONPATH
export PYTHONPATH="{pythonpath}:$PYTHONPATH"
{python_cmd} "{solution_path}"
"""
        else:
            wrapper_content = f"""#!/bin/bash
{python_cmd} "{solution_path}"
"""
        
        wrapper_script.write_text(wrapper_content)
        wrapper_script.chmod(0o755)
        
        # Find Claude Desktop config directory
        home = Path.home()
        config_dirs = [
            home / ".config" / "Claude",
            home / "Library" / "Application Support" / "Claude",
        ]
        
        config_dir = None
        for dir_path in config_dirs:
            if dir_path.exists():
                config_dir = dir_path
                break
        
        if not config_dir:
            print("⚠️  Claude Desktop config directory not found")
            print("   Please configure manually:")
            print(f"   - Server path: {wrapper_script}")
            return False
        
        # Create or update config
        config_file = config_dir / "claude_desktop_config.json"
        
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
            except:
                config = {}
        else:
            config = {}
        
        if "mcpServers" not in config:
            config["mcpServers"] = {}
        
        config["mcpServers"][project_name] = {
            "command": str(wrapper_script),
            "args": []
        }
        
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Configuration added to {config_file}")
        print(f"   Restart Claude Desktop to activate the server.")
        return True
        
    except Exception as e:
        print(f"❌ Error during configuration: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 02\n")

    success = True
    success = test_tools_registered() and success
    print()

    print("Testing tool execution...")
    success = asyncio.run(test_tools_execution()) and success
    print()

    success = test_tools_listed() and success
    print()

    if success:
        print("All tests pass!")
        print("You can now run 'python solution.py' to start your server with the tools")
        
        # Optionally setup Claude Desktop
        if "--setup-claude" in sys.argv:
            print("\nSetting up Claude Desktop...")
            setup_claude_desktop()
    else:
        print("Some tests failed. Check your code!")
        sys.exit(1)
