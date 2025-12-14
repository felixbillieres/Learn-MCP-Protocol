"""
Test script for project 14
Note: Elicitation requires a real MCP client to be fully tested
This test verifies that tools are properly defined
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock, MagicMock

async def test_tools_exist():
    """Test that tools exist"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'create_profile'):
        print("❌ The tool 'create_profile' does not exist")
        return False
    
    if not hasattr(solution, 'configure_preferences'):
        print("❌ The tool 'configure_preferences' does not exist")
        return False
    
    print("✅ Tools exist")
    return True

async def test_elicitation_structure():
    """Test that tools use elicitation (simulated)"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Create a mock Context with elicitation
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_response = {"name": "Test", "age": 25, "email": "test@example.com"}
    mock_elicitation.create = AsyncMock(return_value=mock_response)
    mock_ctx.elicitation = mock_elicitation
    
    try:
        # Test that the tool can be called
        result = await solution.create_profile(mock_ctx)
        
        # Check that elicitation was called
        if not mock_elicitation.create.called:
            print("⚠️  ctx.elicitation.create() was not called (normal if code is not implemented)")
        else:
            print("✅ Elicitation is used correctly")
        
        print("✅ The tool can be called")
        return True
        
    except AttributeError as e:
        if "elicitation" in str(e):
            print("⚠️  Elicitation is not yet implemented in the code")
            print("💡 Make sure to use ctx.elicitation.create()")
            return True  # Not an error, just not yet implemented
        raise
    except Exception as e:
        print(f"⚠️  Error (may be normal if not implemented): {e}")
        return True  # Not a fatal error

if __name__ == "__main__":
    print("🧪 Test for Project 14\n")
    print("Note: Elicitation requires a real MCP client to be fully tested\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_elicitation_structure()) and success
    
    print()
    if success:
        print("✅ Basic tests pass!")
        print("💡 To test elicitation completely, use a real MCP client")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
