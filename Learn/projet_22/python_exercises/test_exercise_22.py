"""
Test script for Python Exercise 22
Tests advanced MCP concepts
"""

import sys
import importlib.util

def test_concept():
    """Test the main concept"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_22.py")
    exercise = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False
    
    # Basic test - just check that main function exists
    if not hasattr(exercise, 'main'):
        print("main function is not defined")
        return False
    
    print("✓ Basic structure is correct")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 22 - Advanced MCP Concepts\n")
    
    tests = [test_concept]
    passed = sum(1 for test in tests if test())
    
    print(f"Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! You're ready for MCP Project 22!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
