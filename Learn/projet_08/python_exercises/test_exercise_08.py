"""
Test script for Python Exercise 08
Tests MCP resources
"""

import sys
import importlib.util

def test_resources():
    """Test resource functions"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_08.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test list_resources
    resources = exercise.list_resources()
    if not isinstance(resources, list):
        print("list_resources should return a list")
        return False

    if len(resources) == 0:
        print("Should return at least one resource")
        return False

    # Test read_resource
    try:
        content = exercise.read_resource("info://app/version")
        if content.get("text") != "1.0.0":
            print("Should return version 1.0.0")
            return False
    except Exception as e:
        print(f"Error reading resource: {e}")
        return False

    print("✓ Resources work correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 08 - MCP Resources\n")

    tests = [test_resources]
    passed = sum(1 for test in tests if test())

    print(f"Results: {passed}/{len(tests)} tests passed")

    if passed == len(tests):
        print("🎉 All tests passed! You're ready for MCP Project 08!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
