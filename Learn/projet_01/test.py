"""
Test script for project 01
This script verifies that the MCP server is properly configured
"""

import sys
import importlib.util

def test_server_creation():
    """Test that the server is properly created"""

    # Import the solution module
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error during import: {e}")
        return False

    # Check that mcp_server exists
    if not hasattr(solution, 'mcp_server'):
        print("The variable 'mcp_server' does not exist")
        return False

    # Check that it's a FastMCP instance
    from mcp.server.fastmcp import FastMCP
    if not isinstance(solution.mcp_server, FastMCP):
        print("'mcp_server' is not a FastMCP instance")
        return False

    # Check configuration
    if solution.mcp_server.name != "MyFirstServer":
        print(f"The server name should be 'MyFirstServer', but it's '{solution.mcp_server.name}'")
        return False

    print("MCP server correctly created!")
    print(f"  Name: {solution.mcp_server.name}")
    
    # Check host and port variables if they exist
    if hasattr(solution, 'mcp_host'):
        print(f"  Host: {solution.mcp_host}")
    else:
        print(f"  Host: (not defined as variable)")
    
    if hasattr(solution, 'mcp_port'):
        print(f"  Port: {solution.mcp_port}")
    else:
        print(f"  Port: (not defined as variable)")
    
    return True

def test_main_exists():
    """Test that the main function exists"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error during import: {e}")
        return False

    if not hasattr(solution, 'main'):
        print("The function 'main()' does not exist")
        return False

    if not callable(solution.main):
        print("'main' is not a function")
        return False

    print("The main() function exists!")
    return True

if __name__ == "__main__":
    print("Test for Project 01\n")

    success = True
    success = test_server_creation() and success
    print()
    success = test_main_exists() and success

    print()
    if success:
        print("All tests pass!")
        print("You can now run 'python solution.py' to start your server")
    else:
        print("Some tests failed. Check your code!")
        sys.exit(1)
