"""
Test script for Python Exercise 17
Tests LLM sampling and message management
"""

import sys
import importlib.util

def test_message_builder():
    """Test message building functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_17.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    builder = exercise.MessageBuilder()

    # Test user message
    user_msg = builder.build_user_message("Hello!")
    assert user_msg["role"] == "user"
    assert user_msg["content"]["type"] == "text"
    assert user_msg["content"]["text"] == "Hello!"

    # Test system message
    system_msg = builder.build_system_message("You are helpful")
    assert system_msg["role"] == "system"
    assert "helpful" in system_msg["content"]["text"]

    # Test assistant message
    assistant_msg = builder.build_assistant_message("Hi there!", "gpt-4")
    assert assistant_msg["role"] == "assistant"
    assert assistant_msg["model"] == "gpt-4"
    assert assistant_msg["stop_reason"] == "end_turn"

    print("✓ MessageBuilder works correctly")
    return True

def test_llm_simulator():
    """Test LLM simulation functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_17.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    simulator = exercise.LLMSimulator()

    # Test basic completion
    messages = [{"role": "user", "content": {"type": "text", "text": "Hello"}}]
    response = simulator.simulate_completion(messages)

    assert response["role"] == "assistant"
    assert "content" in response
    assert "model" in response
    assert "usage" in response
    assert response["model"] == "simulated-gpt-4"

    # Test conversation history
    simulator.add_to_history(messages[0])
    simulator.add_to_history(response)
    history = simulator.get_conversation_context()
    assert len(history) == 2

    print("✓ LLMSimulator works correctly")
    return True

def test_question_prompt():
    """Test question prompt creation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_17.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test simple question
    messages = exercise.create_question_prompt("What is AI?")
    assert len(messages) == 2  # system + user
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert "What is AI?" in messages[1]["content"]["text"]

    # Test question with context
    messages_with_context = exercise.create_question_prompt("What is this?", "Context about Python")
    assert "Context about Python" in messages_with_context[1]["content"]["text"]
    assert "What is this?" in messages_with_context[1]["content"]["text"]

    print("✓ create_question_prompt works correctly")
    return True

def test_summary_prompt():
    """Test summary prompt creation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_17.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    sample_text = "This is a long text that needs summarization."

    # Test concise summary
    messages = exercise.create_summary_prompt(sample_text, "concise")
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert "concise" in messages[0]["content"]["text"].lower()
    assert sample_text in messages[1]["content"]["text"]

    # Test detailed summary
    detailed_messages = exercise.create_summary_prompt(sample_text, "detailed")
    assert "comprehensive" in detailed_messages[0]["content"]["text"].lower()

    # Test bullet point summary
    bullet_messages = exercise.create_summary_prompt(sample_text, "bullet")
    assert "bullet" in bullet_messages[0]["content"]["text"].lower()

    print("✓ create_summary_prompt works correctly")
    return True

def test_sampling_simulation():
    """Test the complete sampling simulation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_17.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test sampling call
    messages = exercise.create_question_prompt("What is machine learning?")
    response = exercise.simulate_sampling_call(messages)

    assert response["role"] == "assistant"
    assert "content" in response
    assert "usage" in response
    assert isinstance(response["usage"]["total_tokens"], int)

    # Test with different parameters
    response_temp = exercise.simulate_sampling_call(messages, temperature=0.1, max_tokens=50)
    assert response_temp["role"] == "assistant"

    # Test summarization sampling
    summary_messages = exercise.create_summary_prompt("Long text here", "concise")
    summary_response = exercise.simulate_sampling_call(summary_messages)
    assert "summary" in summary_response["content"]["text"].lower()

    print("✓ simulate_sampling_call works correctly")
    return True

def test_integration():
    """Test integration of all components"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_17.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Create a conversation flow
    simulator = exercise.LLMSimulator()

    # First message
    question_msgs = exercise.create_question_prompt("Explain recursion")
    response1 = simulator.simulate_completion(question_msgs)

    # Add to history
    simulator.add_to_history(question_msgs[1])  # user message
    simulator.add_to_history(response1)

    # Follow-up question
    followup_msgs = exercise.create_question_prompt("Give me a code example")
    # Add conversation context
    full_conversation = simulator.get_conversation_context() + followup_msgs[1:]

    response2 = simulator.simulate_completion(full_conversation)

    assert response1["role"] == "assistant"
    assert response2["role"] == "assistant"
    assert len(simulator.get_conversation_context()) == 2

    print("✓ Integration test works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 17 - LLM Sampling and Message Management\n")

    tests = [
        test_message_builder,
        test_llm_simulator,
        test_question_prompt,
        test_summary_prompt,
        test_sampling_simulation,
        test_integration
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            print()

    print(f"Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! You're ready for MCP Project 17!")
        print("You've mastered LLM message formatting, sampling parameters, and conversation management!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
