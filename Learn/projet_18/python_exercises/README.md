# Python Exercises for MCP Project 18

Before implementing advanced MCP sampling features, let's practice LLM parameter handling and response processing.

## Exercise 18: Advanced Sampling Parameters

This exercise covers:
- Temperature and top_p parameter management
- Max tokens and token counting
- Response format handling
- Sampling strategy implementation

### Instructions

1. Open `exercise_18.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_18.py`

### What you'll practice

- **Parameter classes**: Managing sampling parameters
- **Token counting**: Estimating response lengths
- **Format validation**: Ensuring proper parameter ranges
- **Sampling strategies**: Different generation approaches

### Key Concepts

- **Temperature**: Controls randomness (0.0-2.0)
- **Top_p**: Nucleus sampling probability (0.0-1.0)
- **Max tokens**: Response length limits
- **Response format**: Structured output requirements

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 18!
```

### Tips

- Temperature 0.0 = deterministic, higher = more creative
- Top_p 1.0 = all tokens, lower = more focused
- Validate parameter ranges before using
- Consider token limits for API costs

Once you've completed this exercise, you'll know how to handle advanced LLM sampling parameters in MCP!
