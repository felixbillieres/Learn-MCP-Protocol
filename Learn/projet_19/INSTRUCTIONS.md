# Instructions - Project 19

## Your mission

Create an agentic workflow with sampling and tools.

## Steps to follow

1. **Create a FastMCP server** with basic tools

2. **Create simple tools**:
   - `calculate`: Takes `expression` (str), evaluates and returns result
   - `search_info`: Takes `term` (str), returns info (simulated)
   - `convert_unit`: Takes `value`, `source_unit`, `target_unit`, converts

3. **Create an `agent_solver` tool**:
   - Takes `question` (str) and `ctx: Context`
   - Uses sampling with defined tools
   - Allows the LLM to use tools to solve the question
   - Returns the final response

4. **Define tools for the LLM**:
   - Create tool definitions in MCP format
   - Include them in the sampling request with `tools`

## Hints

- For sampling with tools, use `tools` in create_message
- Each tool has `name`, `description`, `inputSchema` (JSON Schema)
- The LLM will decide when to use which tools
- The client automatically handles tool execution

## Test

The test will verify that tools are properly defined.
