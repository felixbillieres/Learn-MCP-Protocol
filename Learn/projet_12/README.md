# Project 12: Prompts with dynamic arguments

## Objective

Learn to create prompts that accept dynamic arguments to personalize content.

## Concepts to learn

### Arguments in prompts

Prompts can accept **arguments** that allow you to personalize the returned message. For example, a code review prompt can accept a `language` argument to adapt the message.

### Argument structure

Each argument has:
- `name`: Argument name
- `description`: Description (optional)
- `required`: If the argument is required (optional, default false)

### Usage

When a client requests a prompt with `prompts/get`, it can pass an `arguments` dict with argument values.

## What you will create

In this project, you will create prompts that use arguments to personalize content.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
