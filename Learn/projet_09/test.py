"""
Test script for project 09
"""

import sys
import importlib.util
import asyncio

async def test_list_resource_templates():
    """Test that list_resource_templates works"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.list_resource_templates()

        if not isinstance(result, list):
            print(f"list_resource_templates should return a list")
            return False

        if len(result) == 0:
            print("There should be at least one template")
            return False

        # Check structure
        for template in result:
            if "uriTemplate" not in template:
                print("Each template must have 'uriTemplate'")
                return False
            if "{" in template["uriTemplate"] and "}" in template["uriTemplate"]:
                print(f"Template found: {template['uriTemplate']}")

        print(f"list_resource_templates works! {len(result)} templates found")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_template_resource():
    """Test that read_resource handles templates"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        # Test with config template
        result = await solution.read_resource("config://database/host")

        if not isinstance(result, dict) or "contents" not in result:
            print("The result must contain 'contents'")
            return False

        print("read_resource handles config:// templates")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_file_template():
    """Test with file template"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        result = await solution.read_resource("file://readme.txt")

        if not isinstance(result, dict) or "contents" not in result:
            print("The result must contain 'contents'")
            return False

        print("read_resource handles file:// templates")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 09\n")

    success = True
    success = asyncio.run(test_list_resource_templates()) and success
    print()
    success = asyncio.run(test_read_template_resource()) and success
    print()
    success = asyncio.run(test_read_file_template()) and success

    print()
    if success:
        print("All tests pass!")
    else:
        print("Some tests failed.")
        sys.exit(1)
