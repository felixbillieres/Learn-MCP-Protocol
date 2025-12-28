# Learn MCP Protocol in Python - Complete Learning Platform

A comprehensive, progressive learning guide for mastering the Model Context Protocol (MCP) in Python, with 40+ pedagogical exercises to build your skills step-by-step.

## What's New: Python Exercises System

This repository now includes comprehensive Python exercises for each MCP project! Before diving into MCP implementation, master the Python concepts you'll need.

### Python Exercises Structure

Each project now has a `python_exercises/` folder with:
- `exercise_XX.py` - Complete Python code with TODOs (not just tests!)
- `test_exercise_XX.py` - Automated validation tests
- `README.md` - Detailed learning instructions

### Learning Flow

```
1. Study Python Exercise -> Master concepts
2. Implement MCP Project -> Apply knowledge
3. Validate with Tests -> Confirm understanding
4. Next Project -> Progressive learning
```

---

## Repository Overview

### 40 Progressive MCP Projects

| Section | Projects | Focus | Difficulty |
|---------|----------|-------|------------|
| **Learn** | 01-25 | Core MCP + Advanced Features | Beginner → Expert |
| **Offensive** | 26-32 | Security Offensive Tools | Advanced |
| **Defensive** | 33-40 | Security Defensive Tools | Advanced |

### Complete Learning Path

#### Core MCP Fundamentals (Projects 01-07)
1. **Project 01** - Basic MCP server with FastMCP
2. **Project 02** - First tools (async functions, decorators)
3. **Project 03** - Pydantic models & validation
4. **Project 04** - Context logging (info/warning/error)
5. **Project 05** - Error handling & validation
6. **Project 06** - Complex types (List, Dict, Optional)
7. **Project 07** - Complete mini-server (all concepts combined)

#### MCP Core Features (Projects 08-19)
8. **Resources** - Expose data via MCP
9. **URI Templates** - Dynamic resource access
10. **Subscriptions** - Real-time notifications
11. **Prompts** - Message templates for LLMs
12. **Dynamic Prompts** - Arguments & personalization
13. **Advanced Prompts** - Multi-message workflows
14. **Elicitation** - Request user information
15. **Schema Validation** - JSON Schema elicitation
16. **URL Elicitation** - OAuth & secure interactions
17. **LLM Sampling** - Request completions
18. **Advanced Sampling** - Temperature, tokens, preferences
19. **Agentic Workflows** - Tools + LLM orchestration

#### Security & Authorization (Projects 20-22)
20. **OAuth Basics** - Token validation
21. **Scopes & Audiences** - Granular permissions
22. **Advanced Security** - Rate limiting, monitoring

#### ⚡ **Advanced Concepts (Projects 23-25)**
23. **Roots** - Path-based access control
24. **Transports** - Multi-transport configuration
25. **FINAL PROJECT** - Complete MCP server (all features)

#### Offensive Security (Projects 26-32)
26. **Port Scanner** - Network scanning & service analysis
27. **Payload Manager** - Exploit/shellcode management
28. **Vulnerability Analyzer** - CVE analysis & advisories
29. **Pentest Sessions** - Exploitation session management
30. **Exploit Framework** - Chained exploit execution
31. **C2 Manager** - Command & control simulation
32. **Pentest Automation** - Complete workflow orchestration

#### Defensive Security (Projects 33-40)
33. **SIEM** - Security event processing & alerting
34. **Incident Manager** - Security incident triage
35. **Malware Analyzer** - File analysis & YARA rules
36. **Patch Manager** - Security patch tracking
37. **Firewall Manager** - Rule validation & management
38. **Anomaly Detector** - ML-based anomaly detection
39. **Secrets Manager** - Secure credential management
40. **FINAL PROJECT** - Complete security platform

---

## Repository Structure

```
Learn-MCP-Protocol/
├── Learn/                    # Core MCP learning (01-25)
│   ├── projet_01/
│   │   ├── python_exercises/    # 🆕 Python prep exercises!
│   │   │   ├── exercise_01.py
│   │   │   ├── test_exercise_01.py
│   │   │   └── README.md
│   │   ├── README.md
│   │   ├── INSTRUCTIONS.md
│   │   ├── solution.py
│   │   └── test.py
│   └── ...
│
├── Offensive/               # Security offensive tools (26-32)
│   ├── projet_26/
│   │   ├── python_exercises/    # 🆕 Python prep exercises!
│   │   └── ...
│   └── ...
│
├── Defensive/              # Security defensive tools (33-40)
│   ├── projet_33/
│   │   ├── python_exercises/    # 🆕 Python prep exercises!
│   │   └── ...
│   └── ...
│
├── README.md               # This file
├── README_FR.md           # French version
└── README_EN.md           # English version
```

