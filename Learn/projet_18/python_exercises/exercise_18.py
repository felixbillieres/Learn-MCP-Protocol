# Exercise 18: Advanced Sampling Parameters
# Before using advanced sampling parameters, let's practice controlling LLM behavior

from typing import List, Dict, Any, Optional
import random
import time

# TODO: Create a class called 'SamplingConfig'
# - __init__: stores temperature, max_tokens, model_preferences
# - validate_config: ensures parameters are within valid ranges
# - get_config_dict: returns config as dict for API calls
# - suggest_config: suggests optimal config for different use cases

# TODO: Create a class called 'AdvancedLLMSimulator'
# - simulate_response: generates responses based on parameters
# - apply_temperature: modifies creativity based on temperature
# - enforce_token_limit: ensures response stays within token limits
# - apply_model_preferences: adjusts response based on preferences

# TODO: Create a function called 'creative_writing_config'
# Returns SamplingConfig optimized for creative writing
# High temperature, longer responses, creative preferences

# TODO: Create a function called 'code_generation_config'
# Returns SamplingConfig optimized for code generation
# Lower temperature, technical preferences, precise responses

# TODO: Create a function called 'conversation_config'
# Returns SamplingConfig optimized for natural conversation
# Balanced temperature, conversational preferences

# TODO: Create a function called 'analyze_sampling_effect'
# Parameters: base_text (str), configs (list of SamplingConfig)
# Tests how different configs affect the same input
# Returns comparison of responses

class SamplingConfig:
    """Configuration for LLM sampling parameters"""

    def __init__(self, temperature: float = 0.7, max_tokens: int = 100,
                 model_preferences: Optional[Dict[str, Any]] = None):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model_preferences = model_preferences or {}
        self.validate_config()

    def validate_config(self):
        """Validate that all parameters are within acceptable ranges"""
        if not 0 <= self.temperature <= 2:
            raise ValueError(f"Temperature must be between 0 and 2, got {self.temperature}")

        if not 1 <= self.max_tokens <= 4096:
            raise ValueError(f"Max tokens must be between 1 and 4096, got {self.max_tokens}")

        valid_preferences = ['intelligencePriority', 'speedPriority', 'costPriority']
        for pref in self.model_preferences:
            if pref not in valid_preferences:
                raise ValueError(f"Invalid preference: {pref}")

    def get_config_dict(self) -> Dict[str, Any]:
        """Return configuration as dictionary"""
        return {
            'temperature': self.temperature,
            'max_tokens': self.max_tokens,
            'model_preferences': self.model_preferences
        }

    def suggest_config(self, use_case: str) -> 'SamplingConfig':
        """Suggest optimal config for different use cases"""
        suggestions = {
            'creative': SamplingConfig(1.2, 300, {'intelligencePriority': 'high'}),
            'analytical': SamplingConfig(0.3, 500, {'intelligencePriority': 'high'}),
            'conversational': SamplingConfig(0.8, 150, {'speedPriority': 'medium'}),
            'coding': SamplingConfig(0.2, 1000, {'intelligencePriority': 'high'}),
            'summarization': SamplingConfig(0.5, 200, {'speedPriority': 'high'})
        }
        return suggestions.get(use_case, self)

