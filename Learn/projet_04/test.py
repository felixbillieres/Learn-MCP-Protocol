"""
Test script for project 04
This script verifies that Context is properly used for logging
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_context_import():
    """Test that Context is imported"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error during import: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Check that Context is available
    try:
        from mcp.server.fastmcp import Context
        print("Context is properly importable")
    except ImportError:
        print("Cannot import Context")
        return False

    return True

async def test_tool_with_context():
    """Test that the tool properly uses Context"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Create a mock Context
    mock_ctx = AsyncMock()

    # Test with a valid file
    try:
        result = await solution.process_file("test.txt", mock_ctx)

        # Check that ctx.info was called
        if mock_ctx.info.call_count < 2:
            print(f"ctx.info() should be called at least 2 times, but was called {mock_ctx.info.call_count} times")
            return False

        # Check that the result is a dict
        if not isinstance(result, dict):
            print(f"The result should be a dict, but it's {type(result)}")
            return False

        # Check result keys
        if "file" not in result or "status" not in result:
            print(f"The result should contain 'file' and 'status'")
            return False

        print(f"Tool works with Context! Result: {result}")
        print(f"  ctx.info() called {mock_ctx.info.call_count} times")

    except Exception as e:
        print(f"Error during execution: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

async def test_tool_with_warning():
    """Test that the tool uses ctx.warning() when necessary"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    # Test with a non-.txt file (should generate a warning)
    try:
        result = await solution.process_file("test.pdf", mock_ctx)

        # Check that ctx.warning was called
        if mock_ctx.warning.call_count == 0:
            print("ctx.warning() should be called for a non-.txt file")
            return False

        print("ctx.warning() is properly used for non-.txt files")

    except Exception as e:
        print(f"Error during execution: {e}")
        return False

    return True

async def test_tool_with_error():
    """Test that the tool uses ctx.error() and raises an exception"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    # Test with the file "error.txt" (should generate an error)
    try:
        result = await solution.process_file("error.txt", mock_ctx)

        # If we get here, the error was not raised
        print("The tool should raise a ValueError for 'error.txt'")
        return False

    except ValueError:
        # This is what we expect!
        # Check that ctx.error was called
        if mock_ctx.error.call_count == 0:
            print("ctx.error() should be called before raising the exception")
            return False

        print("ctx.error() is properly used and the exception is correctly raised")
        return True

    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 04\n")

    success = True
    success = test_context_import() and success
    print()

    print("Testing execution with Context...")
    success = asyncio.run(test_tool_with_context()) and success
    print()

    print("Testing with warning...")
    success = asyncio.run(test_tool_with_warning()) and success
    print()

    print("Testing with error...")
    success = asyncio.run(test_tool_with_error()) and success

    print()
    if success:
        print("All tests pass!")
        print("You've learned to use Context for logging!")
    else:
        print("Some tests failed. Check your code!")
        sys.exit(1)
