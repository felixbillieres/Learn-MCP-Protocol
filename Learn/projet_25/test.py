"""Test script for project 25 (FINAL)"""
import sys
import importlib.util
import asyncio

async def test_complete_server():
    """Test that the server is complete."""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Check that the server exists
    if not hasattr(solution, 'mcp_server'):
        print("❌ The server does not exist")
        return False
    
    print("✅ The server exists")
    print("🎉 FINAL PROJECT! Use all the features you've learned!")
    return True

if __name__ == "__main__":
    print("🧪 Test for Project 25 (FINAL)\n")
    success = asyncio.run(test_complete_server())
    if success:
        print("✅ Basic test passes!")
        print("💡 This is the final project - implement all features!")
    else:
        print("❌ Test failed.")
        sys.exit(1)
