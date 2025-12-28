# Python Exercises for MCP Project 06

Before implementing complex tool parameters in MCP, let's practice working with lists, nested models, and advanced Pydantic features.

## Exercise 06: Complex Parameters & Nested Models

This exercise covers:
- List parameters and return types
- Nested Pydantic models
- Optional fields with defaults
- Complex data validation

### Instructions

1. Open `exercise_06.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_06.py`

### What you'll practice

- **User model**: Creating nested Pydantic models
- **List handling**: Working with List[str] and List[Model]
- **Optional fields**: Using `field | None` syntax
- **Default values**: Automatic field initialization

### Key Concepts

- **Nested models**: Models containing other models
- **List types**: `List[str]`, `List[User]`, etc.
- **Optional fields**: Fields that can be None
- **Field descriptions**: Adding metadata to model fields

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 06!
```

### Tips

- Use `List[Type]` for list fields
- Optional fields use `Type | None = None`
- Use `Field(description="...")` for field metadata
- Nested models inherit validation rules

Once you've completed this exercise, you'll know how to create complex MCP tools with nested parameters and return types!
