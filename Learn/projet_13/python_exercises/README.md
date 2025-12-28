# 🎯 Python Exercise 13: Advanced Prompts with Multi-Message Conversations

## 📋 **Before You Start: Why This Exercise Matters**

**MCP Project 13** introduces **advanced prompts** with multiple messages and resource references. Before implementing complex conversation flows, you need to master Python concepts for managing sequential message exchanges and integrating external references.

This exercise teaches you:
- **Multi-message conversation management** for complex interactions
- **Message sequencing** and conversation flow control
- **Resource reference handling** and integration
- **Advanced prompt composition** with multiple roles

---

## 🎯 **Learning Objectives**

By completing this exercise, you'll master:

### ✅ **Core Python Skills**
- **List manipulation** for message sequence management
- **Dictionary composition** for complex data structures
- **Function composition** for building modular prompts
- **Data integration** patterns for combining multiple sources

### ✅ **Advanced MCP Prompt Concepts**
- **Multi-turn conversations**: System → User → Assistant flows
- **Resource integration**: Referencing external data in prompts
- **Message role management**: System, user, assistant coordination
- **Prompt modularity**: Building reusable prompt components

---

## 📚 **Theoretical Background**

### 🗣️ **Single vs Multi-Message Prompts**

**Single Message (Project 11-12):**
```python
messages = [
    {"role": "user", "content": {"type": "text", "text": "Hello!"}}
]
```

**Multi-Message Conversation (Project 13):**
```python
messages = [
    {
        "role": "system",
        "content": {"type": "text", "text": "You are a helpful coding assistant."}
    },
    {
        "role": "user",
        "content": {"type": "text", "text": "Help me with this Python code."}
    },
    {
        "role": "assistant",
        "content": {"type": "text", "text": "I'd be happy to help! What specific issue are you facing?"}
    },
    {
        "role": "user",
        "content": {"type": "text", "text": "The function isn't working as expected."}
    }
]
```

### 🔗 **Resource Integration**

**Resource References in Messages:**
```python
# Reference to external data
message_with_resource = {
    "role": "user",
    "content": {
        "type": "text",
        "text": "Analyze this code following our guidelines."
    },
    "resources": [
        {
            "uri": "doc://guidelines/best_practices",
            "content": "Best coding practices document..."
        }
    ]
}
```

### 🏗️ **Python Skills You'll Need**

#### 1. **List Operations for Message Sequences**
```python
# Building conversation flows
messages = []

# Add system context
messages.append({
    "role": "system",
    "content": {"type": "text", "text": "You are a tutor."}
})

# Add user question
messages.append({
    "role": "user",
    "content": {"type": "text", "text": f"Explain {topic}"}
})

# Add assistant response (simulated)
messages.append({
    "role": "assistant",
    "content": {"type": "text", "text": f"Let me explain {topic}..."}
})
```

#### 2. **Dictionary Composition for Complex Structures**
```python
def create_tutorial_prompt(topic):
    return {
        "name": "tutorial",
        "messages": [
            {
                "role": "system",
                "content": {"type": "text", "text": "You are a helpful tutor."}
            },
            {
                "role": "user",
                "content": {"type": "text", "text": f"Teach me about {topic}."}
            },
            {
                "role": "assistant",
                "content": {"type": "text", "text": f"I'd be glad to teach you about {topic}. Let's start with the basics..."}
            }
        ]
    }
```

#### 3. **Resource Integration Patterns**
```python
def create_code_analysis_prompt(code):
    return {
        "name": "code_analysis",
        "messages": [
            {
                "role": "user",
                "content": {"type": "text", "text": f"Analyze this code: {code}"}
            }
        ],
        "resources": [
            {
                "uri": "doc://guidelines/best_practices",
                "content": "Code analysis guidelines and best practices..."
            }
        ]
    }
```

---

## 🛠️ **Exercise Structure**

### 📁 **Files Overview**
- **`exercise_13.py`**: Your implementation with TODOs
- **`test_exercise_13.py`**: Validation tests
- **`README.md`**: This detailed guide

### 🎯 **Implementation Tasks**

#### 1. **ResourceReference Class**
```python
class ResourceReference:
    def __init__(self, uri, content):
        # TODO: Store URI and content
        pass

    def get_content(self):
        # TODO: Return content
        pass

    def get_metadata(self):
        # TODO: Return URI and type info
        pass
```

#### 2. **Prompt Creation Functions**
```python
def create_tutorial_prompt(topic):
    # TODO: Create multi-message tutorial prompt
    pass

def create_code_analysis_prompt(code):
    # TODO: Create prompt with resource reference
    pass

def create_multi_step_prompt(steps):
    # TODO: Create prompt with multiple user messages
    pass
```

---

## 🚀 **Step-by-Step Implementation Guide**

### Step 1: Understanding Message Flows

**Tutorial Conversation Pattern:**
```python
def create_tutorial_prompt(topic):
    return {
        "name": "tutorial",
        "messages": [
            # System sets context
            {
                "role": "system",
                "content": {"type": "text", "text": "You are a helpful tutor."}
            },
            # User asks question
            {
                "role": "user",
                "content": {"type": "text", "text": f"Teach me about {topic}."}
            },
            # Assistant provides guidance
            {
                "role": "assistant",
                "content": {"type": "text", "text": f"Let me explain {topic} step by step..."}
            }
        ]
    }
```

**Resource-Enhanced Prompt:**
```python
def create_code_analysis_prompt(code):
    return {
        "name": "code_analysis",
        "messages": [
            {
                "role": "user",
                "content": {"type": "text", "text": f"Analyze this code: {code}"}
            }
        ],
        "resources": [
            {
                "uri": "doc://guidelines/best_practices",
                "content": "Follow these coding standards..."
            }
        ]
    }
```

