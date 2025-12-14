"""
Test script for project 07 (FINAL PROJECT)
This script tests all features of the task manager
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_basic_structure():
    """Test that the basic structure is correct"""

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
    if not hasattr(solution, 'Task'):
        print("The model 'Task' does not exist")
        return False

    if not hasattr(solution, 'TaskStatistics'):
        print("The model 'TaskStatistics' does not exist")
        return False

    # Check the list
    if not hasattr(solution, 'tasks'):
        print("The list 'tasks' does not exist")
        return False

    print("Basic structure correct")
    return True

async def test_create_task():
    """Test task creation"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    # Reset
    solution.tasks.clear()
    mock_ctx = AsyncMock()

    try:
        result = await solution.create_task(
            title="My first task",
            description="Test description",
            priority="high",
            tags=["test", "important"],
            ctx=mock_ctx
        )

        if not isinstance(result, solution.Task):
            print(f"The result should be a Task, but it's {type(result)}")
            return False

        if result.title != "My first task":
            print("The title is not correct")
            return False

        if len(solution.tasks) != 1:
            print(f"The task should be added, but the list contains {len(solution.tasks)} elements")
            return False

        print("create_task works")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_list_tasks():
    """Test list and filters"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    solution.tasks.clear()
    mock_ctx = AsyncMock()

    # Create some tasks
    t1 = await solution.create_task("Task 1", None, "high", ["a"], mock_ctx)
    t2 = await solution.create_task("Task 2", None, "normal", ["b"], mock_ctx)
    t3 = await solution.create_task("Task 3", None, "high", ["a"], mock_ctx)

    await solution.mark_completed(t1.id, True, mock_ctx)

    try:
        # Test list all
        all_tasks = await solution.list_tasks(None, None, None, mock_ctx)
        if len(all_tasks) != 3:
            print(f"Should return 3 tasks, but returned {len(all_tasks)}")
            return False

        # Test filter by completed
        completed = await solution.list_tasks(True, None, None, mock_ctx)
        if len(completed) != 1:
            print(f"Should return 1 completed task, but returned {len(completed)}")
            return False

        # Test filter by priority
        high_priority = await solution.list_tasks(None, "high", None, mock_ctx)
        if len(high_priority) != 2:
            print(f"Should return 2 high priority tasks, but returned {len(high_priority)}")
            return False

        # Test filter by tag
        tag_a = await solution.list_tasks(None, None, "a", mock_ctx)
        if len(tag_a) != 2:
            print(f"Should return 2 tasks with tag 'a', but returned {len(tag_a)}")
            return False

        print("list_tasks works with all filters")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_update_task():
    """Test task update"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    solution.tasks.clear()
    mock_ctx = AsyncMock()

    t1 = await solution.create_task("Original title", "Original desc", "normal", [], mock_ctx)

    try:
        updated = await solution.update_task(
            t1.id,
            title="Updated title",
            priority="high",
            ctx=mock_ctx
        )

        if updated.title != "Updated title":
            print("Title should be updated")
            return False

        if updated.priority != "high":
            print("Priority should be updated")
            return False

        if updated.description != "Original desc":
            print("Description should remain unchanged")
            return False

        print("update_task works")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_delete_task():
    """Test task deletion"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    solution.tasks.clear()
    mock_ctx = AsyncMock()

    t1 = await solution.create_task("Task to delete", None, "normal", [], mock_ctx)
    task_id = t1.id

    try:
        deleted = await solution.delete_task(task_id, mock_ctx)

        if not deleted:
            print("delete_task should return True")
            return False

        if len(solution.tasks) != 0:
            print("The task should be removed from the list")
            return False

        print("delete_task works")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_get_statistics():
    """Test statistics"""

    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)

    solution.tasks.clear()
    mock_ctx = AsyncMock()

    # Create varied tasks
    t1 = await solution.create_task("Task 1", None, "high", ["a"], mock_ctx)
    t2 = await solution.create_task("Task 2", None, "normal", ["b"], mock_ctx)
    t3 = await solution.create_task("Task 3", None, "high", ["a"], mock_ctx)

    await solution.mark_completed(t1.id, True, mock_ctx)

    try:
        stats = await solution.get_statistics(mock_ctx)

        if stats.total != 3:
            print(f"Total should be 3, but it's {stats.total}")
            return False

        if stats.completed != 1:
            print(f"Completed should be 1, but it's {stats.completed}")
            return False

        if stats.in_progress != 2:
            print(f"In progress should be 2, but it's {stats.in_progress}")
            return False

        print("get_statistics works")
        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 07 (FINAL PROJECT)\n")

    success = True
    success = test_basic_structure() and success
    print()

    print("Testing create_task...")
    success = asyncio.run(test_create_task()) and success
    print()

    print("Testing list_tasks...")
    success = asyncio.run(test_list_tasks()) and success
    print()

    print("Testing update_task...")
    success = asyncio.run(test_update_task()) and success
    print()

    print("Testing delete_task...")
    success = asyncio.run(test_delete_task()) and success
    print()

    print("Testing get_statistics...")
    success = asyncio.run(test_get_statistics()) and success

    print()
    if success:
        print("🎉 All tests pass!")
        print("You've completed the final beginner project!")
        print("You now know how to create a complete MCP server!")
    else:
        print("Some tests failed. Check your code!")
        sys.exit(1)
