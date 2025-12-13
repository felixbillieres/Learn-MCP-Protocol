"""
Test script for project 31
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
    if not hasattr(solution, 'Beacon'):
        print("Model 'Beacon' does not exist")
        return False
    print("Models exist")
    return True

if __name__ == "__main__":
    print("Test Project 31\n")
    success = test_models_exist()
    print()
    if success:
        print("All tests pass!")
    else:
        print("Some tests failed")
        sys.exit(1)

