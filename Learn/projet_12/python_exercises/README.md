# Python Exercise 12: Dynamic Prompt Arguments & Template Processing

## Overview

This exercise teaches string templating and dynamic content generation for MCP Project 12. You'll learn to create prompts that accept parameters and generate personalized content.

## Learning Objectives

### Python Skills
- String formatting with templates and placeholders
- Parameter validation and error handling
- Dynamic content generation
- Safe template substitution

### MCP Preparation
- Dynamic prompt creation with arguments
- Parameter validation for prompt safety
- Template-based message generation
- MCP message formatting with variables

## Key Concepts

### Template Substitution
```python
# Basic string formatting
template = "Hello, {name}! Welcome to {topic}."
result = template.format(name="Alice", topic="Python")

# DynamicPrompt class for structured templates
class DynamicPrompt:
    def __init__(self, template, arguments):
        self.template = template
        self.arguments = arguments

    def format_message(self, params):
        return self.template.format(**params)
```

### Parameter Validation
```python
def validate_arguments(self, provided_args):
    for arg_name, arg_def in self.arguments.items():
        if arg_def.get("required", False) and arg_name not in provided_args:
            raise ValueError(f"Missing required argument: {arg_name}")
```

## Implementation Tasks

### 1. DynamicPrompt Class
```python
class DynamicPrompt:
    def __init__(self, template, arguments):
        # Store template and argument definitions
        pass

    def validate_arguments(self, provided_args):
        # Check required arguments are present
        pass

    def format_message(self, provided_args):
        # Replace placeholders with argument values
        pass
```

### 2. Prompt Creation Functions
```python
def create_code_review_prompt():
    # Create prompt for code review with language and code params
    pass

def create_summary_prompt():
    # Create prompt for summarization with topic and length params
    pass
```

### 3. Execution System
```python
def execute_prompt(prompt, arguments):
    # Validate and format prompt into MCP message structure
    pass
```

## Usage Examples

```python
# Create a code review prompt
code_prompt = create_code_review_prompt()
message = execute_prompt(code_prompt, {
    "language": "Python",
    "code": "def hello(): print('world')"
})
# Returns MCP-formatted message with substituted content

# Create a summary prompt with default values
summary_prompt = create_summary_prompt()
message = execute_prompt(summary_prompt, {"topic": "AI"})
# Uses default "concise" for length parameter
```

## Testing

Run tests to validate your implementation:
```bash
python3 test_exercise_12.py
```

Tests cover:
- Template substitution accuracy
- Parameter validation
- Error handling for missing arguments
- MCP message format compliance

## Success Criteria

- [ ] DynamicPrompt handles template substitution correctly
- [ ] Parameter validation catches missing required arguments
- [ ] Default values work for optional parameters
- [ ] MCP message format is correct

## Next Steps

These templating skills will be essential when implementing dynamic prompts with FastMCP decorators in Project 12.

---

## 🎯 **Learning Objectives**

By completing this exercise, you'll master:

### ✅ **Core Python Skills**
- **String templating**: f-strings, .format(), template substitution
- **Dictionary parameter handling**: Managing dynamic inputs
- **Validation patterns**: Ensuring template safety
- **Dynamic content generation**: Creating adaptive responses

### ✅ **MCP Dynamic Prompt Concepts**
- **Parameter injection**: Inserting variables into prompt templates
- **Template safety**: Preventing injection attacks
- **Dynamic message generation**: Creating context-aware conversations
- **Argument validation**: Ensuring required parameters are provided

---

## 📚 **Theoretical Background**

### 🔄 **Static vs Dynamic Prompts**

**Static Prompt (Project 11):**
```python
messages = [
    {"role": "user", "content": {"type": "text", "text": "Hello! How can I help you today?"}}
]
# Always the same message
```

**Dynamic Prompt (Project 12):**
```python
def create_greeting(name, time_of_day):
    messages = [
        {"role": "user", "content": {"type": "text", "text": f"Good {time_of_day}, {name}! How can I help you today?"}}
    ]
    return messages
# Personalized greeting based on parameters
```

### 🏗️ **Python Skills You'll Need**

#### 1. **String Formatting Techniques**
```python
# f-strings (modern, recommended)
name = "Alice"
message = f"Hello, {name}! Welcome!"

# .format() method
message = "Hello, {}! Welcome!".format(name)

# Template substitution
from string import Template
template = Template("Hello, $name! Welcome!")
message = template.substitute(name="Alice")
```

