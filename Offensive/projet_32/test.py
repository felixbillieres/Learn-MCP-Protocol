"""
Test script for project 32
This script verifies the pentest automation framework
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
    
    if not hasattr(solution, 'Pentest'):
        print("The model 'Pentest' does not exist")
        return False
    
    if not hasattr(solution, 'PentestPhase'):
        print("The model 'PentestPhase' does not exist")
        return False
    
    if not hasattr(solution, 'Finding'):
        print("The model 'Finding' does not exist")
        return False
    
    if not hasattr(solution, 'Report'):
        print("The model 'Report' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_create_pentest():
    """Test pentest creation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'pentests'):
        solution.pentests.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.create_pentest("192.168.1.0/24", mock_ctx)
        
        if not isinstance(result, solution.Pentest):
            print(f"create_pentest should return a Pentest, but returned {type(result)}")
            return False
        
        if result.target != "192.168.1.0/24":
            print(f"Pentest target should be '192.168.1.0/24', but is '{result.target}'")
            return False
        
        if len(solution.pentests) != 1:
            print(f"Pentest should be added, but list contains {len(solution.pentests)} pentests")
            return False
        
        print("create_pentest works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_pentest_phases():
    """Test pentest phase execution"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'pentests'):
        solution.pentests.clear()
    
    mock_ctx = AsyncMock()
    
    pentest = await solution.create_pentest("192.168.1.1", mock_ctx)
    pentest_id = pentest.id
    
    try:
        # Test reconnaissance phase
        result = await solution.execute_reconnaissance(pentest_id, mock_ctx)
        if not isinstance(result, solution.Pentest):
            print("execute_reconnaissance should return a Pentest")
            return False
        
        # Test prepare exploits
        result = await solution.prepare_exploits(pentest_id, mock_ctx)
        if not isinstance(result, solution.Pentest):
            print("prepare_exploits should return a Pentest")
            return False
        
        # Test deploy payloads
        result = await solution.deploy_payloads(pentest_id, mock_ctx)
        if not isinstance(result, solution.Pentest):
            print("deploy_payloads should return a Pentest")
            return False
        
        print("Pentest phases work")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_execute_exploits_with_elicitation():
    """Test exploit execution with elicitation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'pentests'):
        solution.pentests.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"confirm": True})
    mock_ctx.elicitation = mock_elicitation
    
    pentest = await solution.create_pentest("192.168.1.1", mock_ctx)
    
    try:
        result = await solution.execute_exploits(pentest.id, mock_ctx)
        
        if not isinstance(result, solution.Pentest):
            print(f"execute_exploits should return a Pentest, but returned {type(result)}")
            return False
        
        print("execute_exploits with elicitation works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_complete_pentest_workflow():
    """Test complete pentest workflow"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'pentests'):
        solution.pentests.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"confirm": True})
    mock_ctx.elicitation = mock_elicitation
    
    pentest = await solution.create_pentest("192.168.1.1", mock_ctx)
    
    try:
        # Execute all phases
        await solution.execute_reconnaissance(pentest.id, mock_ctx)
        await solution.prepare_exploits(pentest.id, mock_ctx)
        await solution.deploy_payloads(pentest.id, mock_ctx)
        await solution.execute_exploits(pentest.id, mock_ctx)
        await solution.establish_persistence(pentest.id, mock_ctx)
        await solution.configure_c2(pentest.id, mock_ctx)
        await solution.achieve_objectives(pentest.id, mock_ctx)
        
        # Generate report
        report = await solution.generate_report(pentest.id, mock_ctx)
        
        if not isinstance(report, solution.Report):
            print(f"generate_report should return a Report, but returned {type(report)}")
            return False
        
        print("Complete pentest workflow works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 32\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing create_pentest...")
    success = asyncio.run(test_create_pentest()) and success
    print()
    
    print("Testing pentest phases...")
    success = asyncio.run(test_pentest_phases()) and success
    print()
    
    print("Testing execute_exploits with elicitation...")
    success = asyncio.run(test_execute_exploits_with_elicitation()) and success
    print()
    
    print("Testing complete workflow...")
    success = asyncio.run(test_complete_pentest_workflow()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional pentest automation framework!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
