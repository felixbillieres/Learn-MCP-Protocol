"""
Test script for Python Exercise 05
Tests error handling and validation needed for MCP Project 05
"""

import sys
import asyncio
import importlib.util

def test_safe_divide():
    """Test the safe_divide function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_05.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'safe_divide'):
        print("safe_divide function is not defined")
        return False

    ctx = exercise.MockContext()

    async def test_valid_division():
        result = await exercise.safe_divide(10, 2, ctx)
        if result != 5:
            print(f"10 / 2 should be 5, got {result}")
            return False
        return True

    async def test_division_by_zero():
        ctx2 = exercise.MockContext()
        try:
            await exercise.safe_divide(10, 0, ctx2)
            print("Should have raised ValueError for division by zero")
            return False
        except ValueError as e:
            if "zero" not in str(e):
                print(f"Error message should mention zero, got: {e}")
                return False
        return True

    async def test_none_dividend():
        ctx3 = exercise.MockContext()
        try:
            await exercise.safe_divide(None, 2, ctx3)
            print("Should have raised ValueError for None dividend")
            return False
        except ValueError as e:
            if "Dividend" not in str(e):
                print(f"Error message should mention Dividend, got: {e}")
                return False
        return True

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        if not loop.run_until_complete(test_valid_division()):
            return False
        if not loop.run_until_complete(test_division_by_zero()):
            return False
        if not loop.run_until_complete(test_none_dividend()):
            return False
    finally:
        loop.close()

    print("✓ safe_divide function works correctly")
    return True

def test_validate_and_process():
    """Test the validate_and_process function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_05.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'validate_and_process'):
        print("validate_and_process function is not defined")
        return False

    async def test_valid_data():
        ctx = exercise.MockContext()
        data = {"name": "Alice", "age": 30, "email": "alice@example.com"}
        required = ["name", "age"]

        result = await exercise.validate_and_process(data, required, ctx)

        if result != data:
            print("Should return the same data dict")
            return False

        return True

    async def test_missing_field():
        ctx = exercise.MockContext()
        data = {"name": "Bob"}
        required = ["name", "age"]

        try:
            await exercise.validate_and_process(data, required, ctx)
            print("Should have raised ValueError for missing age")
            return False
        except ValueError as e:
            if "age" not in str(e):
                print(f"Error should mention age, got: {e}")
                return False

        return True

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        if not loop.run_until_complete(test_valid_data()):
            return False
        if not loop.run_until_complete(test_missing_field()):
            return False
    finally:
        loop.close()

    print("✓ validate_and_process function works correctly")
    return True

def test_process_numbers():
    """Test the process_numbers function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_05.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'process_numbers'):
        print("process_numbers function is not defined")
        return False

    async def test_operations():
        ctx = exercise.MockContext()
        numbers = [1, 2, 3, 4, 5]

        # Test sum
        result = await exercise.process_numbers(numbers, "sum", ctx)
        if result != 15:
            print(f"Sum should be 15, got {result}")
            return False

        # Test average
        result = await exercise.process_numbers(numbers, "average", ctx)
        if result != 3:
            print(f"Average should be 3, got {result}")
            return False

        return True

    async def test_empty_list():
        ctx = exercise.MockContext()
        try:
            await exercise.process_numbers([], "sum", ctx)
            print("Should have raised ValueError for empty list")
            return False
        except ValueError as e:
            if "empty" not in str(e):
                print(f"Error should mention empty, got: {e}")
                return False
        return True

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        if not loop.run_until_complete(test_operations()):
            return False
        if not loop.run_until_complete(test_empty_list()):
            return False
    finally:
        loop.close()

    print("✓ process_numbers function works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 05 - Error Handling and Validation\n")

    tests = [
        test_safe_divide,
        test_validate_and_process,
        test_process_numbers
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
        print("🎉 All tests passed! You're ready for MCP Project 05!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
