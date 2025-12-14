# Project 09: Resources with URI templates

## Objective

Learn to create resources with URI templates that allow dynamically parameterized resources.

## Concepts to learn

### What is a URI template?

A **URI template** is an URI model that accepts parameters. This allows you to create dynamic resources without having to declare them all individually.

**Example**:
- Template: `file:///{path}`
- Resolved URI: `file:///home/user/document.txt` (with `path=/home/user/document.txt`)

### Templates vs Static Resources

- **Static resources**: Fixed URIs, known in advance (project 08)
- **Resources with templates**: Dynamic URIs, generated from parameters

### Advantages of templates

- Less repetitive code
- Support many resources without declaring them all
- Increased flexibility

## MCP Documentation

Templates use the [RFC 6570 URI Templates](https://datatracker.ietf.org/doc/html/rfc6570) format.

Example template:
```
file:///{path}
config://{section}/{key}
```

## What you will create

In this project, you will create a server that exposes resource templates to access dynamic configuration files.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
