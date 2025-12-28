# Exercise 15: Complex Elicitation Schemas
# Before creating complex elicitation, let's practice schema validation

import re

# TODO: Create a function called 'validate_username'
# Parameters: username (str)
# Validates: 3-20 chars, alphanumeric only
# Returns True if valid, raises ValueError if invalid

# TODO: Create a function called 'validate_email'
# Parameters: email (str)
# Validates basic email format (contains @ and .)
# Returns True if valid, raises ValueError if invalid

# TODO: Create a function called 'validate_age'
# Parameters: age (int)
# Validates: between 13 and 120
# Returns True if valid, raises ValueError if invalid

# TODO: Create a function called 'create_registration_schema'
# Returns a dict representing the JSON schema for user registration
# Include all validation rules from the project

# TODO: Create a function called 'create_order_schema'
# Returns a dict representing the JSON schema for product ordering
# Include enum validation for products

# TODO: Create a function called 'validate_elicitation_response'
# Parameters: response (dict), schema (dict)
# Validates that response matches the schema requirements
# Returns validated data or raises ValueError

def validate_username(username):
    """Validate username according to project requirements"""
    if not isinstance(username, str):
        raise ValueError("Username must be a string")

    if len(username) < 3 or len(username) > 20:
        raise ValueError("Username must be 3-20 characters long")

    if not re.match(r'^[a-zA-Z0-9]+$', username):
        raise ValueError("Username must contain only alphanumeric characters")

    return True

def validate_email(email):
    """Validate email format"""
    if not isinstance(email, str):
        raise ValueError("Email must be a string")

    if '@' not in email or '.' not in email:
        raise ValueError("Email must contain @ and . characters")

    return True

def validate_age(age):
    """Validate age range"""
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")

    if age < 13 or age > 120:
        raise ValueError("Age must be between 13 and 120")

    return True

def create_registration_schema():
    """Create JSON schema for user registration"""
    return {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "minLength": 3,
                "maxLength": 20,
                "pattern": "^[a-zA-Z0-9]+$"
            },
            "email": {
                "type": "string",
                "format": "email"
            },
            "age": {
                "type": "integer",
                "minimum": 13,
                "maximum": 120
            },
            "newsletter": {
                "type": "boolean",
                "default": False
            }
        },
        "required": ["username", "email", "age"]
    }

def create_order_schema():
    """Create JSON schema for product ordering"""
    return {
        "type": "object",
        "properties": {
            "product": {
                "type": "string",
                "enum": ["basic", "premium", "enterprise"]
            },
            "quantity": {
                "type": "integer",
                "minimum": 1,
                "maximum": 100
            },
            "express_delivery": {
                "type": "boolean"
            }
        },
        "required": ["product", "quantity"]
    }

def validate_elicitation_response(response, schema):
    """Validate elicitation response against schema"""
    if not isinstance(response, dict):
        raise ValueError("Response must be a dictionary")

    required_fields = schema.get("required", [])
    properties = schema.get("properties", {})

    # Check required fields
    for field in required_fields:
        if field not in response:
            raise ValueError(f"Missing required field: {field}")

    # Validate individual fields
    for field, value in response.items():
        if field in properties:
            field_def = properties[field]

            # Type validation
            expected_type = field_def.get("type")
            if expected_type == "string" and not isinstance(value, str):
                raise ValueError(f"Field {field} must be a string")
            elif expected_type == "integer" and not isinstance(value, int):
                raise ValueError(f"Field {field} must be an integer")
            elif expected_type == "boolean" and not isinstance(value, bool):
                raise ValueError(f"Field {field} must be a boolean")

            # Range validation
            if "minimum" in field_def and value < field_def["minimum"]:
                raise ValueError(f"Field {field} must be >= {field_def['minimum']}")
            if "maximum" in field_def and value > field_def["maximum"]:
                raise ValueError(f"Field {field} must be <= {field_def['maximum']}")

            # Enum validation
            if "enum" in field_def and value not in field_def["enum"]:
                raise ValueError(f"Field {field} must be one of: {field_def['enum']}")

    return response

def main():
    # Test your schema validation
    try:
        validate_username("testuser")
        validate_email("test@example.com")
        validate_age(25)
        print("✓ Basic validation works")
    except Exception as e:
        print(f"✗ Validation error: {e}")

if __name__ == "__main__":
    main()
