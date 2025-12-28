"""
Test script for Python Exercise 06
Tests complex types needed for MCP Project 06
"""

import sys
import importlib.util

def test_product_model():
    """Test the Product model"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_06.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'Product'):
        print("Product model is not defined")
        return False

    # Test creating products
    try:
        p1 = exercise.Product(id=1, name="Laptop", price=999.99, tags=["electronics", "computer"])
        p2 = exercise.Product(id=2, name="Book", price=19.99, metadata={"author": "Alice"})

        assert p1.name == "Laptop"
        assert p1.tags == ["electronics", "computer"]
        assert p2.metadata["author"] == "Alice"
    except Exception as e:
        print(f"Error creating products: {e}")
        return False

    print("✓ Product model works correctly")
    return True

def test_filter_products_by_tag():
    """Test filtering products by tag"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_06.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'filter_products_by_tag'):
        print("filter_products_by_tag function is not defined")
        return False

    # Create test products
    products = [
        exercise.Product(id=1, name="Laptop", price=999, tags=["electronics"]),
        exercise.Product(id=2, name="Phone", price=599, tags=["electronics", "mobile"]),
        exercise.Product(id=3, name="Book", price=20, tags=["reading"])
    ]

    result = exercise.filter_products_by_tag(products, "electronics")

    if len(result) != 2:
        print(f"Should find 2 electronics products, got {len(result)}")
        return False

    print("✓ filter_products_by_tag works correctly")
    return True

def test_calculate_total_price():
    """Test price calculation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_06.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'calculate_total_price'):
        print("calculate_total_price function is not defined")
        return False

    products = [
        exercise.Product(id=1, name="A", price=10),
        exercise.Product(id=2, name="B", price=20)
    ]

    # Test with default tax (20% + 20% = 24, total = 30 * 1.2 = 36)
    total = exercise.calculate_total_price(products)
    if abs(total - 36) > 0.01:
        print(f"Total should be 36, got {total}")
        return False

    # Test with custom tax (10% + 10% = 20, total = 30 * 1.1 = 33)
    total_custom = exercise.calculate_total_price(products, 0.1)
    if abs(total_custom - 33) > 0.01:
        print(f"Total with custom tax should be 33, got {total_custom}")
        return False

    print("✓ calculate_total_price works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 06 - Complex Types\n")

    tests = [
        test_product_model,
        test_filter_products_by_tag,
        test_calculate_total_price
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
        print("🎉 All tests passed! You're ready for MCP Project 06!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