class AdvancedLLMSimulator:
    """Advanced LLM simulator with parameter-aware responses"""

    def __init__(self):
        self.base_responses = {
            'creative': [
                "In a world where colors danced like fireflies in the twilight...",
                "The ancient clock tower whispered secrets to the wind...",
                "Stars rearranged themselves into constellations of forgotten dreams..."
            ],
            'analytical': [
                "Based on the data, the correlation coefficient is 0.87...",
                "The optimal solution requires balancing multiple constraints...",
                "Statistical analysis shows a 95% confidence interval..."
            ],
            'conversational': [
                "That's really interesting! I think what you're saying is...",
                "I completely understand where you're coming from...",
                "Let me share my thoughts on that topic..."
            ],
            'coding': [
                "Here's a clean, efficient solution using modern best practices...",
                "The algorithm has O(n log n) time complexity and uses...",
                "This implementation handles edge cases and includes proper error handling..."
            ]
        }

    def simulate_response(self, messages: List[Dict[str, Any]], config: SamplingConfig) -> Dict[str, Any]:
        """Generate response based on sampling configuration"""
        # Analyze input to determine response type
        input_text = self._extract_input_text(messages)
        response_type = self._classify_input(input_text)

        # Get base response
        base_response = self._get_base_response(response_type)

        # Apply temperature effects
        modified_response = self.apply_temperature(base_response, config.temperature)

        # Enforce token limits
        final_response = self.enforce_token_limit(modified_response, config.max_tokens)

        # Apply model preferences
        preference_adjusted = self.apply_model_preferences(final_response, config.model_preferences)

        return {
            "role": "assistant",
            "content": {
                "type": "text",
                "text": preference_adjusted
            },
            "model": "advanced-simulator",
            "stop_reason": "end_turn",
            "usage": {
                "temperature": config.temperature,
                "max_tokens": config.max_tokens,
                "actual_tokens": len(preference_adjusted.split())
            }
        }

    def _extract_input_text(self, messages: List[Dict[str, Any]]) -> str:
        """Extract text from the last user message"""
        for msg in reversed(messages):
            if msg.get("role") == "user":
                return msg.get("content", {}).get("text", "")
        return ""

    def _classify_input(self, text: str) -> str:
        """Classify input to determine response type"""
        text_lower = text.lower()

        if any(word in text_lower for word in ['write', 'story', 'poem', 'creative']):
            return 'creative'
        elif any(word in text_lower for word in ['analyze', 'calculate', 'data', 'statistics']):
            return 'analytical'
        elif any(word in text_lower for word in ['code', 'function', 'program', 'algorithm']):
            return 'coding'
        else:
            return 'conversational'

    def _get_base_response(self, response_type: str) -> str:
        """Get a base response for the given type"""
        responses = self.base_responses.get(response_type, self.base_responses['conversational'])
        return random.choice(responses)

    def apply_temperature(self, text: str, temperature: float) -> str:
        """Modify response based on temperature setting"""
        if temperature < 0.3:
            # Low temperature: more focused, shorter
            words = text.split()
            return " ".join(words[:len(words)//2]) + "."
        elif temperature > 1.0:
            # High temperature: more creative, elaborate
            embellishments = [
                " And let me tell you something fascinating...",
                " This reminds me of a time when...",
                " In the grand scheme of things...",
                " Interestingly enough..."
            ]
            return text + " " + random.choice(embellishments)
        else:
            # Medium temperature: balanced
            return text

    def enforce_token_limit(self, text: str, max_tokens: int) -> str:
        """Ensure response doesn't exceed token limit"""
        words = text.split()
        max_words = max_tokens // 4  # Rough token estimation

        if len(words) > max_words:
            truncated = " ".join(words[:max_words])
            return truncated + "..."

        return text

    def apply_model_preferences(self, text: str, preferences: Dict[str, Any]) -> str:
        """Adjust response based on model preferences"""
        modified_text = text

        if preferences.get('intelligencePriority') == 'high':
            modified_text = "Based on comprehensive analysis: " + modified_text

        if preferences.get('speedPriority') == 'high':
            # Remove embellishments for speed
            modified_text = modified_text.replace(" And let me tell you something fascinating...", "")
            modified_text = modified_text.replace(" This reminds me of a time when...", "")
            modified_text = modified_text.replace(" In the grand scheme of things...", "")
            modified_text = modified_text.replace(" Interestingly enough...", "")

        return modified_text.strip()

def creative_writing_config() -> SamplingConfig:
    """Configuration optimized for creative writing"""
    return SamplingConfig(
        temperature=1.2,
        max_tokens=300,
        model_preferences={
            'intelligencePriority': 'high',
            'speedPriority': 'low'
        }
    )

def code_generation_config() -> SamplingConfig:
    """Configuration optimized for code generation"""
    return SamplingConfig(
        temperature=0.2,
        max_tokens=1000,
        model_preferences={
            'intelligencePriority': 'high',
            'speedPriority': 'medium'
        }
    )

def conversation_config() -> SamplingConfig:
    """Configuration optimized for natural conversation"""
    return SamplingConfig(
        temperature=0.8,
        max_tokens=150,
        model_preferences={
            'speedPriority': 'medium',
            'intelligencePriority': 'medium'
        }
    )

def analyze_sampling_effect(base_text: str, configs: List[SamplingConfig]) -> Dict[str, Any]:
    """Analyze how different configs affect the same input"""
    simulator = AdvancedLLMSimulator()
    messages = [{"role": "user", "content": {"type": "text", "text": base_text}}]

    results = {}
    for i, config in enumerate(configs):
        response = simulator.simulate_response(messages, config)
        results[f'config_{i+1}'] = {
            'config': config.get_config_dict(),
            'response': response['content']['text'],
            'tokens_used': response['usage']['actual_tokens']
        }

    return results

def main():
    """Demonstrate advanced sampling parameters"""
    try:
        print("=== Advanced Sampling Parameters Exercise ===\n")

        simulator = AdvancedLLMSimulator()

        # Test different configurations
        test_message = [{"role": "user", "content": {"type": "text", "text": "Write a creative story"}}]

        print("1. Creative Writing Configuration:")
        creative_config = creative_writing_config()
        creative_response = simulator.simulate_response(test_message, creative_config)
        print(f"Config: temp={creative_config.temperature}, max_tokens={creative_config.max_tokens}")
        print(f"Response: {creative_response['content']['text'][:100]}...\n")

        print("2. Code Generation Configuration:")
        code_config = code_generation_config()
        code_message = [{"role": "user", "content": {"type": "text", "text": "Write a Python function"}}]
        code_response = simulator.simulate_response(code_message, code_config)
        print(f"Config: temp={code_config.temperature}, max_tokens={code_config.max_tokens}")
        print(f"Response: {code_response['content']['text'][:100]}...\n")

        print("3. Conversation Configuration:")
        conv_config = conversation_config()
        conv_message = [{"role": "user", "content": {"type": "text", "text": "What's your opinion on AI?"}}]
        conv_response = simulator.simulate_response(conv_message, conv_config)
        print(f"Config: temp={conv_config.temperature}, max_tokens={conv_config.max_tokens}")
        print(f"Response: {conv_response['content']['text'][:100]}...\n")

        print("4. Parameter Comparison:")
        configs = [creative_writing_config(), code_generation_config(), conversation_config()]
        analysis = analyze_sampling_effect("Explain machine learning", configs)

        for config_name, result in analysis.items():
            print(f"{config_name}: {len(result['response'])} chars, {result['tokens_used']} tokens")

        print("\n✅ Advanced sampling parameters exploration completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
