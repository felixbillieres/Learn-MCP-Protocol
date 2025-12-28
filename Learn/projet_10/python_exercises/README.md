# Python Exercises for MCP Project 10

Before implementing MCP resource subscriptions, let's practice event-driven programming and callback management.

## Exercise 10: Resource Subscriptions & Notifications

This exercise covers:
- Subscription management and lifecycle
- Event notification systems
- Callback registration and handling
- Resource change broadcasting

### Instructions

1. Open `exercise_10.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_10.py`

### What you'll practice

- **SubscriptionManager class**: Managing subscriptions
- **Callback handling**: Registering and calling subscribers
- **Event broadcasting**: Notifying all subscribers of changes
- **Subscription lifecycle**: Subscribe/unsubscribe operations

### Key Concepts

- **Subscriptions**: Clients registering interest in resources
- **Callbacks**: Functions called when resources change
- **Event-driven**: Reactive programming patterns
- **Notification systems**: Broadcasting changes to subscribers

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 10!
```

### Tips

- Use sets to store multiple callbacks per resource
- Handle subscription cleanup properly
- Test callback execution and error handling
- Consider thread safety for concurrent subscriptions

Once you've completed this exercise, you'll know how to implement MCP resource subscription systems!
