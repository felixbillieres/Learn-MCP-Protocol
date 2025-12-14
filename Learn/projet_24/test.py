"""
Test script for project 24
This script verifies transport configuration
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_server_exists():
    """Test that server exists"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error during import: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    if not hasattr(solution, 'mcp_server'):
        print("The server does not exist")
        return False
    
    print("Server exists")
    return True

async def test_transport_info():
    """Test transport info tool"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    try:
        if hasattr(solution, 'transport_info'):
            result = await solution.transport_info()
            
            if not isinstance(result, dict):
                print(f"transport_info should return a dict, but returned {type(result)}")
                return False
            
            if "transport" not in result:
                print("Result should contain 'transport' key")
                return False
            
            # Verify transport is one of the valid values
            valid_transports = ["http", "stdio"]
            if result["transport"] not in valid_transports:
                print(f"Transport should be one of {valid_transports}, but is '{result['transport']}'")
                return False
            
            print(f"transport_info works: transport is '{result['transport']}'")
            return True
        else:
            print("transport_info function does not exist")
            return False
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_transport_configuration():
    """Test transport configuration handling"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'TRANSPORT'):
        print("TRANSPORT configuration should exist")
        return False
    
    # Verify it's a valid transport
    valid_transports = ["http", "stdio"]
    if solution.TRANSPORT not in valid_transports:
        print(f"TRANSPORT should be one of {valid_transports}")
        return False
    
    print(f"Transport configuration is valid: {solution.TRANSPORT}")
    return True

def test_main_function():
    """Test that main function exists"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'main'):
        print("main function does not exist")
        return False
    
    print("main function exists")
    return True

if __name__ == "__main__":
    print("Test for Project 24\n")
    
    success = True
    success = test_server_exists() and success
    print()
    
    success = test_transport_configuration() and success
    print()
    
    success = test_main_function() and success
    print()
    
    print("Testing transport_info...")
    success = asyncio.run(test_transport_info()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've implemented transport configuration!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