---

## How to Use the Python Exercises

### Before Each MCP Project

1. **Check if Python exercises exist** for your project:
   ```bash
   ls Learn/projet_XX/python_exercises/
   ```

2. **Study the Python concepts** needed:
   ```bash
   cat Learn/projet_XX/python_exercises/README.md
   ```

3. **Complete the exercise**:
   ```bash
   # Edit the exercise
   nano Learn/projet_XX/python_exercises/exercise_XX.py

   # Run tests to validate
   python3 Learn/projet_XX/python_exercises/test_exercise_XX.py
   ```

4. **When tests pass** - You're ready for the MCP project!

### Progressive Difficulty

| Project Range | Python Concepts | MCP Focus |
|---------------|----------------|-----------|
| 01-07 | Basic Python | MCP Fundamentals |
| 08-13 | Data structures | Resources & Prompts |
| 14-19 | Async, validation | Elicitation & Sampling |
| 20-25 | Security, auth | Advanced MCP |
| 26-32 | Network, security | Offensive Tools |
| 33-40 | Monitoring, analysis | Defensive Tools |

---

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Basic Python knowledge (recommended but not required)
- No prior MCP knowledge needed!

### Installation
```bash
# Install MCP and dependencies
pip install mcp pydantic

# For some exercises (optional)
pip install requests aiohttp
```

### Learning Workflow

1. **Start with Project 01** - Complete the Python exercise first
2. **Read the theory** - `README.md` explains MCP concepts
3. **Follow instructions** - `INSTRUCTIONS.md` guides implementation
4. **Code & test** - Complete `solution.py`, validate with `test.py`
5. **Repeat** - Each project builds on previous knowledge

### Testing Your Progress

```bash
# Test Python exercise (prep)
python3 Learn/projet_XX/python_exercises/test_exercise_XX.py

# Test MCP implementation
python3 Learn/projet_XX/test.py
```

---

## Language Support

- **Learn Projects (01-25)**: Documentation in **French** 🇫🇷
- **Offensive/Defensive (26-40)**: Documentation in **English** 🇺🇸
- **Code & Tests**: Always in **English** (consistent naming)

---

## What You'll Master

### ✅ **Python Skills**
- Async/await programming
- Pydantic data validation
- Error handling & logging
- Network programming
- Security concepts
- Data structures & algorithms

### ✅ **MCP Expertise**
- Server creation with FastMCP
- Tools, resources, prompts
- Elicitation & sampling
- Authentication & authorization
- Production-ready implementations

### ✅ **Security Proficiency**
- Offensive security tools
- Defensive security systems
- Incident response
- Security automation

---

## Resources & Documentation

- **[MCP Specification](https://modelcontextprotocol.io)** - Official protocol docs
- **[FastMCP](https://github.com/jlowin/fastmcp)** - Python MCP implementation
- **[Pydantic](https://docs.pydantic.dev)** - Data validation library

### 🆘 **Getting Help**

- Check the `README.md` and `INSTRUCTIONS.md` in each project
- Review the Python exercises for concept clarification
- Run tests to identify specific issues
- Join MCP community discussions

---

## Contributing

This is a learning platform - contributions welcome!

- Report Issues: Found a bug or unclear instruction?
- Suggest Improvements: Better examples or explanations?
- Code Contributions: Enhanced exercises or tools?
- Documentation: Improve clarity or add examples?

**See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.**

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **MCP Community** - For the excellent protocol specification
- **FastMCP Authors** - For the Python implementation
- **Security Researchers** - For offensive/defensive techniques
- **Open Source Community** - For the tools and libraries

---

## Ready to Start?

```bash
# Clone the repository
git clone https://github.com/el/learn-mcp-protocol.git
cd learn-mcp-protocol

# Start with the first Python exercise
cd Learn/projet_01/python_exercises
python3 test_exercise_01.py  # Should show what to implement

# Then move to MCP implementation
cd ..
python3 test.py  # MCP project tests
```

**Happy Learning! Master MCP step by step, from Python basics to advanced security platforms.**

---

**Built with love by Félix Billières**

