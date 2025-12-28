"""
Test script for Python Exercise 09
Tests resource templates
"""

import sys
import importlib.util

def test_uri_parsing():
    """Test URI parsing"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_09.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test valid URI
    result = exercise.parse_config_uri("config://app/version")
    if result is None:
        print("Should parse valid config URI")
        return False

    if result.get("section") != "app" or result.get("key") != "version":
        print("Should extract section and key correctly")
        return False

    # Test invalid URI
    result2 = exercise.parse_config_uri("info://app/version")
    if result2 is not None:
        print("Should return None for non-config URI")
        return False

    print("✓ URI parsing works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 09 - Resource Templates\n")

    tests = [test_uri_parsing]
    passed = sum(1 for test in tests if test())

    print(f"Results: {passed}/{len(tests)} tests passed")

    if passed == len(tests):
        print("🎉 All tests passed! You're ready for MCP Project 09!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
