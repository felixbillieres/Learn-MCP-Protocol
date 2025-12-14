"""
Test script for project 10
Note: Subscriptions are difficult to test without a real MCP client
This test verifies the basic structure
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

async def test_list_resources():
    """Test that list_resources works"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.list_resources()
        if not isinstance(result, list):
            print("list_resources should return a list")
            return False
        print("list_resources works")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

async def test_update_status():
    """Test that update_status works"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    try:
        result = await solution.update_status("stopped", 100, mock_ctx)

        # Check that status was updated
        if solution.status_content["status"] != "stopped":
            print("Status should be updated")
            return False

        print("update_status works")
        return True
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 10\n")
    print("Note: Subscriptions require a real MCP client to be fully tested\n")

    success = True
    success = asyncio.run(test_list_resources()) and success
    print()
    success = asyncio.run(test_update_status()) and success

    print()
    if success:
        print("Basic tests pass!")
        print("Subscriptions require a real MCP client to be tested")
    else:
        print("Some tests failed.")
        sys.exit(1)
