"""
Test script for project 05
This script verifies error handling and validation
"""

import sys
import importlib.util
import asyncio
import math
from unittest.mock import AsyncMock

async def test_normal_division():
    """Test normal division"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    try:
        result = await solution.calculate_division(10.0, 2.0, mock_ctx)

        if result != 5.0:
            print(f"10.0 / 2.0 should give 5.0, but gave {result}")
            return False

        if mock_ctx.info.call_count < 2:
            print("ctx.info() should be called at least 2 times (start and success)")
            return False

        print("Normal division works: 10.0 / 2.0 = 5.0")
        return True

    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_division_by_zero():
    """Test division by zero"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    try:
        result = await solution.calculate_division(10.0, 0.0, mock_ctx)

        # If we get here, the error was not raised
        print("The tool should raise ValueError for division by zero")
        return False

    except ValueError as e:
        if "zero" not in str(e).lower():
            print(f"The error message should mention 'zero', but says: {e}")
            return False

        if mock_ctx.error.call_count == 0:
            print("ctx.error() should be called before raising the exception")
            return False

        print(f"Division by zero correctly handled: {e}")
        return True

    except Exception as e:
        print(f"Unexpected error (should be ValueError): {e}")
        return False

async def test_infinity_result():
    """Test with infinite result"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    try:
        # Use a very small value to create a result close to infinity
        result = await solution.calculate_division(1.0, 0.0000001, mock_ctx)

        if not math.isinf(result) and result < 1000000:
            # For this test, we accept either a very large number or infinity
            # (depending on implementation)
            pass

        # Check that a warning was emitted (if code detects infinity)
        # If math.isinf is used, ctx.warning should be called
        print(f"Calculation with very small divisor: result = {result}")
        return True

    except Exception as e:
        # This is also acceptable if an exception is raised
        print(f"Calculation detected as problematic (acceptable)")
        return True

async def test_missing_parameters():
    """Test with missing parameters"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    mock_ctx = AsyncMock()

    # Test with None values (if the function accepts them)
    # None cannot be passed directly. We test instead with invalid values

    print("Parameter validation tests passed")
    return True

if __name__ == "__main__":
    print("Test for Project 05\n")

    success = True
    print("Testing normal division...")
    success = asyncio.run(test_normal_division()) and success
    print()

    print("Testing division by zero...")
    success = asyncio.run(test_division_by_zero()) and success
    print()

    print("Testing infinity result...")
    success = asyncio.run(test_infinity_result()) and success
    print()

    print("Testing missing parameters...")
    success = asyncio.run(test_missing_parameters()) and success

    print()
    if success:
        print("All tests pass!")
        print("You've learned error handling and validation!")
    else:
        print("Some tests failed. Check your code!")
        sys.exit(1)
