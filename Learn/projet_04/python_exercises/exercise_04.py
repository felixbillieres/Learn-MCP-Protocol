# Exercise 04: Context and Logging
# Before using Context in MCP tools, let's practice logging and error handling

import asyncio
import time
from typing import Any

# Mock Context class for exercise (similar to MCP Context)
class MockContext:
    def __init__(self):
        self.logs = []

    async def info(self, message: str):
        """Log an info message"""
        self.logs.append(f"INFO: {message}")
        print(f"📝 {message}")

    async def warning(self, message: str):
        """Log a warning message"""
        self.logs.append(f"WARNING: {message}")
        print(f"⚠️  {message}")

    async def error(self, message: str):
        """Log an error message"""
        self.logs.append(f"ERROR: {message}")
        print(f"❌ {message}")

# TODO: Create an async function called 'process_file'
# Parameters: filename (str), ctx (MockContext)
# Simulate file processing with these steps:
# 1. ctx.info() "Starting to process file {filename}"
# 2. Check if filename.endswith(".txt"), if not: ctx.warning() "Warning: file may not be text"
# 3. ctx.info() "Reading content..."
# 4. Simulate processing time: await asyncio.sleep(0.1)
# 5. If filename == "error.txt": ctx.error() + raise ValueError("Corrupted file")
# 6. ctx.info() "Processing completed successfully"
# 7. Return {"file": filename, "status": "processed", "size": 1024}

# TODO: Create an async function called 'calculate_with_logging'
# Parameters: a (float), b (float), operation (str), ctx (MockContext)
# Supported operations: "add", "subtract", "multiply", "divide"
# Steps:
# 1. ctx.info() "Calculating {a} {operation} {b}"
# 2. Validate operation, if invalid: ctx.error() + raise ValueError("Invalid operation")
# 3. Perform calculation
# 4. If result > 1000: ctx.warning() "Large result detected"
# 5. ctx.info() "Result: {result}"
# 6. Return the result

# TODO: Create an async function called 'batch_process'
# Parameters: items (list of dicts), ctx (MockContext)
# Each item dict has: {"filename": str, "operation": str, "a": float, "b": float}
# For each item:
# - Process the file (call process_file)
# - Calculate with the operation (call calculate_with_logging)
# - Handle errors gracefully (log but continue)
# Return list of successful results

def main():
    # Test your functions here
    pass

if __name__ == "__main__":
    main()
