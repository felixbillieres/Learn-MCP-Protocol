"""
Test script for project 06
This script verifies tools with complex parameters
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

    # Check models
    if not hasattr(solution, 'User'):
        print("The model 'User' does not exist")
        return False

    if not hasattr(solution, 'UserStatistics'):
        print("The model 'UserStatistics' does not exist")
        return False

    print("Models exist")
    return True

def test_user_model():
    """Test that the User model works"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    try:
        # Test creation with all fields
        user = solution.User(
            id=1,
            name="Alice",
            email="alice@example.com",
            tags=["admin", "premium"],
            score=95.5
        )

        if user.name != "Alice":
            print("The name is not correctly assigned")
            return False

        if user.score != 95.5:
            print("The score is not correctly assigned")
            return False

        # Test with default values
        user2 = solution.User(
            id=2,
            name="Bob",
            tags=[]
        )

        if user2.score != 0.0:
            print(f"The default score should be 0.0, but it's {user2.score}")
            return False

        print("The User model works correctly")
        return True

    except Exception as e:
        print(f"Error during model creation: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_add_user():
    """Test the add_user tool"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Reset the list
    if hasattr(solution, 'users'):
        solution.users.clear()

    mock_ctx = AsyncMock()

    user = solution.User(
        id=1,
        name="Alice",
        tags=["admin"]
    )

    try:
        result = await solution.add_user(user, mock_ctx)

        if not isinstance(result, solution.User):
            print(f"The result should be a User, but it's {type(result)}")
            return False

        if len(solution.users) != 1:
            print(f"The user should be added, but the list contains {len(solution.users)} elements")
            return False

        print("add_user works")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_list_users():
    """Test the list_users tool"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    if hasattr(solution, 'users'):
        solution.users.clear()

    mock_ctx = AsyncMock()

    # Add some users
    u1 = solution.User(id=1, name="Alice", tags=["admin"])
    u2 = solution.User(id=2, name="Bob", tags=["user"])
    u3 = solution.User(id=3, name="Charlie", tags=["admin", "premium"])

    await solution.add_user(u1, mock_ctx)
    await solution.add_user(u2, mock_ctx)
    await solution.add_user(u3, mock_ctx)

    try:
        # Test without filter
        all_users = await solution.list_users(None, mock_ctx)
        if len(all_users) != 3:
            print(f"Should return 3 users, but returned {len(all_users)}")
            return False

        # Test with tag filter
        admin_users = await solution.list_users("admin", mock_ctx)
        if len(admin_users) != 2:
            print(f"Should return 2 admin users, but returned {len(admin_users)}")
            return False

        print("list_users works with filters")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_statistics():
    """Test the get_statistics tool"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    if hasattr(solution, 'users'):
        solution.users.clear()

    mock_ctx = AsyncMock()

    # Add users with different scores
    u1 = solution.User(id=1, name="Alice", tags=["admin"], score=90.0)
    u2 = solution.User(id=2, name="Bob", tags=["user"], score=75.0)
    u3 = solution.User(id=3, name="Charlie", tags=["admin"], score=85.0)

    await solution.add_user(u1, mock_ctx)
    await solution.add_user(u2, mock_ctx)
    await solution.add_user(u3, mock_ctx)

    try:
        stats = await solution.get_statistics(mock_ctx)

        if not isinstance(stats, solution.UserStatistics):
            print(f"The result should be UserStatistics, but it's {type(stats)}")
            return False

        if stats.total != 3:
            print(f"Total should be 3, but it's {stats.total}")
            return False

        if stats.average_score != (90.0 + 75.0 + 85.0) / 3:
            print(f"Average score is incorrect")
            return False

        print("get_statistics works")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 06\n")

    success = True
    success = test_models_exist() and success
    print()

    success = test_user_model() and success
    print()

    print("Testing add_user...")
    success = asyncio.run(test_add_user()) and success
    print()

    print("Testing list_users...")
    success = asyncio.run(test_list_users()) and success
    print()

    print("Testing get_statistics...")
    success = asyncio.run(test_get_statistics()) and success

    print()
    if success:
        print("All tests pass!")
        print("You've learned to work with complex parameters!")
    else:
        print("Some tests failed. Check your code!")
        sys.exit(1)
