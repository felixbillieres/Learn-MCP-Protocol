# Python Exercises for MCP Project 05

Before implementing validation in MCP tools, let's practice error handling and data validation.

## Exercise 05: Error Handling and Validation

This exercise covers:
- Input validation with clear error messages
- Proper error logging before raising exceptions
- Handling edge cases (None, empty lists, invalid operations)
- Combining validation with logging

### Instructions

1. Open `exercise_05.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_05.py`

### What you'll practice

- **Validation**: Checking inputs before processing
- **Error logging**: Using `ctx.error()` before raising exceptions
- **Clear messages**: Descriptive error messages
- **Edge cases**: Handling None, empty lists, invalid operations

### Key Concepts

- **Validate early**: Check inputs at function start
- **Log then raise**: Always `ctx.error()` before `raise ValueError()`
- **Clear messages**: Users should understand what went wrong
- **Fail fast**: Don't continue processing invalid data

### Expected Output

When all tests pass, you should see:
```
🎉 All tests passed! You're ready for MCP Project 05!
```
