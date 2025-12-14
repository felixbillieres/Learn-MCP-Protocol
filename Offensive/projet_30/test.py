"""
Test script for project 30
This script verifies the exploitation framework
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
    
    if not hasattr(solution, 'TargetInfo'):
        print("The model 'TargetInfo' does not exist")
        return False
    
    if not hasattr(solution, 'Exploit'):
        print("The model 'Exploit' does not exist")
        return False
    
    if not hasattr(solution, 'ExploitChain'):
        print("The model 'ExploitChain' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_analyze_target():
    """Test target analysis with elicitation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Mock elicitation
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_response = {
        "ip": "192.168.1.100",
        "os": "Linux",
        "services": ["ssh", "http"]
    }
    mock_elicitation.create = AsyncMock(return_value=mock_response)
    mock_ctx.elicitation = mock_elicitation
    
    try:
        result = await solution.analyze_target(mock_ctx)
        
        if not isinstance(result, solution.TargetInfo):
            print(f"analyze_target should return TargetInfo, but returned {type(result)}")
            return False
        
        print("analyze_target works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_create_chain():
    """Test exploit chain creation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'chains'):
        solution.chains.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"ip": "192.168.1.1", "os": "Linux"})
    mock_ctx.elicitation = mock_elicitation
    
    target = await solution.analyze_target(mock_ctx)
    
    try:
        result = await solution.create_chain(target, mock_ctx)
        
        if not isinstance(result, solution.ExploitChain):
            print(f"create_chain should return ExploitChain, but returned {type(result)}")
            return False
        
        if len(solution.chains) != 1:
            print(f"Chain should be added, but list contains {len(solution.chains)} chains")
            return False
        
        print("create_chain works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_execute_chain():
    """Test exploit chain execution"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'chains'):
        solution.chains.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"ip": "192.168.1.1", "os": "Linux"})
    mock_ctx.elicitation = mock_elicitation
    
    target = await solution.analyze_target(mock_ctx)
    chain = await solution.create_chain(target, mock_ctx)
    
    try:
        result = await solution.execute_chain(chain.id, mock_ctx)
        
        if not isinstance(result, solution.ExploitChain):
            print(f"execute_chain should return ExploitChain, but returned {type(result)}")
            return False
        
        if hasattr(result, 'status') and result.status != "executed":
            print("Chain status should be 'executed' after execution")
            return False
        
        print("execute_chain works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_generate_payload():
    """Test payload generation using sampling"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"ip": "192.168.1.1", "os": "Linux"})
    mock_ctx.elicitation = mock_elicitation
    
    # Mock sampling
    mock_sampling = MagicMock()
    mock_response = MagicMock()
    mock_response.content.text = "payload_code_here"
    mock_sampling.create_message = AsyncMock(return_value=mock_response)
    mock_ctx.sampling = mock_sampling
    
    target = await solution.analyze_target(mock_ctx)
    
    try:
        result = await solution.generate_payload("exploit_123", target, mock_ctx)
        
        if not isinstance(result, str):
            print(f"generate_payload should return a string, but returned {type(result)}")
            return False
        
        if len(result) == 0:
            print("Generated payload should not be empty")
            return False
        
        print("generate_payload works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 30\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing analyze_target...")
    success = asyncio.run(test_analyze_target()) and success
    print()
    
    print("Testing create_chain...")
    success = asyncio.run(test_create_chain()) and success
    print()
    
    print("Testing execute_chain...")
    success = asyncio.run(test_execute_chain()) and success
    print()
    
    print("Testing generate_payload...")
    success = asyncio.run(test_generate_payload()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional exploitation framework!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
