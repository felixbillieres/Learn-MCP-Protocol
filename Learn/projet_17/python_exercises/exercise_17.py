# Exercise 17: LLM Sampling and Message Management
# Before using sampling in MCP tools, let's practice LLM interactions and message formatting

from typing import List, Dict, Any, Optional
import json
import time

# TODO: Create a class called 'MessageBuilder'
# - build_user_message: creates user message with text content
# - build_system_message: creates system message with instructions
# - build_assistant_message: creates assistant message with response
# - format_messages: converts to MCP sampling format

# TODO: Create a class called 'LLMSimulator'
# - __init__: stores conversation history
# - simulate_completion: simulates LLM response based on input
# - add_to_history: adds messages to conversation history
# - get_conversation_context: returns formatted conversation

# TODO: Create a function called 'create_question_prompt'
# Parameters: question (str), context (str, optional)
# This function should:
# - Build appropriate system message
# - Build user message with question and context
# - Return messages list ready for sampling

# TODO: Create a function called 'create_summary_prompt'
# Parameters: text (str), style (str, default "concise")
# This function should:
# - Create system prompt for summarization
# - Include style instructions (concise, detailed, bullet points)
# - Build user message with text to summarize
# - Return formatted messages

# TODO: Create a function called 'simulate_sampling_call'
# Parameters: messages (list), temperature (float, default 0.7), max_tokens (int, default 100)
# This function should:
# - Simulate LLM API call with parameters
# - Generate appropriate response based on input
# - Return response in MCP sampling format

