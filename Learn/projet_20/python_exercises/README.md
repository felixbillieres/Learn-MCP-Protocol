# Python Exercises for MCP Project 20

Before implementing OAuth token validation in MCP, let's practice token parsing and validation logic.

## Exercise 20: OAuth Token Validation

This exercise covers:
- JWT token structure and parsing
- Token signature verification
- Expiration and claims validation
- Secure token handling patterns

### Instructions

1. Open `exercise_20.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_20.py`

### What you'll practice

- **Token parsing**: Extracting claims from JWT tokens
- **Signature verification**: Ensuring token authenticity
- **Claims validation**: Checking token contents and validity
- **Error handling**: Managing invalid or expired tokens

### Key Concepts

- **JWT structure**: Header, payload, signature components
- **Token claims**: Standard fields (iss, sub, exp, iat)
- **Signature algorithms**: HS256, RS256 validation
- **Expiration handling**: Token lifetime management

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 20!
```

### Tips

- Always verify signatures before trusting claims
- Check expiration dates carefully
- Validate issuer and audience fields
- Handle malformed tokens gracefully

Once you've completed this exercise, you'll know how to implement secure OAuth token validation in MCP!
