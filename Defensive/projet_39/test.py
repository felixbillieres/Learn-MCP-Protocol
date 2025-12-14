"""
Test script for project 39
This script verifies the secrets manager
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
    
    if not hasattr(solution, 'Secret'):
        print("The model 'Secret' does not exist")
        return False
    
    if not hasattr(solution, 'AccessLog'):
        print("The model 'AccessLog' does not exist")
        return False
    
    print("Models exist")
    return True

def test_masking_helper():
    """Test masking helper function"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'mask_secret'):
        masked = solution.mask_secret("mysecret123")
        if "mysecret123" in masked:
            print("mask_secret should mask the secret value")
            return False
        if len(masked) == 0:
            print("mask_secret should return a non-empty string")
            return False
        print("mask_secret works")
    
    return True

async def test_create_secret():
    """Test secret creation with authorization"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'secrets'):
        solution.secrets.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.create_secret(
            "api_key",
            "password",
            "secret123",
            tags=["production"],
            token="Bearer valid_token",
            ctx=mock_ctx
        )
        
        if not isinstance(result, solution.Secret):
            print(f"create_secret should return Secret, but returned {type(result)}")
            return False
        
        if result.name != "api_key":
            print(f"Secret name should be 'api_key', but is '{result.name}'")
            return False
        
        print("create_secret works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_list_secrets():
    """Test listing secrets (masked)"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'secrets'):
        solution.secrets.clear()
    
    mock_ctx = AsyncMock()
    
    await solution.create_secret("secret1", "password", "value1", token="Bearer token", ctx=mock_ctx)
    await solution.create_secret("secret2", "api_key", "value2", token="Bearer token", ctx=mock_ctx)
    
    try:
        result = await solution.list_secrets("Bearer token", mock_ctx)
        
        if not isinstance(result, list):
            print(f"list_secrets should return a list, but returned {type(result)}")
            return False
        
        if len(result) != 2:
            print(f"Should return 2 secrets, but returned {len(result)}")
            return False
        
        # Check that values are masked
        for secret in result:
            if hasattr(secret, 'value') and 'value' in secret.get('value', '').lower():
                print("Secret values should be masked in list")
                return False
        
        print("list_secrets works with masking")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_secret():
    """Test getting secret with elicitation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'secrets'):
        solution.secrets.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"confirm": True, "reason": "investigation"})
    mock_ctx.elicitation = mock_elicitation
    
    secret = await solution.create_secret("test_secret", "password", "secret_value", token="Bearer token", ctx=mock_ctx)
    
    try:
        result = await solution.get_secret(secret.id if hasattr(secret, 'id') else "test_secret", "Bearer token", mock_ctx)
        
        if not isinstance(result, solution.Secret):
            print(f"get_secret should return Secret, but returned {type(result)}")
            return False
        
        print("get_secret works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_update_secret():
    """Test updating a secret"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'secrets'):
        solution.secrets.clear()
    
    mock_ctx = AsyncMock()
    
    secret = await solution.create_secret("old_secret", "password", "old_value", token="Bearer token", ctx=mock_ctx)
    secret_id = secret.id if hasattr(secret, 'id') else "old_secret"
    
    try:
        result = await solution.update_secret(secret_id, "new_value", "Bearer token", mock_ctx)
        
        if not isinstance(result, solution.Secret):
            print(f"update_secret should return Secret, but returned {type(result)}")
            return False
        
        print("update_secret works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_delete_secret():
    """Test deleting a secret"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'secrets'):
        solution.secrets.clear()
    
    mock_ctx = AsyncMock()
    
    secret = await solution.create_secret("to_delete", "password", "value", token="Bearer token", ctx=mock_ctx)
    secret_id = secret.id if hasattr(secret, 'id') else "to_delete"
    
    try:
        result = await solution.delete_secret(secret_id, "Bearer token", mock_ctx)
        
        if not isinstance(result, bool):
            print(f"delete_secret should return a bool, but returned {type(result)}")
            return False
        
        if not result:
            print("delete_secret should return True on success")
            return False
        
        # Verify secret is removed
        secrets = await solution.list_secrets("Bearer token", mock_ctx)
        if len(secrets) != 0:
            print("Secret should be removed from the list")
            return False
        
        print("delete_secret works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_view_logs():
    """Test viewing access logs"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'secrets'):
        solution.secrets.clear()
    
    mock_ctx = AsyncMock()
    
    secret = await solution.create_secret("logged_secret", "password", "value", token="Bearer token", ctx=mock_ctx)
    secret_id = secret.id if hasattr(secret, 'id') else "logged_secret"
    
    # Access the secret to generate a log
    try:
        await solution.get_secret(secret_id, "Bearer token", mock_ctx)
    except:
        pass
    
    try:
        result = await solution.view_logs(secret_id, "Bearer token", mock_ctx)
        
        if not isinstance(result, list):
            print(f"view_logs should return a list, but returned {type(result)}")
            return False
        
        print(f"view_logs works: found {len(result)} log entries")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 39\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    success = test_masking_helper() and success
    print()
    
    print("Testing create_secret...")
    success = asyncio.run(test_create_secret()) and success
    print()
    
    print("Testing list_secrets...")
    success = asyncio.run(test_list_secrets()) and success
    print()
    
    print("Testing get_secret...")
    success = asyncio.run(test_get_secret()) and success
    print()
    
    print("Testing update_secret...")
    success = asyncio.run(test_update_secret()) and success
    print()
    
    print("Testing delete_secret...")
    success = asyncio.run(test_delete_secret()) and success
    print()
    
    print("Testing view_logs...")
    success = asyncio.run(test_view_logs()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional secrets manager!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
