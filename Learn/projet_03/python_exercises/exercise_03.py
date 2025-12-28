# Exercise 03: Pydantic Models
# Before using Pydantic in MCP tools, let's practice creating models

# TODO: Import BaseModel and Field from pydantic
from pydantic import BaseModel, Field

# TODO: Create a Pydantic model called 'Person'
# Fields:
# - name: str (required, description "Person's full name")
# - age: int (required, minimum 0, maximum 150, description "Age in years")
# - email: str | None (optional, description "Email address")
# - occupation: str (required, default "Unemployed", description "Job title")

# TODO: Create a Pydantic model called 'Address'
# Fields:
# - street: str (required, description "Street address")
# - city: str (required, description "City name")
# - postal_code: str (required, description "Postal code")
# - country: str (required, default "France", description "Country")

# TODO: Create a Pydantic model called 'Contact'
# Fields:
# - person: Person (required, description "Person information")
# - address: Address (required, description "Address information")
# - phone: str | None (optional, description "Phone number")

# TODO: Create a function called 'create_person'
# Parameters: name (str), age (int), email (str | None) = None, occupation (str) = None
# If occupation is None, don't pass it (let default be used)
# Return a Person instance

# TODO: Create a function called 'create_contact'
# Parameters: person_data (dict), address_data (dict), phone (str | None) = None
# Create Person and Address instances from the dicts
# Return a Contact instance

# TODO: Create a function called 'validate_contacts'
# Parameter: contacts (list of Contact)
# For each contact, print validation info
# Return list of valid contacts (all should be valid if created correctly)

def main():
    # Test your models here
    pass

if __name__ == "__main__":
    main()
