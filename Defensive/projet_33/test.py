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

async def test_collecter_evenement():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    if hasattr(solution, 'events'):
        solution.events.clear()
    mock_ctx = AsyncMock()
    try:
        result = await solution.collecter_evenement(
            "192.168.1.1", "login", "high", {"user": "admin"}, mock_ctx
        )
        if not isinstance(result, solution.SecurityEvent):
            return False
        print("collecter_evenement works")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("Test Project 33\n")
    success = test_models_exist()
    print()
    success = asyncio.run(test_collecter_evenement()) and success
    print()
    if success:
        print("All tests pass!")
    else:
        print("Some tests failed")
        sys.exit(1)

