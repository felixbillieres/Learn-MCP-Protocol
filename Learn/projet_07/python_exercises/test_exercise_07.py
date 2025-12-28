"""
Test script for Python Exercise 07
Tests final project concepts
"""

import sys
import asyncio
import importlib.util

def test_task_operations():
    """Test task creation and completion"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_07.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'create_task'):
        print("create_task function is not defined")
        return False

    async def test_create():
        ctx = exercise.MockContext()
        task = await exercise.create_task("Test task", ctx)

        if task.title != "Test task":
            print("Task title not set correctly")
            return False

        if task.completed != False:
            print("Task should start incomplete")
            return False

        return True

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        if not loop.run_until_complete(test_create()):
            return False
    finally:
        loop.close()

    print("✓ Task operations work correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 07 - Final Project Practice\n")

    tests = [test_task_operations]

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
        print("🎉 All tests passed! You're ready for MCP Project 07!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
