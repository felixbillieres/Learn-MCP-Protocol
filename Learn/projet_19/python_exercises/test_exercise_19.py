"""
Test script for Python Exercise 19
Tests agentic workflows with tools
"""

import sys
import importlib.util

def test_tool_system():
    """Test the tool system"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_19.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test tool creation
    def sample_func(x, y):
        return x + y

    tool = exercise.Tool("test", "Test tool", sample_func, {"type": "object", "properties": {}})
    assert tool.name == "test"
    assert tool.execute({"x": 1, "y": 2}) == 3

    # Test tool schema
    schema = tool.get_schema()
    assert schema["name"] == "test"
    assert "description" in schema

    print("✓ Tool system works correctly")
    return True

def test_tool_registry():
    """Test tool registry functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_19.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    registry = exercise.ToolRegistry()

    # Create and register tool
    def calc(a, b):
        return a + b

    tool = exercise.Tool("calc", "Calculator", calc, {})
    registry.register_tool(tool)

    # Test tool retrieval
    tools = registry.get_available_tools()
    assert len(tools) == 1
    assert tools[0]["name"] == "calc"

    # Test tool execution
    result = registry.execute_tool("calc", {"a": 5, "b": 3})
    assert result == 8

    # Test unknown tool
    result = registry.execute_tool("unknown", {})
    assert "not found" in result

    print("✓ Tool registry works correctly")
    return True

def test_agent_planning():
    """Test agent planning and reasoning"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_19.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    registry = exercise.create_sample_tools()
    agent = exercise.Agent(registry)

    # Test planning for calculation query
    plan = agent.plan("What is 10 + 20?")
    assert "calculator" in plan["analysis"]["tools_needed"]

    # Test planning for search query
    plan = agent.plan("Find information about Python")
    assert "search" in plan["analysis"]["tools_needed"]

    print("✓ Agent planning works correctly")
    return True

def test_agent_execution():
    """Test agent execution of plans"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_19.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    registry = exercise.create_sample_tools()
    agent = exercise.Agent(registry)

    # Test execution
    result = exercise.solve_with_agent("What is 10 + 20?", agent)
    assert "Calculation result" in result or "30" in result

    print("✓ Agent execution works correctly")
    return True

def test_sample_tools():
    """Test the sample tools"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_19.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test calculator
    assert exercise.calculator("add", 5, 3) == 8
    assert exercise.calculator("multiply", 4, 5) == 20

    # Test search
    result = exercise.search("python")
    assert "programming language" in result

    # Test formatter
    assert exercise.formatter("hello", "uppercase") == "HELLO"

    print("✓ Sample tools work correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 19 - Agentic Workflows with Tools\n")

    tests = [
        test_tool_system,
        test_tool_registry,
        test_agent_planning,
        test_agent_execution,
        test_sample_tools
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            print()

    print(f"Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! You're ready for MCP Project 19!")
        print("You've mastered agentic workflows, tool integration, and autonomous problem-solving!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
