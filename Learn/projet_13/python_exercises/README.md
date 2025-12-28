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
