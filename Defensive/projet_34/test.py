"""
Test script for project 34
This script verifies the incident manager
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock, MagicMock

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
    
    if not hasattr(solution, 'Incident'):
        print("The model 'Incident' does not exist")
        return False
    
    if not hasattr(solution, 'IOC'):
        print("The model 'IOC' does not exist")
        return False
    
    if not hasattr(solution, 'ResponseAction'):
        print("The model 'ResponseAction' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_create_incident():
    """Test incident creation with elicitation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'incidents'):
        solution.incidents.clear()
    
    # Mock elicitation
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_response = {
        "title": "Security breach",
        "severity": "high",
        "description": "Unauthorized access detected"
    }
    mock_elicitation.create = AsyncMock(return_value=mock_response)
    mock_ctx.elicitation = mock_elicitation
    
    try:
        result = await solution.create_incident(mock_ctx)
        
        if not isinstance(result, solution.Incident):
            print(f"create_incident should return an Incident, but returned {type(result)}")
            return False
        
        if len(solution.incidents) != 1:
            print(f"Incident should be added, but list contains {len(solution.incidents)} incidents")
            return False
        
        print("create_incident works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_triage_incident():
    """Test incident triage"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'incidents'):
        solution.incidents.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"title": "Test", "severity": "low"})
    mock_ctx.elicitation = mock_elicitation
    
    incident = await solution.create_incident(mock_ctx)
    incident_id = incident.id
    
    try:
        result = await solution.triage_incident(incident_id, mock_ctx)
        
        if not isinstance(result, solution.Incident):
            print(f"triage_incident should return an Incident, but returned {type(result)}")
            return False
        
        print("triage_incident works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_add_ioc():
    """Test adding IOC to incident"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'incidents'):
        solution.incidents.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"title": "Test", "severity": "low"})
    mock_ctx.elicitation = mock_elicitation
    
    incident = await solution.create_incident(mock_ctx)
    ioc = solution.IOC(type="ip", value="1.2.3.4")
    
    try:
        result = await solution.add_ioc(incident.id, ioc, mock_ctx)
        
        if not isinstance(result, solution.Incident):
            print(f"add_ioc should return an Incident, but returned {type(result)}")
            return False
        
        print("add_ioc works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_create_and_execute_action():
    """Test creating and executing response action"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'incidents'):
        solution.incidents.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"title": "Test", "severity": "low"})
    mock_ctx.elicitation = mock_elicitation
    
    incident = await solution.create_incident(mock_ctx)
    
    try:
        # Create action
        action = await solution.create_action(incident.id, "Block IP 1.2.3.4", mock_ctx)
        
        if not isinstance(action, solution.ResponseAction):
            print(f"create_action should return ResponseAction, but returned {type(action)}")
            return False
        
        # Execute action
        executed = await solution.execute_action(action.id, mock_ctx)
        
        if not isinstance(executed, solution.ResponseAction):
            print(f"execute_action should return ResponseAction, but returned {type(executed)}")
            return False
        
        print("create_action and execute_action work")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_resolve_incident():
    """Test resolving an incident"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'incidents'):
        solution.incidents.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"title": "Test", "severity": "low"})
    mock_ctx.elicitation = mock_elicitation
    
    incident = await solution.create_incident(mock_ctx)
    
    try:
        result = await solution.resolve_incident(incident.id, mock_ctx)
        
        if not isinstance(result, solution.Incident):
            print(f"resolve_incident should return an Incident, but returned {type(result)}")
            return False
        
        if hasattr(result, 'status') and result.status != "resolved":
            print("Incident status should be 'resolved'")
            return False
        
        print("resolve_incident works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 34\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing create_incident...")
    success = asyncio.run(test_create_incident()) and success
    print()
    
    print("Testing triage_incident...")
    success = asyncio.run(test_triage_incident()) and success
    print()
    
    print("Testing add_ioc...")
    success = asyncio.run(test_add_ioc()) and success
    print()
    
    print("Testing create_action and execute_action...")
    success = asyncio.run(test_create_and_execute_action()) and success
    print()
    
    print("Testing resolve_incident...")
    success = asyncio.run(test_resolve_incident()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional incident manager!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
