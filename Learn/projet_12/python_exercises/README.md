# Python Exercises for MCP Project 12

Before implementing dynamic prompts in MCP, let's practice string templating and parameter handling.

## Exercise 12: Dynamic Prompt Arguments

This exercise covers:
- String formatting with templates and placeholders
- Parameter validation and error handling
- Dynamic content generation
- Safe template substitution

### Instructions

1. Open `exercise_12.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_12.py`

### What you'll practice

- **DynamicPrompt class**: Structured template management
- **Parameter validation**: Checking required arguments
- **Template substitution**: Safe placeholder replacement
- **MCP message formatting**: Converting to proper message structure

### Key Concepts

- **Template strings**: Using `{variable}` placeholders
- **Parameter validation**: Ensuring required fields are provided
- **Default values**: Automatic fallback for optional parameters
- **Safe substitution**: Preventing template injection

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 12!
```

### Tips

- Use `template.format(**params)` for safe substitution
- Always validate required parameters before formatting
- Test with missing arguments to ensure proper error handling
- MCP messages need specific structure: `{"role": "user", "content": {"type": "text", "text": "..."}}`

Once you've completed this exercise, you'll know how to handle dynamic prompt arguments in MCP!
