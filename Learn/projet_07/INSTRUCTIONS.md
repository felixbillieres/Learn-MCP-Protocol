# Instructions - Project 07 (FINAL PROJECT)

## Your mission

Create a complete MCP server to manage a todo list, using ALL the concepts learned!

## Features to implement

### 1. Pydantic models

**Create `Task`**:
- `id`: int (required)
- `title`: str (required, min 1 character)
- `description`: str | None (optional)
- `completed`: bool (default False)
- `priority`: str (default "normal", possible values: "low", "normal", "high", "urgent")
- `tags`: List[str] (list of tags, can be empty)
- `creation_date`: str (date in format "YYYY-MM-DD HH:MM:SS")

**Create `TaskStatistics`**:
- `total`: int
- `completed`: int
- `in_progress`: int
- `by_priority`: Dict[str, int]
- `by_tag`: Dict[str, int]

### 2. Tools to create

#### `create_task`
- Parameters: `title` (str), `description` (str | None), `priority` (str, default "normal"), `tags` (List[str], default []), `ctx: Context`
- Validates that the title is not empty
- Generates a unique ID (counter or random)
- Creates the creation date
- Adds the task to the list
- Returns: `Task`
- Logs with `ctx.info()`

#### `list_tasks`
- Parameters: `completed` (bool | None, optional to filter), `priority` (str | None, optional), `tag` (str | None, optional), `ctx: Context`
- Returns: `List[Task]`
- Filters according to provided parameters
- Logs with `ctx.info()`

#### `get_task`
- Parameters: `task_id` (int), `ctx: Context`
- Returns: `Task`
- Validates that the task exists
- If not found: `ctx.error()` + `raise ValueError`
- Logs with `ctx.info()`

#### `update_task`
- Parameters: `task_id` (int), `title` (str | None), `description` (str | None), `priority` (str | None), `tags` (List[str] | None), `ctx: Context`
- Returns: `Task` (updated)
- Validates that the task exists
- Updates only the provided fields (not None)
- Validates priority if provided
- Logs with `ctx.info()`

#### `mark_completed`
- Parameters: `task_id` (int), `completed` (bool, default True), `ctx: Context`
- Returns: `Task`
- Validates that the task exists
- Changes the `completed` status
- Logs with `ctx.info()`

#### `delete_task`
- Parameters: `task_id` (int), `ctx: Context`
- Returns: `bool` (True if deleted)
- Validates that the task exists
- Deletes the task from the list
- Logs with `ctx.warning()` (because it's a destructive action)
- If not found: `ctx.error()` + `raise ValueError`

#### `get_statistics`
- Parameters: `ctx: Context`
- Returns: `TaskStatistics`
- Calculates all statistics
- Logs with `ctx.info()`

### 3. Code structure

```python
# Imports
from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

# MCP Server
mcp_server = FastMCP(...)

# Global list to store tasks
tasks = []

# Pydantic models
class Task(BaseModel):
    ...

class TaskStatistics(BaseModel):
    ...

# Tools
@mcp_server.tool()
async def create_task(...):
    ...

# etc.

def main():
    ...

if __name__ == "__main__":
    main()
```

## Tips

1. **Organize your code**: models first, then tools
2. **Validate early**: check parameters at the start of each function
3. **Always log**: use `ctx.info()`, `ctx.warning()`, `ctx.error()`
4. **Clear messages**: errors must be understandable
5. **Reuse logic**: maybe create a `find_task(id)` function to avoid duplication

## Test

Use `python test.py` to test all features.

## Expected result

A functional MCP server that allows you to:
- Create tasks
- List and filter tasks
- Update and delete tasks
- Get statistics

This is your final project! Show me what you've created!
