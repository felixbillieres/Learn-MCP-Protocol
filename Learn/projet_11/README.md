# Project 11: Create your first prompt

## Objective

Learn to create prompts (message templates) with MCP. Prompts allow you to expose reusable templates that clients can use.

## Concepts to learn

### What is a prompt?

A **prompt** is a predefined message template that the MCP server exposes to clients. Prompts are designed to be **user-controlled** - they are exposed so the user can explicitly select them.

### Difference from tools

- **Tools**: Actions the AI can execute (model control)
- **Prompts**: Templates the user can choose to use (user control)
- **Resources**: Data the AI can read (application control)

### Prompt structure

A prompt has:
- `name`: Unique identifier
- `title`: Readable name (optional)
- `description`: Description (optional)
- `arguments`: Dynamic arguments (optional)

### Returned message

When a client requests a prompt, the server returns formatted messages (like messages for an LLM).

## MCP Documentation

Prompts are declared with the `prompts` capability:
```json
{
  "capabilities": {
    "prompts": {}
  }
}
```

## What you will create

In this project, you will create a server that exposes simple prompts for different tasks.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
