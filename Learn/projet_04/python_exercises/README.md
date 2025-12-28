# Python Exercises for MCP Project 04

Before using Context for logging in MCP tools, let's practice error handling and logging patterns.

## Exercise 04: Context and Logging

This exercise covers:
- Using Context for logging (info, warning, error)
- Error handling with proper logging
- Async operations with logging
- Validation and error raising

### Instructions

1. Open `exercise_04.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_04.py`

### What you'll practice

- **Context logging**: `ctx.info()`, `ctx.warning()`, `ctx.error()`
- **Error handling**: Raising exceptions after logging
- **Validation**: Checking inputs and providing feedback
- **Async patterns**: Combining async operations with logging

### Key Concepts

- **Always log before raising**: Use `ctx.error()` then `raise`
- **Different log levels**: Info for normal operations, warning for issues, error for failures
- **Context is async**: Always use `await ctx.method()`

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 04!
```

### Tips

- Log at the start of operations with `ctx.info()`
- Use `ctx.warning()` for non-critical issues
- Use `ctx.error()` right before raising exceptions
- Context methods are async and must be awaited
