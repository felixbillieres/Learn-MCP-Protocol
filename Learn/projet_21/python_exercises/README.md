# Python Exercises for MCP Project 21

Before implementing scope-based authorization in MCP, let's practice token scope validation and access control.

## Exercise 21: Token Scopes & Audience Validation

This exercise covers:
- Scope claim parsing and validation
- Audience verification for tokens
- Access control decision logic
- Multi-tenant authorization patterns

### Instructions

1. Open `exercise_21.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_21.py`

### What you'll practice

- **Scope validation**: Checking token permissions
- **Audience verification**: Ensuring token validity for resource
- **Access control**: Granting/denying based on scopes
- **Policy enforcement**: Applying authorization rules

### Key Concepts

- **Token scopes**: Permission levels in OAuth tokens
- **Audiences**: Intended recipients of tokens
- **Authorization**: Access control based on credentials
- **Policy-based access**: Rules-driven security decisions

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 21!
```

### Tips

- Validate scopes before granting access
- Check audience claims match your service
- Implement principle of least privilege
- Log authorization decisions for auditing

Once you've completed this exercise, you'll know how to implement secure scope-based authorization in MCP!
