"""
Test script for project 28
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
    if not hasattr(solution, 'CVE'):
        print("Model 'CVE' does not exist")
        return False
    print("Models exist")
    return True

async def test_rechercher_cve():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    mock_ctx = AsyncMock()
    try:
        result = await solution.rechercher_cve("CVE-2021-44228", None, mock_ctx)
        if not isinstance(result, list):
            return False
        print("rechercher_cve works")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("Test Project 28\n")
    success = test_models_exist()
    print()
    success = asyncio.run(test_rechercher_cve()) and success
    print()
    if success:
        print("All tests pass!")
    else:
        print("Some tests failed")
        sys.exit(1)

