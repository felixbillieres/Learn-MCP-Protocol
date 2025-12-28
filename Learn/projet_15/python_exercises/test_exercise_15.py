"""
Test script for Python Exercise 15
Tests complex elicitation schemas
"""

import sys
import importlib.util

def test_validation_functions():
    """Test individual validation functions"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_15.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test username validation
    try:
        exercise.validate_username("testuser123")
        exercise.validate_username("ab")  # Too short
        print("Should have failed for short username")
        return False
    except ValueError:
        pass

    try:
        exercise.validate_username("test-user")  # Invalid chars
        print("Should have failed for invalid characters")
        return False
    except ValueError:
        pass

    # Test email validation
    try:
        exercise.validate_email("test@example.com")
        exercise.validate_email("invalid-email")  # Missing @
        print("Should have failed for invalid email")
        return False
    except ValueError:
        pass

    # Test age validation
    try:
        exercise.validate_age(25)
        exercise.validate_age(10)  # Too young
        print("Should have failed for age too low")
        return False
    except ValueError:
        pass

    print("✓ Validation functions work correctly")
    return True

def test_schemas():
    """Test schema creation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_15.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test registration schema
    reg_schema = exercise.create_registration_schema()
    if "properties" not in reg_schema:
        print("Registration schema should have properties")
        return False

    if "username" not in reg_schema["properties"]:
        print("Registration schema should have username property")
        return False

    # Test order schema
    order_schema = exercise.create_order_schema()
    product_prop = order_schema["properties"]["product"]
    if "enum" not in product_prop:
        print("Product should have enum validation")
        return False

    if "basic" not in product_prop["enum"]:
        print("Product enum should include 'basic'")
        return False

    print("✓ Schema creation works correctly")
    return True

def test_response_validation():
    """Test response validation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_15.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test valid response
    schema = exercise.create_registration_schema()
    valid_response = {
        "username": "testuser",
        "email": "test@example.com",
        "age": 25
    }

    try:
        result = exercise.validate_elicitation_response(valid_response, schema)
        if result != valid_response:
            print("Should return the validated response")
            return False
    except Exception as e:
        print(f"Valid response should pass: {e}")
        return False

    # Test invalid response (missing required field)
    invalid_response = {
        "username": "testuser",
        "email": "test@example.com"
        # missing age
    }

    try:
        exercise.validate_elicitation_response(invalid_response, schema)
        print("Should have failed for missing required field")
        return False
    except ValueError:
        pass

    print("✓ Response validation works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 15 - Complex Elicitation Schemas\n")

    tests = [
        test_validation_functions,
        test_schemas,
        test_response_validation
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
        print("🎉 All tests passed! You're ready for MCP Project 15!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