#### 2. **Dictionary-Based Parameter Handling**
```python
def format_message(template, params):
    """Safe parameter substitution"""
    try:
        return template.format(**params)
    except KeyError as e:
        raise ValueError(f"Missing required parameter: {e}")
```

#### 3. **Validation Patterns**
```python
def validate_parameters(required_params, provided_params):
    """Ensure all required parameters are present"""
    missing = set(required_params) - set(provided_params.keys())
    if missing:
        raise ValueError(f"Missing parameters: {list(missing)}")
    return True
```

---

## 🛠️ **Exercise Structure**

### 📁 **Files Overview**
- **`exercise_12.py`**: Your implementation with TODOs
- **`test_exercise_12.py`**: Validation tests
- **`README.md`**: This detailed guide

### 🎯 **Implementation Tasks**

#### 1. **DynamicPrompt Class** (Template Engine)
```python
class DynamicPrompt:
    def __init__(self, template, arguments):
        # TODO: Store template string and argument definitions
        pass

    def validate_arguments(self, provided_args):
        # TODO: Check required arguments are present
        pass

    def format_message(self, provided_args):
        # TODO: Replace placeholders with argument values
        pass
```

#### 2. **Prompt Creation Functions**
```python
def create_code_review_prompt():
    # TODO: Create prompt with language and code parameters
    pass

def create_summary_prompt():
    # TODO: Create prompt with topic and optional length
    pass
```

#### 3. **Execution System**
```python
def execute_prompt(prompt, arguments):
    # TODO: Validate and format prompt into MCP message
    pass
```

---

## 🚀 **Step-by-Step Implementation Guide**

### Step 1: Understanding Template Systems

**Template with Placeholders:**
```python
template = "Please review this {language} code: {code}"
arguments = {"language": "Python", "code": "print('hello')"}
result = template.format(**arguments)
# Result: "Please review this Python code: print('hello')"
```

**Argument Definition Structure:**
```python
arguments = {
    "language": {"required": True},           # Must be provided
    "code": {"required": True},              # Must be provided
    "style": {"required": False, "default": "concise"}  # Optional with default
}
```

### Step 2: Building DynamicPrompt Class

**Core Functionality:**
```python
class DynamicPrompt:
    def __init__(self, template, arguments):
        self.template = template
        self.arguments = arguments

    def validate_arguments(self, provided_args):
        """Ensure all required arguments are present"""
        for arg_name, arg_def in self.arguments.items():
            if arg_def.get("required", False) and arg_name not in provided_args:
                raise ValueError(f"Missing required argument: {arg_name}")
        return True

    def format_message(self, provided_args):
        """Substitute arguments into template"""
        # Merge provided args with defaults
        args_with_defaults = provided_args.copy()

        for arg_name, arg_def in self.arguments.items():
            if arg_name not in args_with_defaults and "default" in arg_def:
                args_with_defaults[arg_name] = arg_def["default"]

        # Safe substitution
        try:
            return self.template.format(**args_with_defaults)
        except KeyError as e:
            raise ValueError(f"Template error: missing argument {e}")
```

### Step 3: Creating Specific Prompts

**Code Review Prompt:**
```python
def create_code_review_prompt():
    template = "Please review this {language} code for bugs and improvements: {code}"
    arguments = {
        "language": {"required": True},
        "code": {"required": True}
    }
    return DynamicPrompt(template, arguments)
```

**Summary Prompt with Defaults:**
```python
def create_summary_prompt():
    template = "Please provide a {length} summary of: {topic}"
    arguments = {
        "topic": {"required": True},
        "length": {"required": False, "default": "concise"}
    }
    return DynamicPrompt(template, arguments)
```

### Step 4: Execution and MCP Integration

**MCP Message Format:**
```python
def execute_prompt(prompt, arguments):
    """Execute prompt and return MCP-formatted message"""
    # Validate arguments
    prompt.validate_arguments(arguments)

    # Format the message content
    message_text = prompt.format_message(arguments)

    # Return MCP message structure
    return {
        "role": "user",
        "content": {
            "type": "text",
            "text": message_text
        }
    }
```

---

## 🧪 **Testing & Examples**

