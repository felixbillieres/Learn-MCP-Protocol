"""
Test script for Python Exercise 12
Tests dynamic prompt arguments
"""

import sys
import importlib.util

def test_dynamic_prompt():
    """Test the DynamicPrompt class"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_12.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'DynamicPrompt'):
        print("DynamicPrompt class is not defined")
        return False

    # Test creating a prompt
    prompt = exercise.DynamicPrompt("Hello {name}!", {"name": {"required": True}})

    # Test validation - missing required arg
    try:
        prompt.validate_arguments({})
        print("Should have raised error for missing required argument")
        return False
    except ValueError:
        pass

    # Test validation - valid args
    try:
        prompt.validate_arguments({"name": "Alice"})
    except ValueError:
        print("Should not raise error for valid arguments")
        return False

    # Test formatting
    result = prompt.format_message({"name": "Alice"})
    if result != "Hello Alice!":
        print(f"Should format to 'Hello Alice!', got '{result}'")
        return False

    print("✓ DynamicPrompt works correctly")
    return True

def test_prompt_creation():
    """Test prompt creation functions"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_12.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'create_code_review_prompt'):
        print("create_code_review_prompt function is not defined")
        return False

    # Test code review prompt
    code_prompt = exercise.create_code_review_prompt()
    if not isinstance(code_prompt, exercise.DynamicPrompt):
        print("create_code_review_prompt should return a DynamicPrompt")
        return False

    # Test with valid args
    result = code_prompt.format_message({"language": "Python", "code": "print('hello')"})
    if "Python" not in result or "print('hello')" not in result:
        print("Code review prompt should include language and code")
        return False

    print("✓ Prompt creation functions work correctly")
    return True

def test_execute_prompt():
    """Test the execute_prompt function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_12.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'execute_prompt'):
        print("execute_prompt function is not defined")
        return False

    # Test execution
    prompt = exercise.create_summary_prompt()
    result = exercise.execute_prompt(prompt, {"topic": "AI"})

    if "AI" not in result["content"]["text"]:
        print("Should include the topic in result content")
        return False

    print("✓ execute_prompt works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 12 - Dynamic Prompt Arguments\n")

    tests = [
        test_dynamic_prompt,
        test_prompt_creation,
        test_execute_prompt
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            print()

    print(f"Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! You're ready for MCP Project 12!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
