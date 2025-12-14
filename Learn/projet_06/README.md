# Project 06: Tools with complex parameters

## Objective

Create more advanced tools with complex parameters (lists, dictionaries, nested Pydantic models).

## Concepts to learn

### Complex types in MCP

MCP tools can accept:
- **Basic types**: `str`, `int`, `float`, `bool`
- **Lists**: `List[str]`, `List[int]`, etc.
- **Dictionaries**: `Dict[str, str]`, etc.
- **Pydantic models**: Your own classes
- **Optional types**: `str | None`, `Optional[str]`

### Example with list

```python
from typing import List

@mcp_server.tool()
async def process_list(items: List[str], ctx: Context) -> List[str]:
    """Processes a list of items"""
    return [item.upper() for item in items]
```

### Example with nested Pydantic model

```python
from pydantic import BaseModel, Field
from typing import List

class Address(BaseModel):
    street: str
    city: str

class Person(BaseModel):
    name: str
    age: int
    addresses: List[Address]  # List of models!
```

## What you will create

In this project, you will create:
1. A `User` model with lists and optional fields
2. A tool that manipulates lists of users
3. A tool that returns complex data

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
