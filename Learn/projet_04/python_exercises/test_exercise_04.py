"""
Test script for Python Exercise 04
Tests Context and logging needed for MCP Project 04
"""

import sys
import asyncio
import importlib.util

def test_context_logging():
    """Test Context logging functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_04.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'MockContext'):
        print("MockContext class is not defined")
        return False

    # Test logging
    ctx = exercise.MockContext()

    async def test_logging():
        await ctx.info("Test info")
        await ctx.warning("Test warning")
        await ctx.error("Test error")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(test_logging())
    loop.close()

    if len(ctx.logs) != 3:
        print(f"Should have 3 log entries, got {len(ctx.logs)}")
        return False

    print("✓ Context logging works correctly")
    return True

def test_process_file():
    """Test the process_file function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_04.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'process_file'):
        print("process_file function is not defined")
        return False

    ctx = exercise.MockContext()

    async def test_success():
        result = await exercise.process_file("test.txt", ctx)

        if not isinstance(result, dict):
            print("process_file should return a dict")
            return False

        if result.get("status") != "processed":
            print("Status should be 'processed'")
            return False

        return True

    async def test_warning():
        ctx2 = exercise.MockContext()
        result = await exercise.process_file("test.doc", ctx2)

        # Should have warning in logs
        warning_found = any("Warning:" in log for log in ctx2.logs)
        if not warning_found:
            print("Should log warning for non-.txt file")
            return False

        return True

    async def test_error():
        ctx3 = exercise.MockContext()
        try:
            await exercise.process_file("error.txt", ctx3)
            print("Should have raised ValueError for error.txt")
            return False
        except ValueError:
            pass  # Expected

        # Should have error in logs
        error_found = any("ERROR:" in log for log in ctx3.logs)
        if not error_found:
            print("Should log error before raising exception")
            return False

        return True

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        if not loop.run_until_complete(test_success()):
            return False
        if not loop.run_until_complete(test_warning()):
            return False
        if not loop.run_until_complete(test_error()):
            return False
    finally:
        loop.close()

    print("✓ process_file function works correctly")
    return True

def test_calculate_with_logging():
    """Test the calculate_with_logging function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_04.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'calculate_with_logging'):
        print("calculate_with_logging function is not defined")
        return False

    ctx = exercise.MockContext()

    async def test_calculations():
        # Test addition
        result = await exercise.calculate_with_logging(5, 3, "add", ctx)
        if result != 8:
            print(f"5 + 3 should be 8, got {result}")
            return False

        # Test large result warning
        ctx2 = exercise.MockContext()
        result = await exercise.calculate_with_logging(100, 200, "multiply", ctx2)
        warning_found = any("Large result" in log for log in ctx2.logs)
        if not warning_found:
            print("Should warn about large result")
            return False

        return True

    async def test_invalid_operation():
        ctx3 = exercise.MockContext()
        try:
            await exercise.calculate_with_logging(5, 3, "invalid", ctx3)
            print("Should have raised ValueError for invalid operation")
            return False
        except ValueError:
            pass  # Expected

        error_found = any("ERROR:" in log for log in ctx3.logs)
        if not error_found:
            print("Should log error for invalid operation")
            return False

        return True

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        if not loop.run_until_complete(test_calculations()):
            return False
        if not loop.run_until_complete(test_invalid_operation()):
            return False
    finally:
        loop.close()

    print("✓ calculate_with_logging function works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 04 - Context and Logging\n")

    tests = [
        test_context_logging,
        test_process_file,
        test_calculate_with_logging
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
        print("🎉 All tests passed! You're ready for MCP Project 04!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
