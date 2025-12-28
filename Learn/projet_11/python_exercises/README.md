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
    pass

def create_help_prompt():
    # Return help prompt structure
    pass

def initialize_prompts():
    # Create manager and add both prompts
    pass
```

## Key Concepts

### Message Structure
MCP messages follow this format:
```python
{
    "role": "user",  # or "assistant" or "system"
    "content": {
        "type": "text",
        "text": "Message content here"
    }
}
```

### Prompt Organization
Prompts are stored as dictionaries:
```python
{
    "name": "greeting",
    "title": "Greeting Prompt",
    "description": "A friendly greeting",
    "messages": [...]  # List of message dictionaries
}
```

## Testing

Run the test suite to validate your implementation:
```bash
python3 test_exercise_11.py
```

The tests verify:
- PromptManager functionality
- Data structure correctness
- Error handling
- MCP message format compliance

## Success Criteria

- [ ] PromptManager stores and retrieves prompts correctly
- [ ] Message structures follow MCP format
- [ ] Error handling for invalid inputs
- [ ] Clean, readable code organization

## Next Steps

Once completed, you'll be ready to implement MCP prompts in Project 11 using FastMCP decorators and server integration.

---

## Learning Objectives

By completing this exercise, you'll master:

### Core Python Skills
- Dictionary operations: Create, read, update prompt metadata
- List manipulation: Handle sequences of messages
- Class design patterns: Build a prompt management system
- Data validation: Ensure prompt structure integrity

### MCP Prompt Concepts
- Message format: Understanding user/assistant message structure
- Prompt metadata: Name, title, description management
- Prompt lifecycle: Creation, storage, retrieval patterns
- Multi-prompt systems: Managing multiple prompts efficiently

---

## 📚 **Theoretical Background**

### 🤖 **What Are MCP Prompts?**

MCP prompts are **predefined conversation templates** that guide LLM behavior:

```python
# Example MCP prompt structure
{
    "name": "code_review",
    "title": "Code Review Assistant",
    "description": "Helps review code for bugs and improvements",
    "messages": [
        {
            "role": "system",
            "content": {
                "type": "text",
                "text": "You are an expert code reviewer..."
            }
        },
        {
            "role": "user",
            "content": {
                "type": "text",
                "text": "Please review this code: {code}"
            }
        }
    ]
}
```

### 🏗️ **Python Skills You'll Need**

#### 1. **Dictionary as Data Container**
```python
# Storing prompt metadata
prompt = {
    "name": "greeting",
    "title": "Greeting Prompt",
    "description": "A friendly greeting",
    "messages": [...]  # List of messages
}
```

#### 2. **List for Message Sequences**
```python
# Managing message order
messages = [
    {"role": "system", "content": {...}},
    {"role": "user", "content": {...}},
    {"role": "assistant", "content": {...}}
]
```

#### 3. **Class for Organization**
```python
class PromptManager:
    def __init__(self):
        self.prompts = {}  # Dictionary storage

    def add_prompt(self, name, prompt_data):
        self.prompts[name] = prompt_data

    def get_prompt(self, name):
        return self.prompts.get(name)
```

---

## 🛠️ **Exercise Structure**

### 📁 **Files Overview**
- **`exercise_11.py`**: Your implementation with TODOs
- **`test_exercise_11.py`**: Validation tests
- **`README.md`**: This detailed guide

### 🎯 **Implementation Tasks**

#### 1. **PromptManager Class** (Core System)
```python
class PromptManager:
    def __init__(self):
        # TODO: Initialize empty prompts storage
        pass

    def add_prompt(self, name, title, description, messages):
        # TODO: Store prompt with metadata
        pass

    def list_prompts(self):
        # TODO: Return prompt list with metadata
        pass

    def get_prompt(self, name):
        # TODO: Retrieve specific prompt
        pass
```

#### 2. **Prompt Creation Functions**
```python
def create_greeting_prompt():
    # TODO: Create greeting prompt with proper structure
    pass

def create_help_prompt():
    # TODO: Create help prompt with messages
    pass
```

#### 3. **System Integration**
```python
def initialize_prompts():
    # TODO: Create manager and populate with prompts
    pass
