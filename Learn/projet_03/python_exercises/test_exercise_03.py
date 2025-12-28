"""
Test script for Python Exercise 03
Tests Pydantic models needed for MCP Project 03
"""

import sys
import importlib.util

def test_imports():
    """Test that Pydantic is imported correctly"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_03.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure to install pydantic: pip install pydantic")
        return False
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Check imports
    if not hasattr(exercise, 'BaseModel'):
        print("BaseModel not imported from pydantic")
        return False

    if not hasattr(exercise, 'Field'):
        print("Field not imported from pydantic")
        return False

    print("✓ Pydantic imports are correct")
    return True

def test_person_model():
    """Test the Person model"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_03.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'Person'):
        print("Person model is not defined")
        return False

    # Test creating a Person
    try:
        person = exercise.Person(name="Alice", age=30, email="alice@example.com")
        assert person.name == "Alice"
        assert person.age == 30
        assert person.email == "alice@example.com"
        assert person.occupation == "Unemployed"  # default value
    except Exception as e:
        print(f"Error creating Person: {e}")
        return False

    # Test default occupation
    try:
        person2 = exercise.Person(name="Bob", age=25)
        assert person2.occupation == "Unemployed"
    except Exception as e:
        print(f"Error with default occupation: {e}")
        return False

    # Test validation
    try:
        invalid_person = exercise.Person(name="Charlie", age=-5)
        print("Should have failed validation for negative age")
        return False
    except Exception:
        pass  # Expected to fail

    print("✓ Person model works correctly")
    return True

def test_address_model():
    """Test the Address model"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_03.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'Address'):
        print("Address model is not defined")
        return False

    # Test creating an Address
    try:
        address = exercise.Address(street="123 Main St", city="Paris", postal_code="75001")
        assert address.street == "123 Main St"
        assert address.city == "Paris"
        assert address.postal_code == "75001"
        assert address.country == "France"  # default value
    except Exception as e:
        print(f"Error creating Address: {e}")
        return False

    # Test custom country
    try:
        address2 = exercise.Address(
            street="456 Oak Ave",
            city="London",
            postal_code="SW1A 1AA",
            country="UK"
        )
        assert address2.country == "UK"
    except Exception as e:
        print(f"Error with custom country: {e}")
        return False

    print("✓ Address model works correctly")
    return True

def test_contact_model():
    """Test the Contact model"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_03.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'Contact'):
        print("Contact model is not defined")
        return False

    # Test creating a Contact
    try:
        person = exercise.Person(name="Alice", age=30)
        address = exercise.Address(street="123 Main St", city="Paris", postal_code="75001")
        contact = exercise.Contact(person=person, address=address, phone="0123456789")

        assert contact.person.name == "Alice"
        assert contact.address.city == "Paris"
        assert contact.phone == "0123456789"
    except Exception as e:
        print(f"Error creating Contact: {e}")
        return False

    print("✓ Contact model works correctly")
    return True

def test_create_person():
    """Test the create_person function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_03.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'create_person'):
        print("create_person function is not defined")
        return False

    # Test creating a person
    try:
        person = exercise.create_person("Alice", 30, "alice@example.com", "Developer")
        assert person.name == "Alice"
        assert person.age == 30
        assert person.email == "alice@example.com"
        assert person.occupation == "Developer"
    except Exception as e:
        print(f"Error in create_person: {e}")
        return False

    # Test with defaults
    try:
        person2 = exercise.create_person("Bob", 25)
        assert person2.name == "Bob"
        assert person2.age == 25
        assert person2.email is None
        assert person2.occupation == "Unemployed"
    except Exception as e:
        print(f"Error in create_person with defaults: {e}")
        return False

    print("✓ create_person function works correctly")
    return True

def test_create_contact():
    """Test the create_contact function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_03.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'create_contact'):
        print("create_contact function is not defined")
        return False

    # Test creating a contact
    try:
        person_data = {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
        address_data = {"street": "789 Pine St", "city": "Lyon", "postal_code": "69001"}

        contact = exercise.create_contact(person_data, address_data, "0987654321")

        assert contact.person.name == "Charlie"
        assert contact.address.city == "Lyon"
        assert contact.phone == "0987654321"
    except Exception as e:
        print(f"Error in create_contact: {e}")
        return False

    print("✓ create_contact function works correctly")
    return True

def test_validate_contacts():
    """Test the validate_contacts function"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_03.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    if not hasattr(exercise, 'validate_contacts'):
        print("validate_contacts function is not defined")
        return False

    # Create test contacts
    try:
        person1 = exercise.Person(name="Alice", age=30)
        address1 = exercise.Address(street="123 Main St", city="Paris", postal_code="75001")
        contact1 = exercise.Contact(person=person1, address=address1)

        person2 = exercise.Person(name="Bob", age=25, occupation="Designer")
        address2 = exercise.Address(street="456 Oak Ave", city="Marseille", postal_code="13001")
        contact2 = exercise.Contact(person=person2, address=address2, phone="0123456789")

        contacts = [contact1, contact2]

        # Test validation
        result = exercise.validate_contacts(contacts)

        if not isinstance(result, list):
            print("validate_contacts should return a list")
            return False

        if len(result) != 2:
            print(f"Should return 2 contacts, got {len(result)}")
            return False

    except Exception as e:
        print(f"Error in validate_contacts: {e}")
        return False

    print("✓ validate_contacts function works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 03 - Pydantic Models\n")

    tests = [
        test_imports,
        test_person_model,
        test_address_model,
        test_contact_model,
        test_create_person,
        test_create_contact,
        test_validate_contacts
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
        print("🎉 All tests passed! You're ready for MCP Project 03!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
