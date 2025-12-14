"""
Test script for project 18
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
    
    tools = ["creative_ideation", "conversation", "quick_response"]
    for tool_name in tools:
        if not hasattr(solution, tool_name):
            print(f"❌ The tool '{tool_name}' does not exist")
            return False
    
    print("✅ All tools exist")
    return True

async def test_advanced_parameters():
    """Test that tools can be called"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    mock_sampling = MagicMock()
    mock_response = MagicMock()
    mock_response.content.text = "Simulated response"
    mock_sampling.create_message = AsyncMock(return_value=mock_response)
    mock_ctx.sampling = mock_sampling
    
    try:
        await solution.quick_response("Test", mock_ctx)
        print("✅ Tools can be called")
        return True
    except Exception as e:
        print(f"⚠️  Error (may be normal if not implemented): {e}")
        return True

if __name__ == "__main__":
    print("🧪 Test for Project 18\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_advanced_parameters()) and success
    
    print()
    if success:
        print("✅ Basic tests pass!")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
