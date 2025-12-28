# Python Exercises for MCP Projects

This directory contains Python exercises designed to help you practice the specific programming concepts needed for each MCP project before you start implementing the actual MCP tools.

## How It Works

Each MCP project (01-10) has a `python_exercises/` folder containing:

- `exercise_XX.py`: The exercise file with TODO comments
- `test_exercise_XX.py`: Test script to verify your implementation
- `README.md`: Instructions specific to that exercise

## Learning Path

The exercises follow the same progression as the MCP projects:

1. **Project 01**: Basic Python (imports, variables, functions)
2. **Project 02**: Async functions and decorators
3. **Project 03**: Pydantic models
4. **Project 04**: Context and logging
5. **Project 05**: Error handling and validation
6. **Project 06**: Complex types (List, Dict, Optional)
7. **Project 07**: Combining all concepts (final project prep)
8. **Project 08**: MCP resources
9. **Project 09**: Resource templates and URI parsing
10. **Project 10**: Subscriptions and notifications

## How to Use

1. **Before starting an MCP project**, do the corresponding Python exercise
2. Open `exercise_XX.py` and complete all TODO comments
3. Run `python3 test_exercise_XX.py` to verify your solution
4. If tests pass, you're ready for the MCP project!

## Tips for Success

- **Read the TODO comments carefully** - they guide you step by step
- **Test frequently** - run the test script often to catch issues early
- **Understand the concepts** - don't just copy code, learn why it works
- **Practice makes perfect** - these exercises build your Python skills progressively

## Dependencies

Some exercises require:
- `pip install pydantic` (for Project 03, 06, 07)

## Example Workflow

```bash
# For MCP Project 01:
cd Learn/projet_01/python_exercises
# Edit exercise_01.py to complete TODOs
python3 test_exercise_01.py
# If tests pass: 🎉 Ready for MCP Project 01!
```

Each exercise is designed to take 15-30 minutes and gives you hands-on practice with the exact Python concepts you'll need for the corresponding MCP project.
