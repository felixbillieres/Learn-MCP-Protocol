"""
Test script for project 03
This script verifies that Pydantic models are properly defined and work
"""

import sys
import importlib.util
import asyncio
from pydantic import ValidationError

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

    # Check that models exist
    if not hasattr(solution, 'Message'):
        print("The class 'Message' does not exist")
        return False

    if not hasattr(solution, 'MessageResponse'):
        print("The class 'MessageResponse' does not exist")
        return False

    # Check that they are Pydantic models
    from pydantic import BaseModel

    if not issubclass(solution.Message, BaseModel):
        print("'Message' must inherit from BaseModel")
        return False

    if not issubclass(solution.MessageResponse, BaseModel):
        print("'MessageResponse' must inherit from BaseModel")
        return False

    print("Pydantic models are properly defined!")
    return True

def test_message_validation():
    """Test that the Message model validates correctly"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Test valid creation
    try:
        msg = solution.Message(
            sender="Alice",
            recipient="Bob",
            content="Hello !"
        )
        if msg.priority != "normal":
            print(f"The default priority should be 'normal', but it's '{msg.priority}'")
            return False
        print("Message created successfully (default priority)")
    except Exception as e:
        print(f"Error during creation of a valid Message: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test with explicit priority
    try:
        msg = solution.Message(
            sender="Alice",
            recipient="Bob",
            content="Urgent!",
            priority="high"
        )
        if msg.priority != "high":
            print(f"The priority should be 'high', but it's '{msg.priority}'")
            return False
        print("Message created with explicit priority")
    except Exception as e:
        print(f"Error during creation with priority: {e}")
        return False

    # Test validation (missing fields)
    try:
        msg = solution.Message(sender="Alice")  # Missing recipient and content
        print("The model should reject an incomplete message")
        return False
    except ValidationError:
        print("Validation works: rejects incomplete messages")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

    return True

async def test_tool_execution():
    """Test that the tool works"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Create a message
    message = solution.Message(
        sender="Alice",
        recipient="Bob",
        content="Test message",
        priority="high"
    )

    # Call the tool
    try:
        result = await solution.send_message(message)

        # Check the type
        if not isinstance(result, solution.MessageResponse):
            print(f"The result should be a MessageResponse, but it's {type(result)}")
            return False

        # Check fields
        if not hasattr(result, 'message_id') or not isinstance(result.message_id, int):
            print("'message_id' should be an int")
            return False

        if result.sender != "Alice":
            print(f"The sender should be 'Alice', but it's '{result.sender}'")
            return False

        if result.recipient != "Bob":
            print(f"The recipient should be 'Bob', but it's '{result.recipient}'")
            return False

        if not hasattr(result, 'send_date') or not isinstance(result.send_date, str):
            print("'send_date' should be a string")
            return False

        print(f"Tool works! Message ID: {result.message_id}, Date: {result.send_date}")
        return True

    except Exception as e:
        print(f"Error during tool execution: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 03\n")

    success = True
    success = test_models_exist() and success
    print()

    success = test_message_validation() and success
    print()

    print("Testing tool execution...")
    success = asyncio.run(test_tool_execution()) and success

    print()
    if success:
        print("All tests pass!")
        print("You've learned to use Pydantic models in MCP!")
    else:
        print("Some tests failed. Check your code!")
        sys.exit(1)
