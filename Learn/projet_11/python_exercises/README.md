# Python Exercise 11: MCP Prompts & Message Management

## Overview

This exercise builds the Python foundation needed for MCP Project 11 (prompts). You'll learn to work with message structures, prompt metadata, and data organization patterns.

## What You'll Learn

### Python Skills
- Dictionary operations for data storage and retrieval
- List manipulation for managing sequences
- Class design for structured code organization
- Data validation and error handling

### MCP Preparation
- Message format structures (user/assistant roles)
- Prompt metadata management (name, title, description)
- Prompt lifecycle operations (create, store, retrieve)
- Multi-prompt system architecture

## Implementation Tasks

### 1. PromptManager Class
Create a class to manage prompt storage and retrieval:

```python
class PromptManager:
    def __init__(self):
        # Initialize storage for prompts
        pass

    def add_prompt(self, name, title, description, messages):
        # Store a prompt with metadata
        pass

    def list_prompts(self):
        # Return list of prompt metadata
        pass

    def get_prompt(self, name):
        # Retrieve specific prompt by name
        pass
```

### 2. Prompt Creation Functions
Implement functions to create specific prompts:

```python
def create_greeting_prompt():
    # Return greeting prompt structure
