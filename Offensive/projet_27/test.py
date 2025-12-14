"""
Test script for project 27
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
    if not hasattr(solution, 'Payload'):
        print("The model 'Payload' does not exist")
        return False
    print("Models exist")
    return True

async def test_create_payload():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    if hasattr(solution, 'payloads'):
        solution.payloads.clear()
    mock_ctx = AsyncMock()
    try:
        result = await solution.create_payload(
            "test", "shell", "linux", "x64", "#!/bin/bash\nwhoami",
            None, [], mock_ctx
        )
        if not isinstance(result, solution.Payload):
            return False
        print("create_payload works")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("Test for Project 27\n")
    success = test_models_exist()
    print()
    success = asyncio.run(test_create_payload()) and success
    print()
    if success:
        print("Tests pass!")
    else:
        print("Tests failed")
        sys.exit(1)
