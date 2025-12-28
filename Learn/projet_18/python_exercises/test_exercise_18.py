"""
Test script for Python Exercise 18
Tests advanced sampling parameters
"""

import sys
import importlib.util

def test_sampling_config():
    """Test SamplingConfig functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_18.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test valid config
    config = exercise.SamplingConfig(temperature=0.8, max_tokens=200)
    assert config.temperature == 0.8
    assert config.max_tokens == 200

    # Test config dict
    config_dict = config.get_config_dict()
    assert config_dict['temperature'] == 0.8
    assert config_dict['max_tokens'] == 200

    # Test invalid temperature
    try:
        exercise.SamplingConfig(temperature=3.0)
        assert False, "Should have raised ValueError for invalid temperature"
    except ValueError:
        pass

    # Test invalid max_tokens
    try:
        exercise.SamplingConfig(max_tokens=5000)
        assert False, "Should have raised ValueError for invalid max_tokens"
    except ValueError:
        pass

    # Test invalid preference
    try:
        exercise.SamplingConfig(model_preferences={'invalidPref': 'high'})
        assert False, "Should have raised ValueError for invalid preference"
    except ValueError:
        pass

    print("✓ SamplingConfig works correctly")
    return True

def test_config_suggestions():
    """Test configuration suggestions for different use cases"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_18.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    base_config = exercise.SamplingConfig()

    # Test creative suggestion
    creative = base_config.suggest_config('creative')
    assert creative.temperature > 1.0
    assert creative.max_tokens > 200

    # Test coding suggestion
    coding = base_config.suggest_config('coding')
    assert coding.temperature < 0.5
    assert coding.max_tokens > 500

    # Test unknown use case (should return self)
    unknown = base_config.suggest_config('unknown')
    assert unknown.temperature == base_config.temperature

    print("✓ Configuration suggestions work correctly")
    return True

def test_advanced_simulator():
    """Test AdvancedLLMSimulator functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_18.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    simulator = exercise.AdvancedLLMSimulator()

    # Test basic response generation
    messages = [{"role": "user", "content": {"type": "text", "text": "Write a story"}}]
    config = exercise.SamplingConfig(temperature=0.7, max_tokens=100)
    response = simulator.simulate_response(messages, config)

    assert response["role"] == "assistant"
    assert "content" in response
    assert "usage" in response
    assert response["model"] == "advanced-simulator"

    print("✓ AdvancedLLMSimulator works correctly")
    return True

def test_temperature_effects():
    """Test how temperature affects responses"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_18.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    simulator = exercise.AdvancedLLMSimulator()
    base_text = "Hello world"

    # Test low temperature (should be shorter/more focused)
    low_temp_config = exercise.SamplingConfig(temperature=0.1)
    low_temp_result = simulator.apply_temperature(base_text, 0.1)
    assert len(low_temp_result) < len(base_text) + 50

    # Test high temperature (should be more elaborate)
    high_temp_config = exercise.SamplingConfig(temperature=1.5)
    high_temp_result = simulator.apply_temperature(base_text, 1.5)
    assert len(high_temp_result) > len(base_text)

    print("✓ Temperature effects work correctly")
    return True

def test_token_limits():
    """Test token limit enforcement"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_18.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    simulator = exercise.AdvancedLLMSimulator()

    long_text = " ".join([f"word{i}" for i in range(100)])
    limited_text = simulator.enforce_token_limit(long_text, 50)

    # Should be truncated
    assert len(limited_text.split()) < len(long_text.split())
    assert limited_text.endswith("...")

    print("✓ Token limits work correctly")
    return True

def test_model_preferences():
    """Test model preference adjustments"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_18.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    simulator = exercise.AdvancedLLMSimulator()

    # Test intelligence priority
    text = "This is a response"
    intelligence_result = simulator.apply_model_preferences(text, {'intelligencePriority': 'high'})
    assert intelligence_result.startswith("Based on comprehensive analysis:")

    # Test speed priority (should remove embellishments)
    creative_text = "This is great! And let me tell you something fascinating..."
    speed_result = simulator.apply_model_preferences(creative_text, {'speedPriority': 'high'})
    assert "fascinating" not in speed_result

    print("✓ Model preferences work correctly")
    return True

def test_config_functions():
    """Test the predefined configuration functions"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_18.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test creative config
    creative = exercise.creative_writing_config()
    assert creative.temperature > 1.0
    assert creative.max_tokens >= 200

    # Test code config
    code = exercise.code_generation_config()
    assert code.temperature < 0.5
    assert code.max_tokens >= 500

    # Test conversation config
    conv = exercise.conversation_config()
    assert 0.5 <= conv.temperature <= 1.0
    assert conv.max_tokens <= 200

    print("✓ Configuration functions work correctly")
    return True

def test_analysis_function():
    """Test the sampling effect analysis"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_18.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    configs = [
        exercise.creative_writing_config(),
        exercise.code_generation_config(),
        exercise.conversation_config()
    ]

    analysis = exercise.analyze_sampling_effect("Test input", configs)

    assert len(analysis) == 3
    for config_name, result in analysis.items():
        assert 'config' in result
        assert 'response' in result
        assert 'tokens_used' in result

    print("✓ Analysis function works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 18 - Advanced Sampling Parameters\n")

    tests = [
        test_sampling_config,
        test_config_suggestions,
        test_advanced_simulator,
        test_temperature_effects,
        test_token_limits,
        test_model_preferences,
        test_config_functions,
        test_analysis_function
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
        print("🎉 All tests passed! You're ready for MCP Project 18!")
        print("You've mastered advanced sampling parameters: temperature, token limits, and model preferences!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
