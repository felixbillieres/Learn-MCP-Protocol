"""
Test script for project 40 - Final Project
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_server_exists():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error: {e}")
        return False
    if not hasattr(solution, 'mcp_server'):
        print("Server does not exist")
        return False
    print("Server exists")
    return True

if __name__ == "__main__":
    print("Test Project 40 - Final Project\n")
    success = test_server_exists()
    print()
    if success:
        print("Basic structure exists!")
        print("Complete the implementation to pass all tests!")
    else:
        print("Some tests failed")
        sys.exit(1)

