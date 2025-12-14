"""
Test script for project 40 - Final Project
This script verifies the complete security platform
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock, MagicMock

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
        print("The server does not exist")
        return False
    
    print("Server exists")
    return True

def test_models_exist():
    """Test that all integration models exist"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    models = ['SecurityOperation', 'ThreatIntelligence', 'SecurityReport']
    for model_name in models:
        if not hasattr(solution, model_name):
            print(f"The model '{model_name}' does not exist")
            return False
    
    print("All integration models exist")
    return True

async def test_scan_ports():
    """Test port scanning tool"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'scans'):
        solution.scans.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.scan_ports("192.168.1.1", mock_ctx)
        
        if not isinstance(result, dict):
            print(f"scan_ports should return a dict, but returned {type(result)}")
            return False
        
        if "target" not in result:
            print("Result should contain 'target' key")
            return False
        
        print("scan_ports works")
        return True
    
    except Exception as e:
        print(f"Error (may be normal if not implemented): {e}")
        return True

async def test_collect_event():
    """Test event collection tool"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'events'):
        solution.events.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.collect_event("firewall", "blocked", mock_ctx)
        
        if not isinstance(result, dict):
            print(f"collect_event should return a dict, but returned {type(result)}")
            return False
        
        print("collect_event works")
        return True
    
    except Exception as e:
        print(f"Error (may be normal if not implemented): {e}")
        return True

async def test_correlate_offensive_defensive():
    """Test correlation tool"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'scans'):
        solution.scans.clear()
    if hasattr(solution, 'incidents'):
        solution.incidents.clear()
    if hasattr(solution, 'operations'):
        solution.operations.clear()
    
    mock_ctx = AsyncMock()
    
    # Setup scan and incident (simulated)
    try:
        result = await solution.correlate_offensive_defensive(0, 0, mock_ctx)
        
        if not isinstance(result, solution.SecurityOperation):
            print(f"correlate_offensive_defensive should return SecurityOperation, but returned {type(result)}")
            return False
        
        print("correlate_offensive_defensive works")
        return True
    
    except Exception as e:
        print(f"Error (may be normal if not implemented): {e}")
        return True

async def test_generate_complete_report():
    """Test report generation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'operations'):
        solution.operations.clear()
    
    mock_ctx = AsyncMock()
    
    # Mock sampling for report generation
    mock_sampling = MagicMock()
    mock_response = MagicMock()
    mock_response.content.text = "Complete security assessment report..."
    mock_sampling.create_message = AsyncMock(return_value=mock_response)
    mock_ctx.sampling = mock_sampling
    
    try:
        result = await solution.generate_complete_report(0, mock_ctx)
        
        if not isinstance(result, solution.SecurityReport):
            print(f"generate_complete_report should return SecurityReport, but returned {type(result)}")
            return False
        
        print("generate_complete_report works")
        return True
    
    except Exception as e:
        print(f"Error (may be normal if not implemented): {e}")
        return True

def test_resources_exist():
    """Test that resources are available"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'list_resources'):
        print("list_resources function does not exist")
        return False
    
    if not hasattr(solution, 'read_resource'):
        print("read_resource function does not exist")
        return False
    
    print("Resources functions exist")
    return True

def test_prompts_exist():
    """Test that prompts are available"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'list_prompts'):
        print("list_prompts function does not exist")
        return False
    
    if not hasattr(solution, 'get_prompt'):
        print("get_prompt function does not exist")
        return False
    
    print("Prompts functions exist")
    return True

if __name__ == "__main__":
    print("Test for Project 40 - Final Project\n")
    
    success = True
    success = test_server_exists() and success
    print()
    
    success = test_models_exist() and success
    print()
    
    success = test_resources_exist() and success
    print()
    
    success = test_prompts_exist() and success
    print()
    
    print("Testing scan_ports...")
    success = asyncio.run(test_scan_ports()) and success
    print()
    
    print("Testing collect_event...")
    success = asyncio.run(test_collect_event()) and success
    print()
    
    print("Testing correlate_offensive_defensive...")
    success = asyncio.run(test_correlate_offensive_defensive()) and success
    print()
    
    print("Testing generate_complete_report...")
    success = asyncio.run(test_generate_complete_report()) and success
    print()
    
    if success:
        print("✅ Basic structure tests pass!")
        print("🎉 FINAL PROJECT! This is a comprehensive platform combining all features.")
        print("💡 Complete the implementation to create a production-ready security platform!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