### **Basic Usage Examples**
```python
# Create and use code review prompt
code_prompt = create_code_review_prompt()
message = execute_prompt(code_prompt, {
    "language": "Python",
    "code": "def hello(): print('world')"
})
print(message["content"]["text"])
# Output: "Please review this Python code for bugs and improvements: def hello(): print('world')"

# Use summary prompt with default
summary_prompt = create_summary_prompt()
message = execute_prompt(summary_prompt, {"topic": "Machine Learning"})
print(message["content"]["text"])
# Output: "Please provide a concise summary of: Machine Learning"
```

### **Error Handling Examples**
```python
# Missing required argument
try:
    execute_prompt(code_prompt, {"language": "Python"})  # Missing 'code'
except ValueError as e:
    print(f"Error: {e}")  # "Missing required argument: code"

# Invalid template substitution
bad_prompt = DynamicPrompt("Hello {name}, you are {age", {"name": {"required": True}})
try:
    bad_prompt.format_message({"name": "Alice"})
except ValueError as e:
    print(f"Template error: {e}")
```

---

## 🎯 **Success Criteria**

### ✅ **Functional Requirements**
- [ ] DynamicPrompt class handles template substitution correctly
- [ ] Argument validation catches missing required parameters
- [ ] Default values work for optional parameters
- [ ] MCP message format is correct for all outputs

### ✅ **Code Quality**
- [ ] Clean error messages for validation failures
- [ ] Safe template substitution (no injection vulnerabilities)
- [ ] Consistent parameter handling across all prompts
- [ ] Proper separation of template logic and execution logic

### ✅ **MCP Readiness**
- [ ] Understanding of parameterized prompt templates
- [ ] Knowledge of argument validation patterns
- [ ] Experience with dynamic content generation
- [ ] Familiarity with MCP message formatting

---

## 🚨 **Common Pitfalls & Solutions**

### ❌ **Template Injection Vulnerability**
```python
# DANGEROUS - Direct string formatting
template = f"Please analyze: {user_input}"  # User could inject code

# SAFE - Parameterized substitution
template = "Please analyze: {user_input}"
result = template.format(user_input=validated_input)
```

### ❌ **Missing Validation**
```python
# BAD - No validation
def format_message(template, params):
    return template.format(**params)  # Crashes if params missing

# GOOD - With validation
def format_message(template, params):
    # Validate required params first
    required = ["user_input"]  # Define what's needed
    for param in required:
        if param not in params:
            raise ValueError(f"Missing {param}")
    return template.format(**params)
```

### ❌ **Inconsistent Parameter Names**
```python
# BAD - Different parameter names
template = "Hello {name}!"
params = {"user_name": "Alice"}  # Won't match

# GOOD - Consistent naming
template = "Hello {name}!"
params = {"name": "Alice"}  # Matches perfectly
```

---

## 💡 **Pro Tips for Success**

### **1. Start with Simple Templates**
Begin with basic substitution before adding complex logic:
```python
# Simple first
template = "Hello {name}!"
args = {"name": "Alice"}

# Then add complexity
template = "Hello {name}, you are {age} years old!"
args = {"name": "Alice", "age": 30}
```

### **2. Test Edge Cases**
Always test with missing parameters, extra parameters, and invalid data:
```python
# Test missing required
try:
    prompt.format_message({})
except ValueError:
    print("Correctly caught missing parameter")

# Test extra parameters (should be ignored)
result = prompt.format_message({"name": "Alice", "extra": "ignored"})
assert "Alice" in result
```

### **3. Use Descriptive Parameter Names**
```python
# GOOD
arguments = {
    "user_name": {"required": True},      # Clear what it represents
    "message_length": {"required": False, "default": "short"}
}

# BAD
arguments = {
    "x": {"required": True},             # Unclear meaning
    "y": {"required": False, "default": "short"}
}
```

---

## 🎉 **Ready for MCP Project 12!**

Once all tests pass, you'll have mastered:

- ✅ **String templating** with safe parameter substitution
- ✅ **Argument validation** for template safety
- ✅ **Dynamic content generation** with defaults
- ✅ **MCP message formatting** for dynamic prompts

**You can now confidently implement dynamic prompts with arguments in Project 12!** 🚀

---

*Remember: MCP Project 12 builds on this foundation by adding FastMCP decorators and actual LLM integration, but all the Python templating logic you learned here will be essential.*
