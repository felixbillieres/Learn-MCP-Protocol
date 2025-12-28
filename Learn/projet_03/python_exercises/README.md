# Python Exercises for MCP Project 03

Before using Pydantic models in MCP tools, let's practice creating and validating data models.

## Exercise 03: Pydantic Models

This exercise covers:
- Creating Pydantic models with BaseModel
- Using Field for descriptions and constraints
- Optional vs required fields
- Default values
- Model validation

### Instructions

1. Open `exercise_03.py`
2. Complete all the TODO comments
3. Run the test: `python3 test_exercise_03.py`

### What you'll practice

- **BaseModel**: Inheriting from Pydantic's BaseModel
- **Field()**: Adding descriptions and constraints
- **Type hints**: Using `str | None` for optional fields
- **Validation**: Automatic validation of data
- **Model composition**: Using models inside other models

### Key Concepts

- **Required fields**: Must be provided when creating the model
- **Optional fields**: Can be None, use `field | None` syntax
- **Default values**: Automatically assigned if not provided
- **Field descriptions**: Help text for API documentation

### Expected Output

When all tests pass, you should see:
```
All tests passed! You're ready for MCP Project 03!
```

### Tips

- Use `Field(description="...")` for field descriptions
- Optional fields use `field: Type | None = None`
- Pydantic validates types automatically
- Models can contain other models as fields

Once you've completed this exercise, you'll know how to create Pydantic models for MCP tools!
