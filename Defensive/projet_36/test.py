"""
Test script for project 36
This script verifies the patch manager
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
    
    if not hasattr(solution, 'Patch'):
        print("The model 'Patch' does not exist")
        return False
    
    if not hasattr(solution, 'Vulnerability'):
        print("The model 'Vulnerability' does not exist")
        return False
    
    if not hasattr(solution, 'DeploymentPlan'):
        print("The model 'DeploymentPlan' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_list_patches():
    """Test listing patches"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'patches'):
        solution.patches.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        # Test list all
        all_patches = await solution.list_patches(None, mock_ctx)
        if not isinstance(all_patches, list):
            print(f"list_patches should return a list, but returned {type(all_patches)}")
            return False
        
        # Test filter by product
        apache_patches = await solution.list_patches("apache", mock_ctx)
        if not isinstance(apache_patches, list):
            print(f"list_patches should return a list when filtered, but returned {type(apache_patches)}")
            return False
        
        print(f"list_patches works: found {len(all_patches)} patches")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_create_deployment_plan():
    """Test creating deployment plan"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'patches'):
        solution.patches.clear()
    if hasattr(solution, 'deployment_plans'):
        solution.deployment_plans.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.create_deployment_plan(
            "patch_001",
            ["server1", "server2", "server3"],
            mock_ctx
        )
        
        if not isinstance(result, solution.DeploymentPlan):
            print(f"create_deployment_plan should return DeploymentPlan, but returned {type(result)}")
            return False
        
        if len(result.systems) != 3:
            print(f"Deployment plan should include 3 systems, but has {len(result.systems)}")
            return False
        
        print("create_deployment_plan works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_deploy_patch_with_elicitation():
    """Test patch deployment with elicitation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'deployment_plans'):
        solution.deployment_plans.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"confirm": True, "schedule": "immediate"})
    mock_ctx.elicitation = mock_elicitation
    
    plan = await solution.create_deployment_plan("patch_001", ["server1"], mock_ctx)
    
    try:
        result = await solution.deploy_patch(plan.id, mock_ctx)
        
        if not isinstance(result, solution.DeploymentPlan):
            print(f"deploy_patch should return DeploymentPlan, but returned {type(result)}")
            return False
        
        if hasattr(result, 'status') and result.status != "deployed":
            print("Plan status should be 'deployed' after deployment")
            return False
        
        print("deploy_patch works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_verify_patch():
    """Test patch verification"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.verify_patch("patch_001", "test_server", mock_ctx)
        
        if not isinstance(result, dict):
            print(f"verify_patch should return a dict, but returned {type(result)}")
            return False
        
        if "verified" not in result:
            print("Result should contain 'verified' key")
            return False
        
        print("verify_patch works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 36\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing list_patches...")
    success = asyncio.run(test_list_patches()) and success
    print()
    
    print("Testing create_deployment_plan...")
    success = asyncio.run(test_create_deployment_plan()) and success
    print()
    
    print("Testing deploy_patch...")
    success = asyncio.run(test_deploy_patch_with_elicitation()) and success
    print()
    
    print("Testing verify_patch...")
    success = asyncio.run(test_verify_patch()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional patch manager!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
