"""
Test script for project 29
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
    if not hasattr(solution, 'Session'):
        print("Model 'Session' does not exist")
        return False
    print("Models exist")
    return True

async def test_create_session():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    if hasattr(solution, 'sessions'):
        solution.sessions.clear()
    mock_ctx = AsyncMock()
    try:
        result = await solution.create_session("ssh", "192.168.1.1", "root", None, mock_ctx)
        if not isinstance(result, solution.Session):
            return False
        print("create_session works")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("Test for Project 29\n")
    success = test_models_exist()
    print()
    success = asyncio.run(test_create_session()) and success
    print()
    if success:
        print("All tests pass!")
    else:
        print("Some tests failed")
        sys.exit(1)
