"""
Test script for project 25 (FINAL)
This script verifies the complete project manager
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_server_exists():
    """Test that the server exists"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error during import: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    if not hasattr(solution, 'mcp_server'):
        print("❌ The server does not exist")
        return False
    
    print("✅ The server exists")
    return True

def test_models_should_exist():
    """Test that models should be defined (check if exist)"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Check for common model names (Project, Task)
    has_models = (
        hasattr(solution, 'Project') or 
        hasattr(solution, 'Task') or
        any('Project' in str(attr) or 'Task' in str(attr) for attr in dir(solution) if attr[0].isupper())
    )
    
    if has_models:
        print("✅ Models are defined")
    else:
        print("💡 Define Project and Task models")
    
    return True

def test_tools_should_exist():
    """Test that tools should be defined (check if exist)"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Common tool names for project managers
    expected_tools = ['create_project', 'list_projects', 'create_task', 'list_tasks']
    found_tools = [tool for tool in expected_tools if hasattr(solution, tool)]
    
    if found_tools:
        print(f"✅ Found {len(found_tools)} tool(s): {', '.join(found_tools)}")
    else:
        print("💡 Define CRUD tools for projects and tasks")
    
    return True

def test_resources_should_exist():
    """Test that resources should be defined (check if exist)"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'list_resources'):
        print("✅ Resources are implemented")
    else:
        print("💡 Implement resources to expose project/task data")
    
    return True

def test_prompts_should_exist():
    """Test that prompts should be defined (check if exist)"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'list_prompts'):
        print("✅ Prompts are implemented")
    else:
        print("💡 Implement prompts for workflows")
    
    return True

async def test_basic_tool_execution():
    """Test that basic tools can be called if they exist"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    # Try to call common tools if they exist
    tools_to_test = ['create_project', 'list_projects']
    called = False
    
    for tool_name in tools_to_test:
        if hasattr(solution, tool_name):
            try:
                tool = getattr(solution, tool_name)
                if callable(tool):
                    await tool(mock_ctx)
                    print(f"✅ {tool_name} can be called")
                    called = True
                    break
            except Exception as e:
                print(f"⚠️  {tool_name} exists but may not be fully implemented: {e}")
                called = True
                break
    
    if not called:
        print("💡 Implement and test your tools")
    
    return True

if __name__ == "__main__":
    print("🧪 Test for Project 25 (FINAL)\n")
    print("🎉 FINAL PROJECT! Use all the features you've learned!\n")
    
    success = True
    success = test_server_exists() and success
    print()
    
    success = test_models_should_exist() and success
    print()
    
    success = test_tools_should_exist() and success
    print()
    
    success = test_resources_should_exist() and success
    print()
    
    success = test_prompts_should_exist() and success
    print()
    
    print("Testing basic tool execution...")
    success = asyncio.run(test_basic_tool_execution()) and success
    print()
    
    if success:
        print("✅ Basic structure tests pass!")
        print("💡 This is the final project - implement all features:")
        print("   - Tools for CRUD operations")
        print("   - Resources to expose data")
        print("   - Prompts for workflows")
        print("   - Elicitation for interactions")
        print("   - Authorization for security")
        print("   - Well-structured, production-quality code")
    else:
        print("❌ Some tests failed.")
        sys.exit(1)
