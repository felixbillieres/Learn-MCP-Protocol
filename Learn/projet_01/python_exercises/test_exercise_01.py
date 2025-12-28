"""
Test script for Python Exercise 01
Tests basic Python concepts needed for MCP Project 01
"""

import sys
import importlib.util

def test_imports():
    """Test that required modules are imported"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_01.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure to import the datetime module!")
        return False

    # Check if datetime is imported
    if not hasattr(exercise, 'datetime') and 'datetime' not in sys.modules:
        print("The datetime module is not imported. Add: import datetime")
        return False

    print("✓ Imports are correct")
    return True

def test_variables():
    """Test that configuration variables are created correctly"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_01.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Check server_name
    if not hasattr(exercise, 'server_name'):
        print("Variable 'server_name' is not defined")
        return False
    if exercise.server_name != "MyFirstServer":
        print(f"server_name should be 'MyFirstServer', but it's '{exercise.server_name}'")
        return False

    # Check server_host
    if not hasattr(exercise, 'server_host'):
        print("Variable 'server_host' is not defined")
        return False
    if exercise.server_host != "127.0.0.1":
        print(f"server_host should be '127.0.0.1', but it's '{exercise.server_host}'")
        return False

    # Check server_port
    if not hasattr(exercise, 'server_port'):
        print("Variable 'server_port' is not defined")
        return False
    if exercise.server_port != 8000:
        print(f"server_port should be 8000, but it's {exercise.server_port}")
        return False

    print("✓ Configuration variables are correct")
    return True

def test_create_welcome_message():
    """Test the create_welcome_message function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_01.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'create_welcome_message'):
        print("Function 'create_welcome_message' is not defined")
        return False

    if not callable(exercise.create_welcome_message):
        print("'create_welcome_message' is not a function")
        return False

    # Test the function
    result = exercise.create_welcome_message("Alice")
    expected = "Welcome to MyFirstServer, Alice!"

    if result != expected:
        print(f"create_welcome_message('Alice') should return '{expected}', but returned '{result}'")
        return False

    print("✓ create_welcome_message function works correctly")
    return True

def test_get_server_info():
    """Test the get_server_info function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_01.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'get_server_info'):
        print("Function 'get_server_info' is not defined")
        return False

    if not callable(exercise.get_server_info):
        print("'get_server_info' is not a function")
        return False

    # Test the function
    result = exercise.get_server_info()

    if not isinstance(result, dict):
        print("get_server_info should return a dictionary")
        return False

    expected_keys = ['name', 'host', 'port', 'url']
    for key in expected_keys:
        if key not in result:
            print(f"Dictionary should contain key '{key}'")
            return False

    if result['name'] != "MyFirstServer":
        print(f"name should be 'MyFirstServer', but it's '{result['name']}'")
        return False

    if result['host'] != "127.0.0.1":
        print(f"host should be '127.0.0.1', but it's '{result['host']}'")
        return False

    if result['port'] != 8000:
        print(f"port should be 8000, but it's {result['port']}")
        return False

    if result['url'] != "http://127.0.0.1:8000":
        print(f"url should be 'http://127.0.0.1:8000', but it's '{result['url']}'")
        return False

    print("✓ get_server_info function works correctly")
    return True

def test_display_server_status():
    """Test the display_server_status function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_01.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'display_server_status'):
        print("Function 'display_server_status' is not defined")
        return False

    if not callable(exercise.display_server_status):
        print("'display_server_status' is not a function")
        return False

    # Test the function (capture print output)
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        result = exercise.display_server_status()

    output = f.getvalue()

    if result is not True:
        print("display_server_status should return True")
        return False

    if "Server MyFirstServer is running on http://127.0.0.1:8000" not in output:
        print("display_server_status should print the correct status message")
        print(f"Output was: {repr(output)}")
        return False

    print("✓ display_server_status function works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 01 - Basic Concepts\n")

    tests = [
        test_imports,
        test_variables,
        test_create_welcome_message,
        test_get_server_info,
        test_display_server_status
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
        print("🎉 All tests passed! You're ready for MCP Project 01!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
