# Project 03: Use Pydantic models

## Objective

Learn to use Pydantic to structure and validate data in your MCP tools.

## Concepts to learn

### What is Pydantic?

Pydantic is a Python library that allows you to:
- **Define data models** with automatic validation
- **Validate types** automatically
- **Document data** with descriptions
- **Convert** between Python and JSON easily

### Why use Pydantic in MCP?

In MCP, data often passes through JSON. Pydantic allows you to:
- Ensure data is correct before using it
- Have clear documentation of what your tool expects/returns
- Have better code structure

### Create a Pydantic model

```python
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age", ge=0, le=120)
    email: str | None = Field(None, description="Optional email")
```

### Use a model in a tool

```python
@mcp_server.tool()
async def create_person(person: Person) -> Person:
    """Creates a person"""
    return person  # Pydantic validates automatically!
```

## What you will create

In this project, you will:
1. Create a Pydantic `Message` model to represent a message
2. Create a tool that uses this model
3. See how Pydantic automatically validates data

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
