"""
Test script for project 19
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

async def test_tools_exist():
    """Test that all tools exist"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    tools = ["calculate", "search_info", "convert_unit", "agent_solver"]
    for tool_name in tools:
        if not hasattr(solution, tool_name):
            print(f"❌ The tool '{tool_name}' does not exist")
            return False
    
    print("✅ All tools exist")
    return True

async def test_tools_for_llm():
    """Test that TOOLS_FOR_LLM is defined"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'TOOLS_FOR_LLM'):
        print("❌ TOOLS_FOR_LLM is not defined")
        return False
    
    if not isinstance(solution.TOOLS_FOR_LLM, list):
        print("❌ TOOLS_FOR_LLM must be a list")
        return False
    
    print(f"✅ TOOLS_FOR_LLM is defined with {len(solution.TOOLS_FOR_LLM)} tools")
    return True

if __name__ == "__main__":
    print("🧪 Test for Project 19\n")
    
    success = True
    success = asyncio.run(test_tools_exist()) and success
    print()
    success = asyncio.run(test_tools_for_llm()) and success
    
    print()
    if success:
        print("✅ Basic tests pass!")
        print("💡 To test agentic workflows, use a real MCP client with LLM")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
