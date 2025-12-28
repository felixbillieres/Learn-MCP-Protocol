# Exercise 05: Error Handling and Validation
# Before implementing robust MCP tools, let's practice validation and error handling

import math
from typing import Any

# Mock Context class for exercise
class MockContext:
    def __init__(self):
        self.logs = []

    async def info(self, message: str):
        self.logs.append(f"INFO: {message}")

    async def warning(self, message: str):
        self.logs.append(f"WARNING: {message}")

    async def error(self, message: str):
        self.logs.append(f"ERROR: {message}")

# TODO: Create an async function called 'safe_divide'
# Parameters: dividend (float), divisor (float), ctx (MockContext)
# Validations:
# - If dividend is None: ctx.error() + raise ValueError("Dividend is required")
# - If divisor is None: ctx.error() + raise ValueError("Divisor is required")
# - If divisor == 0: ctx.error() + raise ValueError("Division by zero impossible")
# Logging:
# - Start: ctx.info() "Calculating {dividend} / {divisor}"
# - Success: ctx.info() "Result: {result}"
# - If infinite result: ctx.warning() "Infinite result detected"
# Return the division result

# TODO: Create an async function called 'validate_and_process'
# Parameters: data (dict), required_fields (list), ctx (MockContext)
# Steps:
# 1. Check each required field exists in data
# 2. For missing fields: ctx.error() + raise ValueError("Missing required field: {field}")
# 3. ctx.info() "All required fields present"
# 4. Return the validated data dict

# TODO: Create an async function called 'process_numbers'
# Parameters: numbers (list of float), operation (str), ctx (MockContext)
# Supported operations: "sum", "average", "max", "min"
# Validations:
# - If numbers is empty: ctx.error() + raise ValueError("Numbers list cannot be empty")
# - If invalid operation: ctx.error() + raise ValueError("Unsupported operation")
# Return the result of the operation

def main():
    # Test your functions here
    pass

if __name__ == "__main__":
    main()
