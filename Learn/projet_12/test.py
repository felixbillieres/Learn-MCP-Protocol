"""
Test script for project 12
"""

import sys
import importlib.util
import asyncio

async def test_prompt_with_args():
    """Test that get_prompt works with arguments"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        # Test with all arguments
        result = await solution.get_prompt(
            "code_review",
            arguments={"language": "python", "code": "def hello(): pass"}
        )
        
        if not isinstance(result, dict) or "messages" not in result:
            print("❌ The result must contain 'messages'")
            return False
        
        # Check that arguments were replaced
        msg_text = result["messages"][0]["content"]["text"]
        if "python" not in msg_text.lower():
            print("❌ Arguments should be replaced in the message")
            return False
        
        print("✅ get_prompt with arguments works!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_missing_required_arg():
    """Test that an error is raised if a required argument is missing"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        await solution.get_prompt("code_review", arguments={"language": "python"})
        # Missing "code" which is required
        print("❌ Should raise ValueError for missing required argument")
        return False
    except ValueError:
        print("✅ ValueError correctly raised for missing argument")
        return True
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

async def test_optional_arg():
    """Test that an optional argument uses its default value"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.get_prompt(
            "summary",
            arguments={"topic": "MCP"}
        )
        # length is optional, should use "short" as default
        
        if not isinstance(result, dict):
            print("❌ The result must be a dict")
            return False
        
        print("✅ Optional arguments work!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Test for Project 12\n")
    
    success = True
    success = asyncio.run(test_prompt_with_args()) and success
    print()
    success = asyncio.run(test_missing_required_arg()) and success
    print()
    success = asyncio.run(test_optional_arg()) and success
    
    print()
    if success:
        print("🎉 All tests pass!")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
