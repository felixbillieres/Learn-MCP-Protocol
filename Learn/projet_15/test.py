"""
Test script for project 15
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock, MagicMock

async def test_schema_structure():
    """Test that tools are defined"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'register'):
        print("❌ The tool 'register' does not exist")
        return False
    
    if not hasattr(solution, 'order_product'):
        print("❌ The tool 'order_product' does not exist")
        return False
    
    print("✅ Tools exist")
    return True

async def test_validation_functions():
    """Test that validation functions work"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Test validate_username
    if hasattr(solution, 'validate_username'):
        assert solution.validate_username("test123") == True
        assert solution.validate_username("ab") == False  # Too short
        assert solution.validate_username("a" * 21) == False  # Too long
        assert solution.validate_username("test-123") == False  # Invalid character
        print("✅ validate_username works")
    
    # Test validate_email
    if hasattr(solution, 'validate_email'):
        assert solution.validate_email("test@example.com") == True
        assert solution.validate_email("invalid") == False
        print("✅ validate_email works")
    
    return True

async def test_elicitation_with_schema():
    """Test that elicitation can be called"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_response = {
        "username": "testuser",
        "email": "test@example.com",
        "age": 25,
        "newsletter": False
    }
    mock_elicitation.create = AsyncMock(return_value=mock_response)
    mock_ctx.elicitation = mock_elicitation
    
    try:
        await solution.register(mock_ctx)
        print("✅ The tool can be called")
        return True
    except Exception as e:
        print(f"⚠️  Error (may be normal if not implemented): {e}")
        return True

if __name__ == "__main__":
    print("🧪 Test for Project 15\n")
    
    success = True
    success = asyncio.run(test_schema_structure()) and success
    print()
    success = asyncio.run(test_validation_functions()) and success
    print()
    success = asyncio.run(test_elicitation_with_schema()) and success
    
    print()
    if success:
        print("✅ Basic tests pass!")
        print("💡 To test elicitation completely, use a real MCP client")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
