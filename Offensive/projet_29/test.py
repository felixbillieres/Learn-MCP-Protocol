"""
Test script for project 29
This script verifies the pentest session manager
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
    
    if not hasattr(solution, 'Session'):
        print("The model 'Session' does not exist")
        return False
    
    if not hasattr(solution, 'Credential'):
        print("The model 'Credential' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_create_session():
    """Test session creation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'sessions'):
        solution.sessions.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.create_session("ssh", "192.168.1.1", "root", None, mock_ctx)
        
        if not isinstance(result, solution.Session):
            print(f"create_session should return a Session, but returned {type(result)}")
            return False
        
        if result.target != "192.168.1.1":
            print(f"Session target should be '192.168.1.1', but is '{result.target}'")
            return False
        
        if len(solution.sessions) != 1:
            print(f"Session should be added, but list contains {len(solution.sessions)} sessions")
            return False
        
        print("create_session works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_list_sessions():
    """Test listing sessions with filters"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'sessions'):
        solution.sessions.clear()
    
    mock_ctx = AsyncMock()
    
    # Create multiple sessions
    s1 = await solution.create_session("ssh", "192.168.1.1", "root", None, mock_ctx)
    s2 = await solution.create_session("rdp", "192.168.1.2", "admin", None, mock_ctx)
    s3 = await solution.create_session("ssh", "192.168.1.3", "user", None, mock_ctx)
    
    try:
        # Test list all
        all_sessions = await solution.list_sessions(None, None, mock_ctx)
        if len(all_sessions) != 3:
            print(f"Should return 3 sessions, but returned {len(all_sessions)}")
            return False
        
        # Test filter by type
        ssh_sessions = await solution.list_sessions(None, "ssh", mock_ctx)
        if len(ssh_sessions) != 2:
            print(f"Should return 2 ssh sessions, but returned {len(ssh_sessions)}")
            return False
        
        print("list_sessions works with filters")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_session():
    """Test getting session details"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'sessions'):
        solution.sessions.clear()
    
    mock_ctx = AsyncMock()
    
    s1 = await solution.create_session("ssh", "192.168.1.1", "root", None, mock_ctx)
    session_id = s1.id
    
    try:
        result = await solution.get_session(session_id, mock_ctx)
        
        if not isinstance(result, solution.Session):
            print(f"get_session should return a Session, but returned {type(result)}")
            return False
        
        if result.id != session_id:
            print(f"Session ID should be {session_id}, but is {result.id}")
            return False
        
        print("get_session works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_close_session():
    """Test closing a session"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'sessions'):
        solution.sessions.clear()
    
    mock_ctx = AsyncMock()
    
    s1 = await solution.create_session("ssh", "192.168.1.1", "root", None, mock_ctx)
    session_id = s1.id
    
    try:
        result = await solution.close_session(session_id, mock_ctx)
        
        if not isinstance(result, bool):
            print(f"close_session should return a bool, but returned {type(result)}")
            return False
        
        if not result:
            print("close_session should return True on success")
            return False
        
        # Check that session status changed
        session = await solution.get_session(session_id, mock_ctx)
        if hasattr(session, 'status') and session.status != "closed":
            print("Session status should be 'closed' after closing")
            return False
        
        print("close_session works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 29\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing create_session...")
    success = asyncio.run(test_create_session()) and success
    print()
    
    print("Testing list_sessions...")
    success = asyncio.run(test_list_sessions()) and success
    print()
    
    print("Testing get_session...")
    success = asyncio.run(test_get_session()) and success
    print()
    
    print("Testing close_session...")
    success = asyncio.run(test_close_session()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional session manager!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