```

---

## 🚀 **Step-by-Step Implementation Guide**

### Step 1: Understanding Data Structures

**Dictionary for Prompt Storage:**
```python
# Each prompt is stored as a dictionary
prompt = {
    "name": "example",           # Unique identifier
    "title": "Example Prompt",   # Human-readable title
    "description": "What this prompt does",
    "messages": [                # List of conversation messages
        {
            "role": "user",      # "user", "assistant", or "system"
            "content": {
                "type": "text",  # Always "text" for now
                "text": "Message content here"
            }
        }
    ]
}
```

### Step 2: Building the PromptManager Class

**Key Operations:**
- **Storage**: Use a dictionary with prompt names as keys
- **Retrieval**: Get prompts by name, return None if not found
- **Listing**: Return metadata for all prompts (without full message content)

**Implementation Pattern:**
```python
class PromptManager:
    def __init__(self):
        self.prompts = {}  # name -> prompt_data mapping

    def add_prompt(self, name, title, description, messages):
        # Validate inputs
        if not name or not messages:
            raise ValueError("Name and messages required")

        # Store structured prompt data
        self.prompts[name] = {
            "name": name,
            "title": title,
            "description": description,
            "messages": messages
        }
```

### Step 3: Creating Specific Prompts

**Greeting Prompt Structure:**
```python
def create_greeting_prompt():
    return {
        "name": "greeting",
        "title": "Greeting Message",
        "description": "A friendly greeting",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "Hello! How can I help you today?"
                }
            }
        ]
    }
```

**Help Prompt Structure:**
```python
def create_help_prompt():
    return {
        "name": "help",
        "title": "Help Message",
        "description": "Provides assistance information",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "I need help with..."
                }
            }
        ]
    }
```

### Step 4: System Integration

**Complete System Setup:**
```python
def initialize_prompts():
    manager = PromptManager()

    # Add greeting prompt
    greeting = create_greeting_prompt()
    manager.add_prompt(
        greeting["name"],
        greeting["title"],
        greeting["description"],
        greeting["messages"]
    )

    # Add help prompt
    help_prompt = create_help_prompt()
    manager.add_prompt(
        help_prompt["name"],
        help_prompt["title"],
        help_prompt["description"],
        help_prompt["messages"]
    )

    return manager
```

---

## 🧪 **Testing & Validation**

### **Automated Tests**
Run the validation tests:
```bash
python3 test_exercise_11.py
```

### **Expected Test Coverage**
- ✅ **PromptManager functionality**: Add, list, retrieve prompts
- ✅ **Data structure validation**: Correct prompt formatting
- ✅ **Error handling**: Invalid inputs, missing data
- ✅ **Message structure**: Proper role/content format

### **Manual Verification**
Test your implementation interactively:
```python
from exercise_11 import initialize_prompts

# Create and test the system
manager = initialize_prompts()

# List available prompts
prompts = manager.list_prompts()
print(f"Available prompts: {len(prompts)}")

# Get specific prompt
greeting = manager.get_prompt("greeting")
print(f"Greeting prompt: {greeting['title']}")

# Test message structure
messages = greeting["messages"]
print(f"First message role: {messages[0]['role']}")
```

---

## 🎯 **Success Criteria**

### ✅ **Functional Requirements**
- [ ] PromptManager stores prompts correctly
- [ ] Prompts can be retrieved by name
- [ ] List operation returns metadata only
- [ ] Message structure follows MCP format
- [ ] Error handling for invalid inputs

### ✅ **Code Quality**
- [ ] Clean, readable class structure
- [ ] Proper docstrings and comments
- [ ] Consistent naming conventions
- [ ] No hardcoded values in core logic

### ✅ **MCP Readiness**
- [ ] Understanding of prompt data structures
- [ ] Familiarity with message formatting
- [ ] Knowledge of metadata management
- [ ] Experience with prompt lifecycle operations

---

## 🚨 **Common Pitfalls & Tips**

### ❌ **Don't Make These Mistakes:**
- **Wrong message format**: Remember `{"role": "user", "content": {"type": "text", "text": "..."}}`
- **Storing full messages in list**: List operation should return metadata only
- **No error handling**: Validate inputs before storing
- **Inconsistent naming**: Use the same keys throughout

### 💡 **Pro Tips:**
- **Start simple**: Implement basic storage first, then add features
- **Test incrementally**: Run tests after each major change
- **Use descriptive names**: `prompts` dict, `add_prompt()` method
- **Validate structure**: Check message format before storing

---

## 🎉 **Ready for MCP Project 11!**

Once all tests pass, you'll have mastered:

- ✅ **Dictionary manipulation** for complex data structures
- ✅ **List operations** for message sequence management
- ✅ **Class design** for organized systems
- ✅ **Data validation** for integrity checks

**You can now confidently implement MCP prompts in Project 11!** 🚀

---

*Remember: These Python exercises are your foundation. MCP Project 11 will build directly on these concepts with the actual FastMCP prompt decorators and server integration.*
