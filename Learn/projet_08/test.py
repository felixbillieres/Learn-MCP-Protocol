"""
Test script for project 08
"""

import sys
import importlib.util
import asyncio

async def test_list_resources():
    """Test that list_resources works"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.list_resources()

        if not isinstance(result, list):
            print(f"list_resources should return a list, but returned {type(result)}")
            return False

        if len(result) < 2:
            print(f"There should be at least 2 resources, but there are {len(result)}")
            return False

        # Check structure
        for res in result:
            if "uri" not in res:
                print("Each resource must have a 'uri' field")
                return False
            if "name" not in res:
                print("Each resource must have a 'name' field")
                return False

        print(f"list_resources works! {len(result)} resources found")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_resource():
    """Test that read_resource works"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.read_resource("config://app/settings")

        if not isinstance(result, dict):
            print(f"read_resource should return a dict")
            return False

        if "contents" not in result:
            print("The result must contain 'contents'")
            return False

        contents = result["contents"]
        if not isinstance(contents, list) or len(contents) == 0:
            print("'contents' must be a non-empty list")
            return False

        print("read_resource works!")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_invalid_resource():
    """Test that read_resource raises an error for invalid URI"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        await solution.read_resource("invalid://uri/does/not/exist")
        print("read_resource should raise ValueError for invalid URI")
        return False
    except ValueError:
        print("read_resource correctly raises ValueError for invalid URI")
        return True
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("Test for Project 08\n")

    success = True
    success = asyncio.run(test_list_resources()) and success
    print()
    success = asyncio.run(test_read_resource()) and success
    print()
    success = asyncio.run(test_read_invalid_resource()) and success

    print()
    if success:
        print("All tests pass!")
    else:
        print("Some tests failed.")
        sys.exit(1)
