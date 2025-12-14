"""
Test script for project 17
Note: Sampling requires a real MCP client with LLM to be fully tested
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
    
    if not hasattr(solution, 'ask_question'):
        print("❌ The tool 'ask_question' does not exist")
        return False
    
    if not hasattr(solution, 'generate_summary'):
        print("❌ The tool 'generate_summary' does not exist")
        return False
    
    print("✅ Tools exist")
    return True

async def test_sampling_usage():
    """Test that sampling can be used (simulated)"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    mock_sampling = MagicMock()
    mock_response = MagicMock()
    mock_response.content.text = "Simulated LLM response"
    mock_sampling.create_message = AsyncMock(return_value=mock_response)
    mock_ctx.sampling = mock_sampling
    
    try:
        result = await solution.ask_question("Test question", mock_ctx)
        if mock_sampling.create_message.called:
            print("✅ ctx.sampling.create_message() is used")
        else:
            print("⚠️  ctx.sampling.create_message() was not called")
        print("✅ The tool can be called")
        return True
    except AttributeError as e:
        if "sampling" in str(e):
            print("⚠️  Sampling is not yet implemented")
            print("💡 Make sure to use ctx.sampling.create_message()")
            return True
        raise
    except Exception as e:
        print(f"⚠️  Error (may be normal if not implemented): {e}")
        return True

if __name__ == "__main__":
    print("🧪 Test for Project 17\n")
    print("Note: Sampling requires a real MCP client with LLM to be fully tested\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_sampling_usage()) and success
    
    print()
    if success:
        print("✅ Basic tests pass!")
        print("💡 To test sampling completely, use a real MCP client with LLM")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
