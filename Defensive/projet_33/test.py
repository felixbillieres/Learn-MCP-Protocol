"""
Test script for project 33
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_models_exist():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error: {e}")
        return False
    if not hasattr(solution, 'SecurityEvent'):
        print("Model 'SecurityEvent' does not exist")
        return False
    print("Models exist")
    return True

async def test_collect_event():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    mock_ctx = AsyncMock()
    try:
        result = await solution.collect_event(
            "firewall", "blocked", "high", {"ip": "1.2.3.4"}, mock_ctx
        )
        if not isinstance(result, solution.SecurityEvent):
            return False
        print("collect_event works")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("Test for Project 33\n")
    success = test_models_exist()
    print()
    success = asyncio.run(test_collect_event()) and success
    print()
    if success:
        print("All tests pass!")
    else:
        print("Some tests failed")
        sys.exit(1)
