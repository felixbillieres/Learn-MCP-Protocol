# Instructions - Project 04

## Your mission

Create a tool that uses Context to log information during its execution.

## Steps to follow

1. **Create a `process_file` tool** that:
   - Takes a parameter `filename` (str) and `ctx: Context`
   - Simulates file processing with several steps
   - Uses Context to log each step

2. **Processing steps**:
   - **Step 1**: `ctx.info()`: "Starting to process file {filename}"
   - **Step 2**: Check if the file exists (simulate with `filename.endswith(".txt")`)
     - If yes: `ctx.info()`: "File found"
     - If no: `ctx.warning()`: "Warning: the file does not appear to be a .txt file"
   - **Step 3**: `ctx.info()`: "Reading content..."
   - **Step 4**: Simulate an error if `filename == "error.txt"`
     - If error: `ctx.error()`: "Error reading the file" then `raise ValueError(...)`
   - **Step 5**: `ctx.info()`: "Processing completed successfully"
   - **Returns**: a dict with `{"file": filename, "status": "processed", "lines": 42}`

3. **Important**:
   - Don't forget to import `Context` from `mcp.server.fastmcp`
   - Use `await` for all Context methods
   - The `ctx` parameter must be the last parameter of the function

## Hints

- Import `Context`: `from mcp.server.fastmcp import Context`
- Use `await ctx.info(...)`, `await ctx.warning(...)`, `await ctx.error(...)`
- The `ctx: Context` parameter is usually placed last
- You can use `time.sleep(0.1)` to simulate processing that takes time

## Test

Use `python test.py` to verify that:
- The tool logs information correctly
- Different log levels work

## Expected result

When you call the tool:
- You should see log messages at each step
- Messages should be adapted to the context (info, warning, error)
