"""
Test script for project 20
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

async def test_validate_token():
    """Test that validate_token works"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Test valid token
    result = solution.validate_token("Bearer token123")
    if result is None:
        print("❌ A valid token should be accepted")
        return False
    
    if "username" not in result:
        print("❌ The result should contain username")
        return False
    
    # Test invalid token
    result = solution.validate_token("Bearer invalid")
    if result is not None:
        print("❌ An invalid token should be rejected")
        return False
    
    print("✅ validate_token works")
    return True

async def test_user_info():
    """Test that user_info works"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.user_info("Bearer token123", mock_ctx)
        
        if not isinstance(result, dict):
            print("❌ The result should be a dict")
            return False
        
        if "username" not in result:
            print("❌ The result should contain username")
            return False
        
        print("✅ user_info works")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_invalid_token_error():
    """Test that an invalid token raises an error"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    try:
        await solution.user_info("Bearer invalid", mock_ctx)
        print("❌ Should raise ValueError for invalid token")
        return False
    except ValueError:
        print("✅ ValueError correctly raised for invalid token")
        return True
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Test for Project 20\n")
    
    success = True
    success = asyncio.run(test_validate_token()) and success
    print()
    success = asyncio.run(test_user_info()) and success
    print()
    success = asyncio.run(test_invalid_token_error()) and success
    
    print()
    if success:
        print("✅ All tests pass!")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
