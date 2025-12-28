"""
Test script for Python Exercise 02
Tests async functions and decorators needed for MCP Project 02
"""

import sys
import asyncio
import time
import importlib.util

def test_decorators():
    """Test that decorators are implemented correctly"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_02.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Check timer decorator
    if not hasattr(exercise, 'timer'):
        print("Decorator 'timer' is not defined")
        return False

    # Check logger decorator
    if not hasattr(exercise, 'logger'):
        print("Decorator 'logger' is not defined")
        return False

    # Test timer decorator
    @exercise.timer
    def test_function():
        time.sleep(0.01)
        return "test"

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        result = test_function()

    output = f.getvalue()
    if "took" not in output or "test_function" not in output:
        print("Timer decorator doesn't print execution time correctly")
        return False

    if result != "test":
        print("Timer decorator doesn't preserve function return value")
        return False

    print("✓ Decorators are implemented correctly")
    return True

def test_async_functions():
    """Test that async functions are implemented correctly"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_02.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Check say_hello_async function
    if not hasattr(exercise, 'say_hello_async'):
        print("Function 'say_hello_async' is not defined")
        return False

    if not asyncio.iscoroutinefunction(exercise.say_hello_async):
        print("'say_hello_async' is not an async function")
        return False

    # Check calculate_sum_async function
    if not hasattr(exercise, 'calculate_sum_async'):
        print("Function 'calculate_sum_async' is not defined")
        return False

    if not asyncio.iscoroutinefunction(exercise.calculate_sum_async):
        print("'calculate_sum_async' is not an async function")
        return False

    print("✓ Async functions are defined correctly")
    return True

def test_async_function_behavior():
    """Test that async functions work correctly"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_02.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    async def test_say_hello():
        result = await exercise.say_hello_async("Alice")
        expected = "Hello, Alice! How are you?"
        if result != expected:
            print(f"say_hello_async('Alice') should return '{expected}', but returned '{result}'")
            return False
        return True

    async def test_calculate_sum():
        result = await exercise.calculate_sum_async(5, 3)
        expected = 8
        if result != expected:
            print(f"calculate_sum_async(5, 3) should return {expected}, but returned {result}")
            return False
        return True

    # Run the async tests
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        success1 = loop.run_until_complete(test_say_hello())
        success2 = loop.run_until_complete(test_calculate_sum())

        if not success1 or not success2:
            return False

    finally:
        loop.close()

    print("✓ Async functions work correctly")
    return True

def test_run_calculations():
    """Test the run_calculations function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_02.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'run_calculations'):
        print("Function 'run_calculations' is not defined")
        return False

    if not callable(exercise.run_calculations):
        print("'run_calculations' is not a function")
        return False

    # Test the function
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        result = exercise.run_calculations()

    output = f.getvalue()

    if not isinstance(result, tuple) or len(result) != 2:
        print("run_calculations should return a tuple with 2 elements")
        return False

    greeting, sum_result = result

    if greeting != "Hello, Alice! How are you?":
        print(f"First element should be greeting, but got '{greeting}'")
        return False

    if sum_result != 8:
        print(f"Second element should be 8, but got {sum_result}")
        return False

    if "Hello, Alice! How are you?" not in output or "8" not in output:
        print("run_calculations should print both results")
        return False

    print("✓ run_calculations function works correctly")
    return True

def test_process_multiple_items():
    """Test the process_multiple_items function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_02.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'process_multiple_items'):
        print("Function 'process_multiple_items' is not defined")
        return False

    if not asyncio.iscoroutinefunction(exercise.process_multiple_items):
        print("'process_multiple_items' is not an async function")
        return False

    async def test_concurrent():
        items = ["Alice", "Bob", "Charlie"]
        results = await exercise.process_multiple_items(items)

        if not isinstance(results, list):
            print("process_multiple_items should return a list")
            return False

        if len(results) != 3:
            print(f"Should return 3 results, but got {len(results)}")
            return False

        expected = [
            "Hello, Alice! How are you?",
            "Hello, Bob! How are you?",
            "Hello, Charlie! How are you?"
        ]

        if results != expected:
            print(f"Expected {expected}, but got {results}")
            return False

        return True

    # Run the async test
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        success = loop.run_until_complete(test_concurrent())
        if not success:
            return False
    finally:
        loop.close()

    print("✓ process_multiple_items function works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 02 - Async Functions and Decorators\n")

    tests = [
        test_decorators,
        test_async_functions,
        test_async_function_behavior,
        test_run_calculations,
        test_process_multiple_items
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
        print("🎉 All tests passed! You're ready for MCP Project 02!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
