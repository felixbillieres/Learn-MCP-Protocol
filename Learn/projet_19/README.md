# Project 19: Sampling with tools and agentic workflows

## Objective

Learn to use sampling with tools to create agentic workflows where the LLM can call functions.

## Concepts to learn

### Sampling with tools

Sampling can include tools that the LLM can use during generation. This allows creating agents that can:
- Call functions
- Receive results
- Continue reasoning
- Iterate until the task is solved

### Agentic flow

1. Server sends a request with available tools
2. LLM decides to call a tool
3. Client executes the tool
4. Client returns the result to the LLM
5. LLM continues with the result
6. Repeats until LLM finishes

### Tool declaration

Tools are declared in the sampling request with:
- `name`: Tool name
- `description`: Description
- `inputSchema`: JSON schema of parameters

## What you will create

In this project, you will create an agentic workflow where the LLM can use tools to solve complex tasks.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
