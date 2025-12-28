# Exercise 02: Async Functions and Decorators
# Before creating MCP tools, let's practice async functions and decorators

import asyncio
import time

# TODO: Create a simple decorator called 'timer'
# This decorator should measure how long a function takes to execute
# It should print: "Function {function_name} took {time:.2f} seconds"
# Use time.time() to measure execution time

# TODO: Create a simple decorator called 'logger'
# This decorator should print: "Calling function: {function_name}"
# before executing the function, and "Finished function: {function_name}" after

# TODO: Create an async function called 'say_hello_async'
# This function should take a 'name' parameter (string)
# It should simulate some work with await asyncio.sleep(0.1)
# It should return a greeting message: f"Hello, {name}! How are you?"
# Add a docstring explaining what the function does

# TODO: Create an async function called 'calculate_sum_async'
# This function should take two parameters 'a' and 'b' (integers)
# It should simulate some work with await asyncio.sleep(0.05)
# It should return the sum of a and b
# Add a docstring explaining what the function does

# TODO: Create a synchronous function called 'run_calculations'
# This function should:
# - Use asyncio.run() to run async functions
# - Call say_hello_async("Alice") and store the result
# - Call calculate_sum_async(5, 3) and store the result
# - Print both results
# - Return a tuple with both results

# TODO: Create an async function called 'process_multiple_items'
# This function should take a list of items (list of strings)
# For each item, it should call say_hello_async(item) concurrently
# Use asyncio.gather() to run all calls at the same time
# Return a list of all the greeting messages

def main():
    # Test your functions here
    pass

if __name__ == "__main__":
    main()
