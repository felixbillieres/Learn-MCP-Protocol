# Learn MCP Protocol in Python

A progressive learning guide for mastering the Model Context Protocol (MCP) in Python, based on real-world project structures.

## Overview

This repository contains **25 progressive mini-projects** designed to take you from beginner to advanced level in MCP development. Each project builds upon previous concepts, providing hands-on experience with all major MCP features.

## Learning Path

### Beginner Level (Projects 01-07)

1. **Project 01** - Create a basic MCP server with FastMCP
2. **Project 02** - Add your first simple tool
3. **Project 03** - Use Pydantic models to structure data
4. **Project 04** - Use Context for logging (info, error, warning)
5. **Project 05** - Error handling and validation
6. **Project 06** - Tools with complex parameters and advanced types
7. **Project 07** - Beginner final project: Complete mini server (inspired by Exegol-MCP)

### Resources (Projects 08-10)

8. **Project 08** - Create your first resource (expose data)
9. **Project 09** - Resources with URI templates and dynamic URIs
10. **Project 10** - Advanced resources: subscriptions and notifications

### Prompts (Projects 11-13)

11. **Project 11** - Create your first prompt (message template)
12. **Project 12** - Prompts with dynamic arguments
13. **Project 13** - Advanced prompts: chaining and complex workflows

### Elicitation (Projects 14-16)

14. **Project 14** - Use elicitation to request information
15. **Project 15** - Elicitation with JSON schemas and validation
16. **Project 16** - Elicitation URL mode for sensitive interactions

### Sampling (Projects 17-19)

17. **Project 17** - Use sampling to request LLM completions
18. **Project 18** - Sampling with model preferences and parameters
19. **Project 19** - Advanced sampling: complex agentic workflows

### Authorization & Security (Projects 20-22)

20. **Project 20** - Introduction to OAuth 2.1 authorization
21. **Project 21** - Implement authentication with tokens
22. **Project 22** - Advanced security: audience and scope validation

### Advanced Concepts (Projects 23-25)

23. **Project 23** - Use Roots to define access boundaries
24. **Project 24** - Custom transports and optimizations
25. **Project 25** - ADVANCED FINAL PROJECT: Complete MCP server with all features

## Project Structure

Each project follows the same structure:

```
projet_XX/
├── README.md        # Theoretical concepts and explanations (currently in French)
├── INSTRUCTIONS.md  # Detailed step-by-step instructions (currently in French)
├── solution.py      # Code template with TODOs to complete
├── test.py          # Test scripts to validate your implementation
└── .gitignore       # Git ignore rules
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Basic Python knowledge (functions, classes, imports)
- No prior MCP knowledge required - you'll learn everything here!

### Installation

```bash
pip install mcp pydantic
```

Or using `uv`:

```bash
uv pip install mcp pydantic
```

### How to Use

1. Start with **Project 01** and work through them sequentially
2. Read `README.md` to understand the theoretical concepts
3. Follow `INSTRUCTIONS.md` for detailed steps
4. Complete the code in `solution.py`
5. Run `python test.py` to validate your implementation
6. Ask for help or code review if needed!

## Translation Status

**Note:** Currently, the project documentation (README.md and INSTRUCTIONS.md files within each project folder) is in French. English translations are planned and will be added soon. The code, test files, and variable names use English conventions and are already in English.

The main README is available in both languages:
- `README.md` - English version (this file)
- `README_FR.md` - French version (original)

## Learning Objectives

By completing these projects, you will master:

- ✅ Creating MCP servers with FastMCP
- ✅ Declaring and implementing tools
- ✅ Using Pydantic for data validation
- ✅ Managing logs and context
- ✅ Proper error handling
- ✅ Working with resources, prompts, and elicitation
- ✅ Implementing authorization and security
- ✅ Building production-ready MCP servers

## Resources

- [MCP Specification](https://modelcontextprotocol.io)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [Pydantic Documentation](https://docs.pydantic.dev)

## Contributing

This is a learning resource. Feel free to:
- Report issues or suggest improvements
- Submit pull requests for better examples
- Share your solutions and implementations

## License

See LICENSE file for details.

## Acknowledgments

This learning path is inspired by real-world MCP implementations and follows the official MCP specification patterns.

---

**Happy Learning!**

