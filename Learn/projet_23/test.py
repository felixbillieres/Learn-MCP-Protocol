"""
Test script for project 23
This script verifies roots functionality
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock, MagicMock

def test_server_exists():
    """Test that server exists"""
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

def test_helper_functions_exist():
    """Test that helper functions exist"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if not hasattr(solution, 'get_authorized_roots'):
        print("get_authorized_roots function does not exist")
        return False
    
    if not hasattr(solution, 'is_path_authorized'):
        print("is_path_authorized function does not exist")
        return False
    
    print("Helper functions exist")
    return True

async def test_list_files():
    """Test listing files in authorized roots"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    # Mock roots if available
    if hasattr(mock_ctx, 'roots'):
        mock_roots = MagicMock()
        mock_roots.list = AsyncMock(return_value=["/safe/path1", "/safe/path2"])
        mock_ctx.roots = mock_roots
    
    try:
        if hasattr(solution, 'list_files'):
            result = await solution.list_files(mock_ctx)
            
            if not isinstance(result, list):
                print(f"list_files should return a list, but returned {type(result)}")
                return False
            
            print("list_files works")
            return True
        else:
            print("list_files function does not exist")
            return False
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_read_file():
    """Test reading authorized files"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    # Mock roots if available
    if hasattr(mock_ctx, 'roots'):
        mock_roots = MagicMock()
        mock_roots.list = AsyncMock(return_value=["/safe/path"])
        mock_ctx.roots = mock_roots
    
    try:
        if hasattr(solution, 'read_file'):
            # Try to read a file (should check authorization first)
            result = await solution.read_file("/safe/path/file.txt", mock_ctx)
            
            if not isinstance(result, str):
                print(f"read_file should return a string, but returned {type(result)}")
                return False
            
            print("read_file works")
            return True
        else:
            print("read_file function does not exist")
            return False
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_path_authorization():
    """Test path authorization logic"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    try:
        if hasattr(solution, 'is_path_authorized'):
            roots = ["/safe/path", "/another/safe"]
            
            # Test authorized path
            result1 = solution.is_path_authorized("/safe/path/file.txt", roots)
            if result1 is not True:
                print("Path under authorized root should be authorized")
                return False
            
            # Test unauthorized path
            result2 = solution.is_path_authorized("/unsafe/path/file.txt", roots)
            if result2 is not False:
                print("Path outside authorized roots should not be authorized")
                return False
            
            print("Path authorization logic works")
            return True
        else:
            print("is_path_authorized function does not exist")
            return False
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 23\n")
    
    success = True
    success = test_server_exists() and success
    print()
    
    success = test_helper_functions_exist() and success
    print()
    
    success = test_path_authorization() and success
    print()
    
    print("Testing list_files...")
    success = asyncio.run(test_list_files()) and success
    print()
    
    print("Testing read_file...")
    success = asyncio.run(test_read_file()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've implemented roots functionality!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
