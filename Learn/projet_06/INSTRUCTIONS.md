# Instructions - Project 06

## Your mission

Create tools with complex parameters and returns (lists, nested models).

## Steps to follow

1. **Create a Pydantic `User` model**:
   - `id`: int (required)
   - `name`: str (required)
   - `email`: str | None (optional)
   - `tags`: List[str] (list of tags, can be empty)
   - `score`: float (required, default value 0.0)
   - Use `Field()` for descriptions

2. **Create a `UserStatistics` model**:
   - `total`: int (total number of users)
   - `by_tag`: Dict[str, int] (number of users per tag)
   - `average_score`: float (average score)

3. **Create the `add_user` tool**:
   - Takes a parameter `user` (type `User`) and `ctx: Context`
   - Simulates adding a user (stores in an in-memory list)
   - Returns the user with their assigned ID
   - Logs with `ctx.info()`

4. **Create the `list_users` tool**:
   - Takes `ctx: Context`
   - Takes an optional parameter `tag_filter`: str | None
   - If `tag_filter` is provided, returns only users having this tag
   - Otherwise, returns all users
   - Returns `List[User]`
   - Logs with `ctx.info()`

5. **Create the `get_statistics` tool**:
   - Takes `ctx: Context`
   - Returns `UserStatistics`
   - Calculates total, stats by tag, and average score
   - Logs with `ctx.info()`

## Hints

- Use `from typing import List, Dict, Optional`
- To store users, use a global list: `users = []`
- To count by tag, iterate over users and their tags
- To calculate the average: `sum(u.score for u in users) / len(users)` if the list is not empty

## Test

Use `python test.py` to verify that:
- Models work with lists
- Tools correctly manipulate complex data
- Filters work

## Expected result

- Add multiple users with different tags
- List all users
- Filter by tag
- Get statistics
