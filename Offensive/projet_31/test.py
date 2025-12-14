"""
Test script for project 31
This script verifies the C2 manager
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_models_exist():
    """Test that models exist"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error during import: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    if not hasattr(solution, 'Beacon'):
        print("The model 'Beacon' does not exist")
        return False
    
    if not hasattr(solution, 'Task'):
        print("The model 'Task' does not exist")
        return False
    
    if not hasattr(solution, 'Command'):
        print("The model 'Command' does not exist")
        return False
    
    print("Models exist")
    return True

def test_validate_token():
    """Test token validation helper"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'validate_token'):
        assert solution.validate_token("Bearer valid_token", "beacons:read") == True
        assert solution.validate_token("Bearer invalid_token", "beacons:read") == False
        assert solution.validate_token(None, "beacons:read") == False
        print("validate_token works")
    
    return True

async def test_list_beacons():
    """Test listing beacons with authorization"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'beacons'):
        solution.beacons.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.list_beacons("Bearer valid_token", mock_ctx)
        
        if not isinstance(result, list):
            print(f"list_beacons should return a list, but returned {type(result)}")
            return False
        
        print(f"list_beacons works: found {len(result)} beacons")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_create_task():
    """Test creating a task for a beacon"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'beacons'):
        solution.beacons.clear()
    if hasattr(solution, 'tasks'):
        solution.tasks.clear()
    
    mock_ctx = AsyncMock()
    
    # Create a beacon first (simulated)
    if hasattr(solution, 'beacons'):
        from pydantic import BaseModel
        beacon = solution.Beacon(id="beacon_123", host="192.168.1.1", status="active")
        solution.beacons["beacon_123"] = beacon
    
    command = solution.Command(type="exec", args=["whoami"])
    
    try:
        result = await solution.create_task("beacon_123", command, "Bearer valid_token", mock_ctx)
        
        if not isinstance(result, solution.Task):
            print(f"create_task should return a Task, but returned {type(result)}")
            return False
        
        print("create_task works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_tasks():
    """Test getting tasks for a beacon"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'beacons'):
        solution.beacons.clear()
    if hasattr(solution, 'tasks'):
        solution.tasks.clear()
    
    mock_ctx = AsyncMock()
    
    # Setup beacon and task
    if hasattr(solution, 'beacons'):
        beacon = solution.Beacon(id="beacon_123", host="192.168.1.1", status="active")
        solution.beacons["beacon_123"] = beacon
    
    command = solution.Command(type="exec", args=["whoami"])
    task = await solution.create_task("beacon_123", command, "Bearer valid_token", mock_ctx)
    
    try:
        result = await solution.get_tasks("beacon_123", "Bearer valid_token", mock_ctx)
        
        if not isinstance(result, list):
            print(f"get_tasks should return a list, but returned {type(result)}")
            return False
        
        if len(result) == 0:
            print("Should return at least one task")
            return False
        
        print(f"get_tasks works: found {len(result)} tasks")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_response():
    """Test getting task response"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'beacons'):
        solution.beacons.clear()
    if hasattr(solution, 'tasks'):
        solution.tasks.clear()
    
    mock_ctx = AsyncMock()
    
    # Setup beacon and task
    if hasattr(solution, 'beacons'):
        beacon = solution.Beacon(id="beacon_123", host="192.168.1.1", status="active")
        solution.beacons["beacon_123"] = beacon
    
    command = solution.Command(type="exec", args=["whoami"])
    task = await solution.create_task("beacon_123", command, "Bearer valid_token", mock_ctx)
    task_id = task.id
    
    try:
        result = await solution.get_response(task_id, "Bearer valid_token", mock_ctx)
        
        if not isinstance(result, solution.Task):
            print(f"get_response should return a Task, but returned {type(result)}")
            return False
        
        print("get_response works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 31\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    success = test_validate_token() and success
    print()
    
    print("Testing list_beacons...")
    success = asyncio.run(test_list_beacons()) and success
    print()
    
    print("Testing create_task...")
    success = asyncio.run(test_create_task()) and success
    print()
    
    print("Testing get_tasks...")
    success = asyncio.run(test_get_tasks()) and success
    print()
    
    print("Testing get_response...")
    success = asyncio.run(test_get_response()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional C2 manager!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
