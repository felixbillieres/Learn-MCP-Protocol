# Learn MCP Protocol in Python

A progressive learning guide for mastering the Model Context Protocol (MCP) in Python, based on real-world project structures.

## Overview

This repository contains **40 progressive mini-projects** designed to take you from beginner to advanced level in MCP development. Each project builds upon previous concepts, providing hands-on experience with all major MCP features.

The projects are organized into three categories:
- **Learn** (Projects 01-25): Core MCP concepts and fundamentals
- **Offensive** (Projects 26-32): Security offensive tools and techniques
- **Defensive** (Projects 33-40): Security defensive tools and incident response

## Learning Path

### Beginner Level (Projects 01-07)

1. **Project 01** - Create a basic MCP server with FastMCP
2. **Project 02** - Add your first simple tool
3. **Project 03** - Use Pydantic models to structure data
4. **Project 04** - Use Context for logging (info, error, warning)
5. **Project 05** - Error handling and validation
6. **Project 06** - Tools with complex parameters and advanced types
7. **Project 07** - Beginner final project: Complete mini server

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

### Offensive Security (Projects 26-32)

26. **Project 26** - Port Scanner MCP: Scan ports and analyze services
27. **Project 27** - Payload Manager: Manage exploits, shells, and shellcodes
28. **Project 28** - Vulnerability Analyzer: Analyze CVEs and generate advisories
29. **Project 29** - Pentest Session Manager: Manage exploitation sessions
30. **Project 30** - Exploitation Framework: Chain exploits with intelligent payloads
31. **Project 31** - C2 Manager: Command & Control server simulation
32. **Project 32** - Pentest Automation: Orchestrate complete pentest workflows

### Defensive Security (Projects 33-40)

33. **Project 33** - SIEM MCP: Security Information and Event Management
34. **Project 34** - Incident Manager: Manage security incidents with triage
35. **Project 35** - Malware Analyzer: Analyze suspicious files and generate YARA rules
36. **Project 36** - Patch Manager: Track and deploy security patches
37. **Project 37** - Firewall Rules Manager: Manage firewall rules with validation
38. **Project 38** - Anomaly Detector: Detect anomalies using baselines and ML
39. **Project 39** - Secrets Manager: Securely manage passwords, tokens, and keys
40. **Project 40** - ADVANCED FINAL PROJECT: Complete security platform (offensive + defensive)

## Repository Structure

The repository is organized into three main directories:

```
Learn/
├── projet_01/       # Core MCP learning projects (01-25)
├── projet_02/
└── ...

Offensive/
├── projet_26/       # Security offensive projects (26-32)
├── projet_27/
└── ...

Defensive/
├── projet_33/       # Security defensive projects (33-40)
├── projet_34/
└── ...
```

## Project Structure

Each project follows the same structure:

```
projet_XX/
├── README.md        # Theoretical concepts and explanations
├── INSTRUCTIONS.md  # Detailed step-by-step instructions
├── solution.py      # Code template with TODOs to complete
├── test.py          # Test scripts to validate your implementation
└── .gitignore       # Git ignore rules (optional)
```

**Note:** Learn projects (01-25) have documentation in French. Offensive and Defensive projects (26-40) have documentation in English.

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

**Note:** 
- **Learn projects (01-25)**: Documentation is in French (README.md and INSTRUCTIONS.md)
- **Offensive projects (26-32)**: Documentation is in English
- **Defensive projects (33-40)**: Documentation is in English

The code, test files, and variable names use English conventions across all projects.

The main README is available in both languages:
- `README.md` - English version (this file)
- `README_FR.md` - French version
- `README_EN.md` - English version (same as README.md)

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
- ✅ **Security offensive tools**: Port scanning, exploitation, C2 management
- ✅ **Security defensive tools**: SIEM, incident response, malware analysis
- ✅ **Complete security platforms**: Combining offensive and defensive capabilities

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

