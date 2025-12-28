# Python Exercises for MCP Project 02

Before creating MCP tools with async functions and decorators, let's practice these essential Python concepts.

## Exercise 02: Async Functions and Decorators

This exercise covers:
- Creating and using decorators
- Understanding async/await syntax
- Working with asyncio for concurrent operations
- Combining sync and async code

### Instructions

1. Open `exercise_02.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_02.py`

### What you'll practice

- **Decorators**: Functions that modify other functions
- **Async functions**: Using `async def` and `await`
- **Asyncio**: Running async code with `asyncio.run()`
- **Concurrency**: Running multiple async operations simultaneously with `asyncio.gather()`
- **Docstrings**: Documenting your functions

### Key Concepts

- **async/await**: Allows non-blocking execution
- **Decorators**: Functions that wrap other functions (like `@timer`)
- **asyncio.gather()**: Run multiple async operations concurrently
- **asyncio.run()**: Entry point to run async code from sync context

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 02!
```

### Tips

- Decorators use `@decorator_name` syntax
- Async functions must use `await` for async operations
- Use `asyncio.run()` to call async functions from sync code
- `asyncio.gather()` returns results in the same order as input

Once you've completed this exercise, you'll understand how MCP tools work with async functions and decorators!