class MessageBuilder:
    """Builds properly formatted messages for LLM interactions"""

    @staticmethod
    def build_user_message(text: str) -> Dict[str, Any]:
        """Create a user message"""
        return {
            "role": "user",
            "content": {
                "type": "text",
                "text": text
            }
        }

    @staticmethod
    def build_system_message(text: str) -> Dict[str, Any]:
        """Create a system message"""
        return {
            "role": "system",
            "content": {
                "type": "text",
                "text": text
            }
        }

    @staticmethod
    def build_assistant_message(text: str, model: str = "gpt-4") -> Dict[str, Any]:
        """Create an assistant message"""
        return {
            "role": "assistant",
            "content": {
                "type": "text",
                "text": text
            },
            "model": model,
            "stop_reason": "end_turn"
        }

    @staticmethod
    def format_messages(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Format messages for MCP sampling"""
        return messages

class LLMSimulator:
    """Simulates LLM responses for testing"""

    def __init__(self):
        self.conversation_history = []
        self.response_templates = {
            "question": "Based on your question '{question}', here's my answer: This is a simulated response to demonstrate LLM interaction.",
            "summary": "Here's a {style} summary of the provided text: [Summary would go here]",
            "default": "I understand your request. This is a simulated LLM response."
        }

    def simulate_completion(self, messages: List[Dict[str, Any]], temperature: float = 0.7,
                          max_tokens: int = 100) -> Dict[str, Any]:
        """Simulate LLM completion"""
        # Analyze last user message to determine response type
        last_user_message = None
        system_message = None

        for msg in reversed(messages):
            if msg["role"] == "user" and not last_user_message:
                last_user_message = msg["content"]["text"]
            elif msg["role"] == "system":
                system_message = msg["content"]["text"]

        # Generate response based on content
        response_text = self._generate_response(last_user_message, system_message, temperature, max_tokens)

        return {
            "role": "assistant",
            "content": {
                "type": "text",
                "text": response_text
            },
            "model": "simulated-gpt-4",
            "stop_reason": "end_turn",
            "usage": {
                "input_tokens": len(str(messages)),
                "output_tokens": len(response_text.split()),
                "total_tokens": len(str(messages)) + len(response_text.split())
            }
        }

    def _generate_response(self, user_text: str, system_text: Optional[str],
                          temperature: float, max_tokens: int) -> str:
        """Generate appropriate response based on input"""
        user_lower = user_text.lower() if user_text else ""

        if "summarize" in user_lower or "summary" in user_lower:
            style = "concise"
            if "detailed" in user_lower:
                style = "detailed"
            elif "bullet" in user_lower:
                style = "bullet-point"
            return self.response_templates["summary"].format(style=style)
        elif "?" in user_text or any(word in user_lower for word in ["what", "how", "why", "when", "where", "who"]):
            return self.response_templates["question"].format(question=user_text[:50])
        else:
            return self.response_templates["default"]

    def add_to_history(self, message: Dict[str, Any]):
        """Add message to conversation history"""
        self.conversation_history.append(message)

    def get_conversation_context(self) -> List[Dict[str, Any]]:
        """Get current conversation context"""
        return self.conversation_history.copy()

def create_question_prompt(question: str, context: Optional[str] = None) -> List[Dict[str, Any]]:
    """Create a prompt for answering questions"""
    builder = MessageBuilder()
    messages = []

    # Add system message
    system_text = "You are a helpful assistant. Answer questions accurately and clearly."
    messages.append(builder.build_system_message(system_text))

    # Add context if provided
    if context:
        context_message = f"Context: {context}\n\nQuestion: {question}"
        messages.append(builder.build_user_message(context_message))
    else:
        messages.append(builder.build_user_message(question))

    return messages

def create_summary_prompt(text: str, style: str = "concise") -> List[Dict[str, Any]]:
    """Create a prompt for text summarization"""
    builder = MessageBuilder()
    messages = []

    # Create style-specific instructions
    style_instructions = {
        "concise": "Provide a brief, focused summary in 1-2 sentences.",
        "detailed": "Provide a comprehensive summary covering all key points.",
        "bullet": "Provide a summary in bullet point format highlighting key information."
    }

    system_text = f"""You are a summarization assistant.
{style_instructions.get(style, style_instructions['concise'])}
Focus on the most important information and maintain factual accuracy."""

    messages.append(builder.build_system_message(system_text))

    # Add the text to summarize
    user_text = f"Please summarize the following text in a {style} style:\n\n{text}"
    messages.append(builder.build_user_message(user_text))

    return messages

def simulate_sampling_call(messages: List[Dict[str, Any]], temperature: float = 0.7,
                          max_tokens: int = 100) -> Dict[str, Any]:
    """Simulate a complete sampling call"""
    simulator = LLMSimulator()

    # Simulate API delay
    time.sleep(0.1)

    # Get response
    response = simulator.simulate_completion(messages, temperature, max_tokens)

    # Limit tokens if necessary (simplified)
    response_text = response["content"]["text"]
    words = response_text.split()
    if len(words) > max_tokens // 5:  # Rough token estimation
        truncated = " ".join(words[:max_tokens // 5])
        response["content"]["text"] = truncated + "..."
        response["stop_reason"] = "max_tokens"

    return response

def main():
    """Demonstrate LLM sampling and message management"""
    try:
        print("=== LLM Sampling Exercise ===\n")

        # Test question answering
        print("1. Question Answering:")
        question_msgs = create_question_prompt("What is Python?", "Python is a programming language")
        print(f"Messages created: {len(question_msgs)}")

        response = simulate_sampling_call(question_msgs)
        print(f"Response: {response['content']['text'][:100]}...")
        print(f"Model: {response['model']}, Tokens used: {response['usage']['total_tokens']}\n")

        # Test summarization
        print("2. Text Summarization:")
        sample_text = """
        Python is a high-level programming language created by Guido van Rossum.
        It was first released in 1991 and has become one of the most popular programming languages.
        Python emphasizes code readability and simplicity, making it great for beginners and experts alike.
        It supports multiple programming paradigms including procedural, object-oriented, and functional programming.
        """

        summary_msgs = create_summary_prompt(sample_text, "concise")
        summary_response = simulate_sampling_call(summary_msgs, temperature=0.3)
        print(f"Summary: {summary_response['content']['text']}\n")

        # Test with different temperatures
        print("3. Temperature Effects:")
        creative_response = simulate_sampling_call(question_msgs, temperature=1.2)
        focused_response = simulate_sampling_call(question_msgs, temperature=0.1)
        print(f"Creative (temp=1.2): {creative_response['content']['text'][:80]}...")
        print(f"Focused (temp=0.1): {focused_response['content']['text'][:80]}...")

        print("\n✅ LLM sampling simulation completed successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
