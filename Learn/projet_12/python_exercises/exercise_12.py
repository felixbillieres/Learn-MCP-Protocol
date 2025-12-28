# Exercise 12: Dynamic Prompt Arguments
# Before creating prompts with arguments, let's practice argument handling

class DynamicPrompt:
    def __init__(self, template, arguments):
        self.template = template
        self.arguments = arguments

    def validate_arguments(self, provided_args):
        """Check that all required arguments are present"""
        for arg_name, arg_def in self.arguments.items():
            if arg_def.get("required", False) and arg_name not in provided_args:
                raise ValueError(f"Missing required argument: {arg_name}")
        return True

    def format_message(self, provided_args):
        """Replace placeholders in template with argument values"""
        # Set defaults for optional arguments
        args_with_defaults = provided_args.copy()
        for arg_name, arg_def in self.arguments.items():
            if arg_name not in args_with_defaults and "default" in arg_def:
                args_with_defaults[arg_name] = arg_def["default"]

        return self.template.format(**args_with_defaults)

def create_code_review_prompt():
    return DynamicPrompt(
        "Please review this {language} code: {code}",
        {
            "language": {"required": True},
            "code": {"required": True}
        }
    )

def create_summary_prompt():
    return DynamicPrompt(
        "Please provide a {length} summary of {topic}",
        {
            "topic": {"required": True},
            "length": {"required": False, "default": "short"}
        }
    )

def execute_prompt(prompt, arguments):
    prompt.validate_arguments(arguments)
    message = prompt.format_message(arguments)
    return {
        "role": "user",
        "content": {"type": "text", "text": message}
    }

def test_prompts():
    code_prompt = create_code_review_prompt()
    summary_prompt = create_summary_prompt()

    # Test code review
    code_result = execute_prompt(code_prompt, {
        "language": "Python",
        "code": "print('hello')"
    })

    # Test summary with default
    summary_result = execute_prompt(summary_prompt, {
        "topic": "AI"
    })

    return [code_result, summary_result]

def main():
    # Test your dynamic prompts
    pass

if __name__ == "__main__":
    main()
