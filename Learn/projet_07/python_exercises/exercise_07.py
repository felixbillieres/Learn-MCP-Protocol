# Exercise 07: Final Project Practice
# Practice combining all concepts: models, validation, async, context

from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import asyncio

class MockContext:
    async def info(self, msg: str): print(f"INFO: {msg}")
    async def warning(self, msg: str): print(f"WARNING: {msg}")
    async def error(self, msg: str): print(f"ERROR: {msg}")

class Task(BaseModel):
    id: int = Field(description="Task ID")
    title: str = Field(description="Task title")
    completed: bool = False

# TODO: Create an async function 'create_task'
# Parameters: title (str), ctx (MockContext)
# - Validate title is not empty
# - Generate ID (use a global counter)
# - Create and return Task instance
# - Log with ctx.info()

# TODO: Create an async function 'complete_task'
# Parameters: task_id (int), ctx (MockContext)
# - Find task by ID (from global tasks list)
# - Mark as completed
# - Return updated task
# - Log with ctx.info()

task_counter = 0
tasks = []

def main():
    # Test your functions here
    pass

if __name__ == "__main__":
    main()
