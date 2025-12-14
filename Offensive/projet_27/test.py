"""
Test script for project 27
This script verifies the payload manager
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
    
    if not hasattr(solution, 'Payload'):
        print("The model 'Payload' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_create_payload():
    """Test payload creation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'payloads'):
        solution.payloads.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.create_payload(
            "test_payload", "shell", "linux", "x64", "#!/bin/bash\nwhoami",
            "Test description", ["test"], mock_ctx
        )
        
        if not isinstance(result, solution.Payload):
            print(f"create_payload should return a Payload, but returned {type(result)}")
            return False
        
        if result.name != "test_payload":
            print(f"Payload name should be 'test_payload', but is '{result.name}'")
            return False
        
        if len(solution.payloads) != 1:
            print(f"Payload should be added, but list contains {len(solution.payloads)} payloads")
            return False
        
        print("create_payload works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_list_payloads():
    """Test listing payloads with filters"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'payloads'):
        solution.payloads.clear()
    
    mock_ctx = AsyncMock()
    
    # Create multiple payloads
    p1 = await solution.create_payload("shell_linux", "shell", "linux", "x64", "code", ctx=mock_ctx)
    p2 = await solution.create_payload("shell_windows", "shell", "windows", "x64", "code", ctx=mock_ctx)
    p3 = await solution.create_payload("meterpreter_linux", "meterpreter", "linux", "x64", "code", ctx=mock_ctx)
    
    try:
        # Test list all
        all_payloads = await solution.list_payloads(None, None, None, mock_ctx)
        if len(all_payloads) != 3:
            print(f"Should return 3 payloads, but returned {len(all_payloads)}")
            return False
        
        # Test filter by type
        shell_payloads = await solution.list_payloads("shell", None, None, mock_ctx)
        if len(shell_payloads) != 2:
            print(f"Should return 2 shell payloads, but returned {len(shell_payloads)}")
            return False
        
        # Test filter by OS
        linux_payloads = await solution.list_payloads(None, "linux", None, mock_ctx)
        if len(linux_payloads) != 2:
            print(f"Should return 2 linux payloads, but returned {len(linux_payloads)}")
            return False
        
        print("list_payloads works with filters")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_payload():
    """Test getting a payload by ID"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'payloads'):
        solution.payloads.clear()
    
    mock_ctx = AsyncMock()
    
    payload = await solution.create_payload("test", "shell", "linux", "x64", "code", ctx=mock_ctx)
    payload_id = payload.id
    
    try:
        result = await solution.get_payload(payload_id, mock_ctx)
        
        if not isinstance(result, solution.Payload):
            print(f"get_payload should return a Payload, but returned {type(result)}")
            return False
        
        if result.id != payload_id:
            print(f"Payload ID should be {payload_id}, but is {result.id}")
            return False
        
        print("get_payload works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_delete_payload():
    """Test deleting a payload"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'payloads'):
        solution.payloads.clear()
    
    mock_ctx = AsyncMock()
    
    payload = await solution.create_payload("to_delete", "shell", "linux", "x64", "code", ctx=mock_ctx)
    payload_id = payload.id
    
    try:
        result = await solution.delete_payload(payload_id, mock_ctx)
        
        if not isinstance(result, bool):
            print(f"delete_payload should return a bool, but returned {type(result)}")
            return False
        
        if not result:
            print("delete_payload should return True on success")
            return False
        
        # Verify payload is removed
        payloads = await solution.list_payloads(None, None, None, mock_ctx)
        if len(payloads) != 0:
            print("Payload should be removed from the list")
            return False
        
        print("delete_payload works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_select_payload():
    """Test payload selection with elicitation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'payloads'):
        solution.payloads.clear()
    
    mock_ctx = AsyncMock()
    from unittest.mock import MagicMock
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"selected": True})
    mock_ctx.elicitation = mock_elicitation
    
    # Create some payloads
    await solution.create_payload("payload1", "shell", "linux", "x64", "code", ctx=mock_ctx)
    await solution.create_payload("payload2", "meterpreter", "linux", "x64", "code", ctx=mock_ctx)
    
    try:
        result = await solution.select_payload("linux", "x64", "shell", mock_ctx)
        
        if not isinstance(result, solution.Payload):
            print(f"select_payload should return a Payload, but returned {type(result)}")
            return False
        
        print("select_payload works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 27\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing create_payload...")
    success = asyncio.run(test_create_payload()) and success
    print()
    
    print("Testing list_payloads...")
    success = asyncio.run(test_list_payloads()) and success
    print()
    
    print("Testing get_payload...")
    success = asyncio.run(test_get_payload()) and success
    print()
    
    print("Testing delete_payload...")
    success = asyncio.run(test_delete_payload()) and success
    print()
    
    print("Testing select_payload...")
    success = asyncio.run(test_select_payload()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional payload manager!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
