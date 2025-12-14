"""
Test script for project 26
This script verifies the port scanner
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
    
    if not hasattr(solution, 'PortInfo'):
        print("The model 'PortInfo' does not exist")
        return False
    
    if not hasattr(solution, 'ScanResult'):
        print("The model 'ScanResult' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_scan_ports():
    """Test the scan_ports tool"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'scans'):
        solution.scans.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.scan_ports("192.168.1.1", None, "quick", mock_ctx)
        
        if not isinstance(result, solution.ScanResult):
            print(f"The result should be a ScanResult, but it's {type(result)}")
            return False
        
        if result.target != "192.168.1.1":
            print(f"The target should be '192.168.1.1', but it's '{result.target}'")
            return False
        
        if len(result.ports) == 0:
            print("The scan should detect at least one port")
            return False
        
        print("scan_ports works")
        return True
    
    except Exception as e:
        print(f"Error during scan: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_analyze_services():
    """Test the analyze_services tool"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'scans'):
        solution.scans.clear()
    
    mock_ctx = AsyncMock()
    
    # Create a scan first
    await solution.scan_ports("192.168.1.1", None, "quick", mock_ctx)
    
    try:
        result = await solution.analyze_services(0, mock_ctx)
        
        if not isinstance(result, dict):
            print(f"The result should be a dict, but it's {type(result)}")
            return False
        
        print("analyze_services works")
        return True
    
    except Exception as e:
        print(f"Error during analysis: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 26\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing scan_ports...")
    success = asyncio.run(test_scan_ports()) and success
    print()
    
    print("Testing analyze_services...")
    success = asyncio.run(test_analyze_services()) and success
    print()
    
    if success:
        print("All tests pass!")
        print("You've created a functional port scanner!")
    else:
        print("Some tests failed. Check your code!")
        sys.exit(1)
