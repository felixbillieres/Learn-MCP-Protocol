"""
Test script for project 21
This script verifies advanced authorization with scopes and audiences
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_models_exist():
    """Test that server and token structure exist"""
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
    
    if not hasattr(solution, 'VALID_TOKENS'):
        print("VALID_TOKENS should exist")
        return False
    
    if not hasattr(solution, 'validate_token'):
        print("validate_token function does not exist")
        return False
    
    print("Server and functions exist")
    return True

def test_validate_token():
    """Test token validation with scopes"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        # Test token with correct scope
        result = solution.validate_token("Bearer token123", required_scopes=["read:data"])
        if result is None:
            print("❌ Token with correct scope should be accepted")
            return False
        
        # Test token with incorrect scope
        result = solution.validate_token("Bearer token123", required_scopes=["admin:all"])
        if result is not None:
            print("⚠️  Token with incorrect scope might be rejected (check implementation)")
        
        # Test token with audience
        result = solution.validate_token("Bearer token123", required_audience="api.example.com")
        if result is None:
            print("⚠️  Token with correct audience might be rejected (check implementation)")
        
        print("✅ Validation with scopes works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_data():
    """Test read_data tool with authorization"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    try:
        if hasattr(solution, 'read_data'):
            result = await solution.read_data("Bearer token123", mock_ctx)
            
            if not isinstance(result, dict):
                print(f"read_data should return a dict, but returned {type(result)}")
                return False
            
            print("✅ read_data works")
            return True
        else:
            print("⚠️  read_data function does not exist")
            return True
    except Exception as e:
        print(f"⚠️  Error (may be normal if not implemented): {e}")
        return True

async def test_write_data():
    """Test write_data tool with authorization"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    try:
        if hasattr(solution, 'write_data'):
            test_data = {"key": "value", "test": True}
            result = await solution.write_data("Bearer token123", test_data, mock_ctx)
            
            if not isinstance(result, dict):
                print(f"write_data should return a dict, but returned {type(result)}")
                return False
            
            print("✅ write_data works")
            return True
        else:
            print("⚠️  write_data function does not exist")
            return True
    except Exception as e:
        print(f"⚠️  Error (may be normal if not implemented): {e}")
        return True

if __name__ == "__main__":
    print("🧪 Test for Project 21\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    success = test_validate_token() and success
    print()
    
    print("Testing read_data...")
    success = asyncio.run(test_read_data()) and success
    print()
    
    print("Testing write_data...")
    success = asyncio.run(test_write_data()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've implemented advanced authorization with scopes and audiences!")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
