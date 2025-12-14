"""
Test script for project 22
This script verifies authorization with rate limiting
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_models_exist():
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
    
    if not hasattr(solution, 'VALID_TOKENS'):
        print("VALID_TOKENS should exist")
        return False
    
    print("Server and configuration exist")
    return True

async def test_check_rate_limit():
    """Test rate limiting function"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        # Test rate limiting logic
        if hasattr(solution, 'check_rate_limit'):
            # Reset request counts
            if hasattr(solution, 'REQUEST_COUNTS'):
                solution.REQUEST_COUNTS.clear()
            
            # First request should be allowed
            result = solution.check_rate_limit("user1", max_requests=5, window=60)
            if result is not True:
                print("First request should be allowed within rate limit")
                return False
            
            print("check_rate_limit works")
            return True
        else:
            print("check_rate_limit function does not exist")
            return False
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_secure_action():
    """Test secure action with authorization"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    try:
        # Test with valid token
        if hasattr(solution, 'secure_action'):
            result = await solution.secure_action("Bearer token123", mock_ctx)
            
            if not isinstance(result, dict):
                print(f"secure_action should return a dict, but returned {type(result)}")
                return False
            
            print("secure_action works")
            return True
        else:
            print("secure_action function does not exist")
            return False
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_token_validation():
    """Test token validation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'VALID_TOKENS'):
        print("VALID_TOKENS should exist")
        return False
    
    if "Bearer token123" not in solution.VALID_TOKENS:
        print("Valid token should be in VALID_TOKENS")
        return False
    
    print("Token validation structure exists")
    return True

if __name__ == "__main__":
    print("Test for Project 22\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    success = test_token_validation() and success
    print()
    
    print("Testing check_rate_limit...")
    success = asyncio.run(test_check_rate_limit()) and success
    print()
    
    print("Testing secure_action...")
    success = asyncio.run(test_secure_action()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've implemented authorization with rate limiting!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
