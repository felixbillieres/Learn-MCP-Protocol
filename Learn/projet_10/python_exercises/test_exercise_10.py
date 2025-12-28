"""
Test script for Python Exercise 10
Tests subscriptions
"""

import sys
import importlib.util

def test_subscriptions():
    """Test subscription system"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_10.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    manager = exercise.SubscriptionManager()

    # Test subscribe
    called = []
    def callback(data):
        called.append(data)

    manager.subscribe("test://uri", callback)

    # Test notify
    manager.notify("test://uri", "test data")

    if len(called) != 1 or called[0] != "test data":
        print("Notification should call callback with data")
        return False

    # Test unsubscribe
    manager.unsubscribe("test://uri", callback)
    manager.notify("test://uri", "more data")

    if len(called) != 1:
        print("Unsubscribed callback should not be called")
        return False

    print("✓ Subscriptions work correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 10 - Subscriptions\n")

    tests = [test_subscriptions]
    passed = sum(1 for test in tests if test())

    print(f"Results: {passed}/{len(tests)} tests passed")

    if passed == len(tests):
        print("🎉 All tests passed! You're ready for MCP Project 10!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
