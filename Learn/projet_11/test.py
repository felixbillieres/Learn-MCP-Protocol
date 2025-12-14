"""
Test script for project 11
"""

import sys
import importlib.util
import asyncio

async def test_list_prompts():
    """Test that list_prompts works"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.list_prompts()
        
        if not isinstance(result, list):
            print(f"❌ list_prompts should return a list")
            return False
        
        if len(result) < 2:
            print(f"❌ There should be at least 2 prompts, but there are {len(result)}")
            return False
        
        # Check structure
        for prompt in result:
            if "name" not in prompt:
                print("❌ Each prompt must have a 'name' field")
                return False
        
        print(f"✅ list_prompts works! {len(result)} prompts found")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_prompt():
    """Test that get_prompt works"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.get_prompt("greeting")
        
        if not isinstance(result, dict):
            print("❌ get_prompt should return a dict")
            return False
        
        if "messages" not in result:
            print("❌ The result must contain 'messages'")
            return False
        
        messages = result["messages"]
        if not isinstance(messages, list) or len(messages) == 0:
            print("❌ 'messages' must be a non-empty list")
            return False
        
        # Check message format
        msg = messages[0]
        if "role" not in msg or "content" not in msg:
            print("❌ Each message must have 'role' and 'content'")
            return False
        
        print("✅ get_prompt works!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_invalid_prompt():
    """Test that get_prompt raises an error for invalid prompt"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        await solution.get_prompt("nonexistent")
        print("❌ get_prompt should raise ValueError for non-existent prompt")
        return False
    except ValueError:
        print("✅ get_prompt correctly raises ValueError for non-existent prompt")
        return True
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Test for Project 11\n")
    
    success = True
    success = asyncio.run(test_list_prompts()) and success
    print()
    success = asyncio.run(test_get_prompt()) and success
    print()
    success = asyncio.run(test_get_invalid_prompt()) and success
    
    print()
    if success:
        print("🎉 All tests pass!")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
