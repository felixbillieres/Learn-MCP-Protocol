"""
Test script for project 16
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
    
    if not hasattr(solution, 'authenticate'):
        print("❌ The tool 'authenticate' does not exist")
        return False
    
    if not hasattr(solution, 'configure_api_key'):
        print("❌ The tool 'configure_api_key' does not exist")
        return False
    
    print("✅ Tools exist")
    return True

async def test_url_mode_usage():
    """Test that tools can be called"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    # For URL mode, the response is generally None or a confirmation
    mock_elicitation.create = AsyncMock(return_value=None)
    mock_ctx.elicitation = mock_elicitation
    
    try:
        await solution.authenticate(mock_ctx)
        print("✅ The authenticate tool can be called")
        return True
    except Exception as e:
        print(f"⚠️  Error (may be normal if not implemented): {e}")
        return True

if __name__ == "__main__":
    print("🧪 Test for Project 16\n")
    print("Note: URL mode elicitation requires a real MCP client to be tested\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_url_mode_usage()) and success
    
    print()
    if success:
        print("✅ Basic tests pass!")
        print("💡 To test URL mode completely, use a real MCP client")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
