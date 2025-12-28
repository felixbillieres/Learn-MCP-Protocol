"""
Test script for Python Exercise 16
Tests URL mode elicitation and authentication
"""

import sys
import importlib.util

def test_url_validator():
    """Test URL validation functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_16.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    validator = exercise.URLValidator()

    # Test valid URLs
    assert validator.validate_url("https://example.com") == True
    assert validator.validate_url("https://api.github.com/user") == True

    # Test invalid URLs
    assert validator.validate_url("http://example.com") == False  # Not HTTPS
    assert validator.validate_url("localhost:3000") == False  # Blocked domain
    assert validator.validate_url("not-a-url") == False  # Invalid format

    # Test normalization
    assert validator.normalize_url("example.com") == "https://example.com"
    assert validator.normalize_url("https://example.com") == "https://example.com"

    # Test domain extraction
    assert validator.extract_domain("https://api.example.com/v1") == "api.example.com"
    assert validator.extract_domain("https://example.com") == "example.com"

    # Test security check
    assert validator.is_secure("https://example.com") == True
    assert validator.is_secure("http://example.com") == False

    print("✓ URLValidator works correctly")
    return True

def test_authentication_manager():
    """Test authentication manager functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_16.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    manager = exercise.AuthenticationManager()

    # Test auth URL generation
    google_url = manager.generate_auth_url('google', 'https://app.example.com/callback')
    assert google_url is not None
    assert 'accounts.google.com' in google_url
    assert 'client_id=demo_app' in google_url

    github_url = manager.generate_auth_url('github', 'https://app.example.com/callback')
    assert github_url is not None
    assert 'github.com' in github_url

    # Test invalid provider
    invalid_url = manager.generate_auth_url('invalid', 'https://app.example.com/callback')
    assert invalid_url is None

    # Test OAuth flow simulation
    tokens = manager.simulate_oauth_flow('google', 'https://app.example.com/callback')
    assert 'access_token' in tokens
    assert tokens['token_type'] == 'Bearer'
    assert 'expires_in' in tokens

    # Test token validation
    token_data = manager.validate_token(tokens['access_token'])
    assert token_data is not None
    assert token_data['provider'] == 'google'
    assert 'user_id' in token_data

    print("✓ AuthenticationManager works correctly")
    return True

def test_elicitation_creation():
    """Test elicitation creation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_16.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test valid elicitation
    elicitation = exercise.create_auth_elicitation('google', 'https://app.example.com/callback')
    assert elicitation['mode'] == 'url'
    assert elicitation['provider'] == 'google'
    assert 'accounts.google.com' in elicitation['url']
    assert 'authenticate with Google' in elicitation['message']

    # Test invalid redirect URL
    try:
        exercise.create_auth_elicitation('google', 'http://insecure.com')
        assert False, "Should have raised ValueError for insecure URL"
    except ValueError:
        pass

    # Test invalid provider
    try:
        exercise.create_auth_elicitation('invalid', 'https://app.example.com/callback')
        assert False, "Should have raised ValueError for invalid provider"
    except ValueError:
        pass

    print("✓ create_auth_elicitation works correctly")
    return True

def test_oauth_callback():
    """Test OAuth callback handling"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_16.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test valid callback
    tokens = exercise.handle_oauth_callback('auth_code_google_123', 'secure_random')
    assert 'access_token' in tokens
    assert tokens['token_type'] == 'Bearer'

    # Test invalid auth code
    try:
        exercise.handle_oauth_callback('invalid_code', 'secure_random')
        assert False, "Should have raised ValueError for invalid code"
    except ValueError:
        pass

    # Test invalid state
    try:
        exercise.handle_oauth_callback('auth_code_google_123', 'invalid_state')
        assert False, "Should have raised ValueError for invalid state"
    except ValueError:
        pass

    print("✓ handle_oauth_callback works correctly")
    return True

def test_secure_api_call():
    """Test secure API calls"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_16.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # First get a valid token
    tokens = exercise.handle_oauth_callback('auth_code_google_123', 'secure_random')

    # Test valid API call
    response = exercise.secure_api_call('/user/profile', tokens['access_token'])
    assert response['status'] == 'success'
    assert 'name' in response['data']
    assert response['data']['name'] == 'John Doe'

    # Test invalid token
    try:
        exercise.secure_api_call('/user/profile', 'invalid_token')
        assert False, "Should have raised ValueError for invalid token"
    except ValueError:
        pass

    # Test unauthorized endpoint
    try:
        exercise.secure_api_call('/admin/stats', tokens['access_token'])
        assert False, "Should have raised ValueError for insufficient permissions"
    except ValueError:
        pass

    # Test unknown endpoint
    try:
        exercise.secure_api_call('/unknown', tokens['access_token'])
        assert False, "Should have raised ValueError for unknown endpoint"
    except ValueError:
        pass

    print("✓ secure_api_call works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 16 - URL Mode Elicitation\n")

    tests = [
        test_url_validator,
        test_authentication_manager,
        test_elicitation_creation,
        test_oauth_callback,
        test_secure_api_call
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
        print("🎉 All tests passed! You're ready for MCP Project 16!")
        print("You've mastered URL validation, OAuth flows, and secure API calls!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
