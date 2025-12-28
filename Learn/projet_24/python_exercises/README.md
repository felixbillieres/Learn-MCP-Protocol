# Python Exercises for MCP Project 24

Before implementing configurable transports in MCP, let's practice transport detection and optimization logic.

## Exercise 24: Configurable Transports & Optimization

This exercise covers:
- Transport protocol detection and selection
- Connection optimization strategies
- Protocol negotiation and fallback
- Performance monitoring and adaptation

### Instructions

1. Open `exercise_24.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_24.py`

### What you'll practice

- **Transport detection**: Identifying available protocols
- **Connection optimization**: Choosing best transport for scenario
- **Protocol negotiation**: Handling capability exchange
- **Performance monitoring**: Tracking and adapting to conditions

### Key Concepts

- **Transport protocols**: HTTP, WebSocket, SSE options
- **Connection optimization**: Latency, bandwidth, reliability trade-offs
- **Protocol negotiation**: Feature detection and compatibility
- **Adaptive behavior**: Switching transports based on conditions

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 24!
```

### Tips

- Detect transport capabilities at connection time
- Choose appropriate protocol for use case
- Monitor performance and adapt as needed
- Provide graceful fallback for unsupported features

Once you've completed this exercise, you'll know how to implement configurable and optimized transports in MCP!
