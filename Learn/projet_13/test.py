"""
Test script for project 13
"""

import sys
import importlib.util
import asyncio

async def test_multiple_messages():
    """Test that tutorial returns multiple messages"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.get_prompt("tutorial", arguments={"topic": "MCP"})
        
        if not isinstance(result, dict) or "messages" not in result:
            print("❌ The result must contain 'messages'")
            return False
        
        messages = result["messages"]
        if len(messages) < 2:
            print(f"❌ tutorial should return at least 2 messages, but returned {len(messages)}")
            return False
        
        print(f"✅ tutorial returns {len(messages)} messages!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_resource_reference():
    """Test that code_analysis references a resource"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        result = await solution.get_prompt(
            "code_analysis",
            arguments={"code": "def test(): pass"}
        )
        
        if not isinstance(result, dict) or "messages" not in result:
            print("❌ The result must contain 'messages'")
            return False
        
        # Check that a resource is referenced
        messages = result["messages"]
        has_resource = False
        for msg in messages:
            content = msg.get("content", {})
            if isinstance(content, dict) and content.get("type") == "resource":
                has_resource = True
                break
        
        if not has_resource:
            print("❌ code_analysis should reference a resource")
            return False
        
        print("✅ code_analysis correctly references a resource!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Test for Project 13\n")
    
    success = True
    success = asyncio.run(test_multiple_messages()) and success
    print()
    success = asyncio.run(test_resource_reference()) and success
    
    print()
    if success:
        print("🎉 All tests pass!")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
