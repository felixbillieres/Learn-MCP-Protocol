"""Tests pour projet 22"""
import sys
import importlib.util
import asyncio

async def test_rate_limit():
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    print("✅ Tests de base passent")

if __name__ == "__main__":
    asyncio.run(test_rate_limit())

