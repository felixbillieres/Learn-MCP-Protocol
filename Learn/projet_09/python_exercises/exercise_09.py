# Exercise 09: Resource Templates
# Practice URI parsing and template matching

import re

# TODO: Create a function 'parse_config_uri' that takes uri (str)
# If uri matches "config://{section}/{key}", extract section and key
# Return dict with "section" and "key", or None if no match

# TODO: Create a function 'get_config_value' that takes section (str), key (str)
# Simulate config data and return a value
# For example: if section=="app" and key=="version", return "1.0.0"

def parse_config_uri(uri: str):
    # TODO: Implement URI parsing
    pass

def get_config_value(section: str, key: str):
    # TODO: Implement config lookup
    pass

def main():
    # Test parsing "config://app/version"
    pass

if __name__ == "__main__":
    main()
