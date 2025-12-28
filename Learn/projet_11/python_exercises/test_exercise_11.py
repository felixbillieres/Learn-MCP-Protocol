"""
Test script for Python Exercise 11
Tests MCP prompts
"""

import sys
import importlib.util

def test_prompt_manager():
    """Test the PromptManager class"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_11.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'PromptManager'):
        print("PromptManager class is not defined")
        return False

    # Test creating manager
    manager = exercise.PromptManager()

    # Test adding prompt
    manager.add_prompt("test", "Test Prompt", "A test", [{"role": "user", "content": "Hello"}])

    # Test listing prompts
    prompts = manager.list_prompts()
    if not isinstance(prompts, list):
        print("list_prompts should return a list")
        return False

    if len(prompts) != 1:
        print("Should have 1 prompt after adding")
        return False

    # Test getting prompt
    prompt = manager.get_prompt("test")
    if prompt is None:
        print("Should find the added prompt")
        return False

    if prompt.get("name") != "test":
        print("Prompt should have correct name")
        return False

    print("✓ PromptManager works correctly")
    return True

def test_prompt_creation():
    """Test prompt creation functions"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_11.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'create_greeting_prompt'):
        print("create_greeting_prompt function is not defined")
        return False

    if not hasattr(exercise, 'create_help_prompt'):
        print("create_help_prompt function is not defined")
        return False

    # Test greeting prompt
    greeting = exercise.create_greeting_prompt()
    if greeting.get("name") != "greeting":
        print("Greeting prompt should have name 'greeting'")
        return False

    if "messages" not in greeting:
        print("Prompt should have messages")
        return False

    # Test help prompt
    help_prompt = exercise.create_help_prompt()
    if help_prompt.get("name") != "help":
        print("Help prompt should have name 'help'")
        return False

    print("✓ Prompt creation functions work correctly")
    return True

def test_initialize_prompts():
    """Test the initialize_prompts function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_11.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'initialize_prompts'):
        print("initialize_prompts function is not defined")
        return False

    # Test initialization
    manager = exercise.initialize_prompts()

    if not isinstance(manager, exercise.PromptManager):
        print("initialize_prompts should return a PromptManager instance")
        return False

    # Check that prompts were added
    prompts = manager.list_prompts()
    if len(prompts) != 2:
        print("Should have 2 prompts after initialization")
        return False

    print("✓ initialize_prompts works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 11 - MCP Prompts\n")

    tests = [
        test_prompt_manager,
        test_prompt_creation,
        test_initialize_prompts
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
        print("🎉 All tests passed! You're ready for MCP Project 11!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
