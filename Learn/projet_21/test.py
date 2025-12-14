"""
Test script for project 21
"""
import sys
import importlib.util
import asyncio

async def test_validation():
    """Test token validation with scopes"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Test required scope
    result = solution.validate_token("Bearer token123", required_scopes=["read:data"])
    if result is None:
        print("❌ Token with correct scope should be accepted")
        return False
    print("✅ Validation with scopes works")
    return True

if __name__ == "__main__":
    print("🧪 Test for Project 21\n")
    success = asyncio.run(test_validation())
    if success:
        print("✅ All tests pass!")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