### Step 2: Building ResourceReference Class

**Complete Implementation:**
```python
class ResourceReference:
    def __init__(self, uri, content):
        self.uri = uri
        self.content = content

    def get_content(self):
        """Return the resource content"""
        return self.content

    def get_metadata(self):
        """Return resource metadata"""
        return {
            "uri": self.uri,
            "type": "resource",
            "mimeType": "text/plain"
        }
```

### Step 3: Multi-Step Conversation Prompts

**Sequential User Messages:**
```python
def create_multi_step_prompt(steps):
    """Create a prompt with multiple user messages representing steps"""
    messages = []

    for i, step in enumerate(steps, 1):
        messages.append({
            "role": "user",
            "content": {
                "type": "text",
                "text": f"Step {i}: {step}"
            }
        })

    return {
        "name": "multi_step",
        "messages": messages
    }
```

---

## 🧪 **Testing & Examples**

### **Tutorial Prompt Example**
```python
# Create tutorial for a topic
tutorial = create_tutorial_prompt("recursion")
print(f"Prompt: {tutorial['name']}")
print(f"Messages: {len(tutorial['messages'])}")

# Check message roles
roles = [msg["role"] for msg in tutorial["messages"]]
print(f"Role sequence: {roles}")  # ['system', 'user', 'assistant']
```

### **Code Analysis with Resources**
```python
# Create analysis prompt
code = "def factorial(n): return n * factorial(n-1) if n > 0 else 1"
analysis_prompt = create_code_analysis_prompt(code)

print(f"Has resources: {'resources' in analysis_prompt}")
if 'resources' in analysis_prompt:
    print(f"Resource URI: {analysis_prompt['resources'][0]['uri']}")
```

### **Multi-Step Process**
```python
# Create step-by-step guide
steps = [
    "Install Python from python.org",
    "Set up a virtual environment",
    "Install required packages",
    "Write your first script"
]

multi_step = create_multi_step_prompt(steps)
print(f"Total steps: {len(multi_step['messages'])}")
print("First step:", multi_step['messages'][0]['content']['text'])
```

---

## 🎯 **Success Criteria**

### ✅ **Functional Requirements**
- [ ] ResourceReference class manages URI and content correctly
- [ ] Tutorial prompts contain proper system/user/assistant sequence
- [ ] Code analysis prompts include resource references
- [ ] Multi-step prompts create sequential user messages
- [ ] All message structures follow MCP format

### ✅ **Code Quality**
- [ ] Clean separation between different prompt types
- [ ] Consistent message formatting across all prompts
- [ ] Proper resource metadata structure
- [ ] Modular function design for reusability

### ✅ **MCP Readiness**
- [ ] Understanding of multi-turn conversation patterns
- [ ] Knowledge of resource integration in prompts
- [ ] Experience with complex message sequencing
- [ ] Familiarity with MCP resource reference format

---

## 🚨 **Common Pitfalls & Solutions**

### ❌ **Wrong Message Order**
```python
# BAD - Assistant before user
messages = [
    {"role": "assistant", "content": {...}},  # Wrong order
    {"role": "user", "content": {...}}
]

# GOOD - Proper conversation flow
messages = [
    {"role": "system", "content": {...}},    # Context first
    {"role": "user", "content": {...}},      # Question second
    {"role": "assistant", "content": {...}}  # Response last
]
```

### ❌ **Missing Resource Structure**
```python
# BAD - Incorrect resource format
"resources": [
    {"uri": "doc://test", "data": "content"}  # Wrong key
]

# GOOD - Proper MCP resource format
"resources": [
    {
        "uri": "doc://test",
        "content": "resource content here"
    }
]
```

### ❌ **Inconsistent Message Format**
```python
# BAD - Missing required fields
messages = [
    {"role": "user", "text": "Hello"}  # Missing content structure
]

# GOOD - Complete MCP message format
messages = [
    {
        "role": "user",
        "content": {
            "type": "text",
            "text": "Hello"
        }
    }
]
```

---

## 💡 **Pro Tips for Success**

### **1. Plan Message Flow First**
Before coding, sketch the conversation:
```
System: Set context for the AI
User: Ask the actual question
Assistant: Provide guidance or response
User: Follow up if needed
```

### **2. Test Message Sequences**
Verify the conversation makes sense:
```python
def validate_conversation_flow(messages):
    """Check if message sequence is logical"""
    roles = [msg["role"] for msg in messages]

    # System should come first (if present)
    if "system" in roles and roles[0] != "system":
        return False

    # Should alternate between user/assistant after system
    conversation_roles = roles[1:] if roles[0] == "system" else roles

    for i, role in enumerate(conversation_roles):
        expected = "user" if i % 2 == 0 else "assistant"
        if role != expected:
            return False

    return True
```

### **3. Use Meaningful Resource URIs**
```python
# GOOD - Descriptive URIs
"uri": "doc://guidelines/python_best_practices"
"uri": "doc://examples/factorial_function"

# BAD - Generic URIs
"uri": "doc://file1"
"uri": "doc://resource"
```

---

## 🎉 **Ready for MCP Project 13!**

Once all tests pass, you'll have mastered:

- ✅ **Multi-message conversation management** with proper sequencing
- ✅ **Resource integration patterns** in prompt structures
- ✅ **Complex prompt composition** with multiple roles
- ✅ **MCP message formatting** for advanced interactions

**You can now confidently implement advanced prompts with conversation flows and resource references in Project 13!** 🚀

---

*Remember: MCP Project 13 adds FastMCP decorators and actual resource server integration, but all the Python logic for managing complex conversations and resource references that you learned here will be the foundation.*
