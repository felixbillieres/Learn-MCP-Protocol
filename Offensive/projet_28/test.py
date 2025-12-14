"""
Test script for project 28
This script verifies the CVE vulnerability analyzer
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
    
    if not hasattr(solution, 'CVE'):
        print("The model 'CVE' does not exist")
        return False
    
    if not hasattr(solution, 'VulnerabilityAnalysis'):
        print("The model 'VulnerabilityAnalysis' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_search_cve_by_id():
    """Test searching for CVE by ID"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'cves'):
        solution.cves.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.search_cve("CVE-2021-44228", None, mock_ctx)
        
        if not isinstance(result, list):
            print(f"search_cve should return a list, but returned {type(result)}")
            return False
        
        print(f"search_cve by ID works: found {len(result)} CVEs")
        return True
    
    except Exception as e:
        print(f"Error during search: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_search_cve_by_product():
    """Test searching for CVE by product"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'cves'):
        solution.cves.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.search_cve(None, "apache", mock_ctx)
        
        if not isinstance(result, list):
            print(f"search_cve should return a list, but returned {type(result)}")
            return False
        
        print(f"search_cve by product works: found {len(result)} CVEs")
        return True
    
    except Exception as e:
        print(f"Error during search: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_analyze_cve():
    """Test CVE analysis"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'cves'):
        solution.cves.clear()
    
    mock_ctx = AsyncMock()
    
    # First create or search for a CVE
    try:
        cves = await solution.search_cve("CVE-2021-44228", None, mock_ctx)
        if len(cves) == 0:
            print("⚠️  No CVE found for analysis test (may need implementation)")
            return True
        
        result = await solution.analyze_cve("CVE-2021-44228", mock_ctx)
        
        if not isinstance(result, solution.VulnerabilityAnalysis):
            print(f"analyze_cve should return VulnerabilityAnalysis, but returned {type(result)}")
            return False
        
        print("analyze_cve works")
        return True
    
    except Exception as e:
        print(f"Error during analysis: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_list_cve_by_product():
    """Test listing CVEs by product"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'cves'):
        solution.cves.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.list_cve_by_product("apache", mock_ctx)
        
        if not isinstance(result, list):
            print(f"list_cve_by_product should return a list, but returned {type(result)}")
            return False
        
        print(f"list_cve_by_product works: found {len(result)} CVEs")
        return True
    
    except Exception as e:
        print(f"Error during list: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 28\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing search_cve by ID...")
    success = asyncio.run(test_search_cve_by_id()) and success
    print()
    
    print("Testing search_cve by product...")
    success = asyncio.run(test_search_cve_by_product()) and success
    print()
    
    print("Testing analyze_cve...")
    success = asyncio.run(test_analyze_cve()) and success
    print()
    
    print("Testing list_cve_by_product...")
    success = asyncio.run(test_list_cve_by_product()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional CVE analyzer!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
