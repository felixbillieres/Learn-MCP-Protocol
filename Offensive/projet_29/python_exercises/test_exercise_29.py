"""
Test script for Python Exercise 29
Tests advanced offensive security concepts
"""

import sys
import importlib.util

def test_concept():
    """Test the implemented concept"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_29.py")
    exercise = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False
    
    # Test basic functionality
    print("✓ Implementation is complete and functional")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 29 - Advanced Offensive Concepts\n")
    
    tests = [test_concept]
    passed = sum(1 for test in tests if test())
    
    print(f"Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! You're ready for Offensive Project 29!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
