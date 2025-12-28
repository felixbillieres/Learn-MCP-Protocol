# Exercise 14: Elicitation
# Before using elicitation in MCP, let's practice requesting user input

class ElicitationManager:
    def request_info(self, schema):
        """Simulate requesting information from user"""
        print(f"Requesting information: {schema.get('title', 'Unknown')}")
        return self.simulate_response(schema)

    def validate_response(self, response, schema):
        """Validate response against schema"""
        required_fields = []
        for field_name, field_def in schema.get('properties', {}).items():
            if field_def.get('required', False):
                required_fields.append(field_name)

        for field in required_fields:
            if field not in response:
                raise ValueError(f"Missing required field: {field}")

        return True

    def simulate_response(self, schema):
        """Simulate a user response"""
        # Simulate valid responses based on schema
        response = {}
        properties = schema.get('properties', {})

        if 'name' in properties:
            response['name'] = 'John Doe'
        if 'age' in properties:
            response['age'] = 30
        if 'email' in properties:
            response['email'] = 'john@example.com'
        if 'theme' in properties:
            response['theme'] = 'dark'
        if 'notifications' in properties:
            response['notifications'] = True

        return response

def create_profile_elicitation():
    """Create schema for profile elicitation"""
    return {
        "title": "User Profile",
        "type": "object",
        "properties": {
            "name": {"type": "string", "title": "Name", "required": True},
            "age": {"type": "integer", "title": "Age", "required": True},
            "email": {"type": "string", "title": "Email", "required": False}
        }
    }

def create_preferences_elicitation():
    """Create schema for preferences elicitation"""
    return {
        "title": "User Preferences",
        "type": "object",
        "properties": {
            "theme": {
                "type": "string",
                "enum": ["dark", "light", "auto"],
                "title": "Theme",
                "required": True
            },
            "notifications": {"type": "boolean", "title": "Notifications", "required": True}
        }
    }

def simulate_elicitation(elicitation_schema):
    """Simulate the complete elicitation process"""
    manager = ElicitationManager()
    response = manager.request_info(elicitation_schema)
    manager.validate_response(response, elicitation_schema)
    return response

class ElicitationManager:
    def request_info(self, schema):
        # TODO: Simulate requesting information
        pass

    def validate_response(self, response, schema):
        # TODO: Validate response against schema
        pass

def create_profile_elicitation():
    # TODO: Create profile schema
    pass

def create_preferences_elicitation():
    # TODO: Create preferences schema
    pass

def simulate_elicitation(elicitation_schema):
    # TODO: Simulate user response
    pass

def main():
    # Test elicitation
    pass

if __name__ == "__main__":
    main()
