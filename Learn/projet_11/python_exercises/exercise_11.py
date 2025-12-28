# Exercise 11: MCP Prompts
# Before creating MCP servers with prompts, let's practice prompt management

# TODO: Create a class called 'PromptManager'
# - __init__: create empty prompts dict
# - add_prompt: add a prompt with name, title, description, and template
# - list_prompts: return list of prompt metadata
# - get_prompt: return prompt content by name

# TODO: Create a function called 'create_greeting_prompt'
# This function should return a prompt dict with:
# - name: "greeting"
# - title: "Greeting Message"
# - description: "A friendly greeting"
# - messages: list with one user message "Hello! How can I help you today?"

# TODO: Create a function called 'create_help_prompt'
# This function should return a prompt dict with:
# - name: "help"
# - title: "Help Message"
# - description: "Provides assistance information"
# - messages: list with one user message "I need help with..."

# TODO: Create a function called 'initialize_prompts'
# This function should:
# - Create a PromptManager instance
# - Add the greeting prompt
# - Add the help prompt
# - Return the manager

class PromptManager:
    def __init__(self):
        self.prompts = {}

    def add_prompt(self, name, title, description, messages):
        self.prompts[name] = {
            "name": name,
            "title": title,
            "description": description,
            "messages": messages
        }

    def list_prompts(self):
        return [
            {
                "name": prompt["name"],
                "title": prompt["title"],
                "description": prompt["description"]
            }
            for prompt in self.prompts.values()
        ]

    def get_prompt(self, name):
        return self.prompts.get(name)

def create_greeting_prompt():
    return {
        "name": "greeting",
        "title": "Greeting Message",
        "description": "A friendly greeting",
        "messages": [
            {"role": "user", "content": {"type": "text", "text": "Hello! How can I help you today?"}}
        ]
    }

def create_help_prompt():
    return {
        "name": "help",
        "title": "Help Message",
        "description": "Provides assistance information",
        "messages": [
            {"role": "user", "content": {"type": "text", "text": "I need help with..."}}
        ]
    }

def initialize_prompts():
    manager = PromptManager()
    greeting = create_greeting_prompt()
    help_prompt = create_help_prompt()

    manager.add_prompt(
        greeting["name"],
        greeting["title"],
        greeting["description"],
        greeting["messages"]
    )

    manager.add_prompt(
        help_prompt["name"],
        help_prompt["title"],
        help_prompt["description"],
        help_prompt["messages"]
    )

    return manager

def main():
    # Test your prompt system
    pass

if __name__ == "__main__":
    main()
