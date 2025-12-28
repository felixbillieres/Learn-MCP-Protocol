# Python Exercises for MCP Project 16

Before implementing URL-based authentication in MCP, let's practice URL validation and OAuth flow handling.

## Exercise 16: URL Elicitation & Authentication

This exercise covers:
- URL validation and parsing
- OAuth redirect URI handling
- Authentication state management
- Secure token exchange patterns

### Instructions

1. Open `exercise_16.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_16.py`

### What you'll practice

- **URL validation**: Checking URL format and security
- **OAuth flows**: Authorization code and implicit flows
- **State management**: Preventing CSRF attacks
- **Token handling**: Secure storage and exchange

### Key Concepts

- **URL elicitation**: Collecting URLs from users safely
- **OAuth 2.0**: Industry-standard authentication protocol
- **Redirect URIs**: Secure callback URL validation
- **State parameters**: CSRF protection in OAuth flows

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 16!
```

### Tips

- Always validate URLs before using them
- Use HTTPS for all authentication URLs
- Implement proper state parameter validation
- Handle token expiration gracefully

Once you've completed this exercise, you'll know how to implement secure URL-based authentication in MCP!
