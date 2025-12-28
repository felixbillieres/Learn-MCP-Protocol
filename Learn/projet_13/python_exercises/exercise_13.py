# Exercise 13: Advanced Prompts with Resources
# Before creating advanced prompts, let's practice resource integration

class ResourceReference:
    def __init__(self, uri, content):
        self.uri = uri
        self.content = content

    def get_content(self):
        return self.content

    def get_metadata(self):
        return {
            "uri": self.uri,
            "type": "resource",
            "mimeType": "text/plain"
        }

def create_tutorial_prompt(topic):
    """Create a tutorial prompt with multiple messages"""
    return {
        "name": "tutorial",
        "messages": [
            {"role": "system", "content": "You are a helpful tutor"},
            {"role": "user", "content": f"Teach me about {topic}"},
            {"role": "assistant", "content": f"Let me explain {topic} step by step"}
        ]
    }

def create_code_analysis_prompt(code):
    """Create a code analysis prompt with resource reference"""
    return {
        "name": "code_analysis",
        "messages": [
            {"role": "user", "content": f"Analyze this code following best practices: {code}"}
        ],
        "resources": [
            {"uri": "doc://guidelines/best_practices", "content": "Best practices guidelines"}
        ]
    }

def create_multi_step_prompt(steps):
    """Create a prompt with multiple user messages"""
    messages = []
    for i, step in enumerate(steps, 1):
        messages.append({"role": "user", "content": f"Step {i}: {step}"})

    return {
        "name": "multi_step",
        "messages": messages
    }

class ResourceReference:
    def __init__(self, uri, content):
        # TODO: Store uri and content
        pass

    def get_content(self):
        # TODO: Return content
        pass

    def get_metadata(self):
        # TODO: Return metadata dict
        pass

def create_tutorial_prompt(topic):
    # TODO: Create tutorial prompt with multiple messages
    pass

def create_code_analysis_prompt(code):
    # TODO: Create code analysis prompt with resource reference
    pass

def create_multi_step_prompt(steps):
    # TODO: Create prompt with multiple user messages
    pass

def main():
    # Test your advanced prompts
    pass

if __name__ == "__main__":
    main()
