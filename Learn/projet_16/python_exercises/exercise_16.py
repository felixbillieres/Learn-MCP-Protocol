# Exercise 16: URL Mode Elicitation
# Before using URL elicitation for authentication, let's practice URL handling and validation

import re
from urllib.parse import urlparse, urljoin
from typing import Optional, Dict, Any

# TODO: Create a class called 'URLValidator'
# - validate_url: checks if URL is valid and secure (HTTPS)
# - normalize_url: ensures URL has proper format
# - extract_domain: gets domain from URL
# - is_secure: checks if URL uses HTTPS

# TODO: Create a class called 'AuthenticationManager'
# - __init__: stores valid auth URLs and tokens
# - generate_auth_url: creates authentication URL with parameters
# - validate_token: checks if token is valid and not expired
# - simulate_oauth_flow: simulates the complete OAuth flow

# TODO: Create a function called 'create_auth_elicitation'
# Parameters: provider (str like 'google', 'github'), redirect_url (str)
# This function should:
# - Validate the redirect URL
# - Generate the appropriate auth URL for the provider
# - Return elicitation data for URL mode

# TODO: Create a function called 'handle_oauth_callback'
# Parameters: auth_code (str), state (str)
# This function should:
# - Validate the auth code format
# - Check state parameter for security
# - Exchange code for token (simulated)
# - Return access token info

# TODO: Create a function called 'secure_api_call'
# Parameters: endpoint (str), token (str), method (str, default 'GET')
# This function should:
# - Validate the token
# - Check if endpoint is allowed
# - Simulate API call with proper headers
# - Return response data

class URLValidator:
    """Validates and processes URLs for security"""

    def __init__(self):
        self.allowed_schemes = ['https']
        self.blocked_domains = ['localhost', '127.0.0.1', '0.0.0.0']

    def validate_url(self, url: str) -> bool:
        """Validate URL format and security"""
        try:
            parsed = urlparse(url)
            # Check scheme
            if parsed.scheme not in self.allowed_schemes:
                return False
            # Check domain
            if parsed.hostname in self.blocked_domains:
                return False
            # Check for basic URL structure
            return bool(parsed.netloc and parsed.scheme)
        except:
            return False

    def normalize_url(self, url: str) -> str:
        """Ensure URL has proper format"""
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url

    def extract_domain(self, url: str) -> Optional[str]:
        """Extract domain from URL"""
        try:
            parsed = urlparse(url)
            return parsed.netloc
        except:
            return None

    def is_secure(self, url: str) -> bool:
        """Check if URL uses HTTPS"""
        try:
            parsed = urlparse(url)
            return parsed.scheme == 'https'
        except:
            return False

class AuthenticationManager:
    """Manages authentication URLs and tokens"""

    def __init__(self):
        self.providers = {
            'google': 'https://accounts.google.com/oauth/authorize',
            'github': 'https://github.com/login/oauth/authorize',
            'microsoft': 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
        }
        self.valid_tokens = {}
        self.token_counter = 0

    def generate_auth_url(self, provider: str, redirect_url: str, scope: str = 'read') -> Optional[str]:
        """Generate OAuth authorization URL"""
        if provider not in self.providers:
            return None

        base_url = self.providers[provider]
        params = f'?client_id=demo_app&redirect_uri={redirect_url}&scope={scope}&response_type=code&state=secure_random'
        return base_url + params

    def validate_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Validate access token"""
        if token in self.valid_tokens:
            token_data = self.valid_tokens[token]
            # Check expiration (simplified)
            if token_data.get('expires_at', 0) > 0:  # Would check against current time
                return token_data
        return None

    def simulate_oauth_flow(self, provider: str, redirect_url: str) -> Dict[str, Any]:
        """Simulate complete OAuth flow"""
        # Generate auth URL
        auth_url = self.generate_auth_url(provider, redirect_url)
        if not auth_url:
            raise ValueError(f"Unsupported provider: {provider}")

        # Simulate user authorization
        auth_code = f"auth_code_{provider}_{self.token_counter}"

        # Exchange code for token
        self.token_counter += 1
        access_token = f"access_token_{self.token_counter}"

        # Store token
        self.valid_tokens[access_token] = {
            'provider': provider,
            'user_id': f'user_{self.token_counter}',
            'scope': ['read', 'profile'],
            'expires_at': 3600,  # Would be timestamp
            'token_type': 'Bearer'
        }

        return {
            'access_token': access_token,
            'token_type': 'Bearer',
            'expires_in': 3600,
            'scope': 'read profile'
        }

def create_auth_elicitation(provider: str, redirect_url: str) -> Dict[str, Any]:
    """Create elicitation data for URL mode authentication"""
    validator = URLValidator()
    manager = AuthenticationManager()

    # Validate redirect URL
    if not validator.validate_url(redirect_url):
        raise ValueError("Invalid redirect URL")

    # Generate auth URL
    auth_url = manager.generate_auth_url(provider, redirect_url)
    if not auth_url:
        raise ValueError(f"Unsupported authentication provider: {provider}")

    return {
        "mode": "url",
        "message": f"Please authenticate with {provider.capitalize()}. You'll be redirected to complete the login process.",
        "url": auth_url,
        "provider": provider,
        "redirect_url": redirect_url
    }

def handle_oauth_callback(auth_code: str, state: str) -> Dict[str, Any]:
    """Handle OAuth callback and token exchange"""
    # Validate auth code format
    if not auth_code or not auth_code.startswith('auth_code_'):
        raise ValueError("Invalid authorization code")

    # Validate state parameter (CSRF protection)
    if state != 'secure_random':
        raise ValueError("Invalid state parameter")

    # Simulate token exchange
    manager = AuthenticationManager()
    # Extract provider from auth code
    provider = auth_code.split('_')[2] if len(auth_code.split('_')) >= 3 else 'google'

    return manager.simulate_oauth_flow(provider, 'https://app.example.com/callback')

def secure_api_call(endpoint: str, token: str, method: str = 'GET') -> Dict[str, Any]:
    """Make authenticated API call"""
    manager = AuthenticationManager()

    # Validate token
    token_data = manager.validate_token(token)
    if not token_data:
        raise ValueError("Invalid or expired token")

    # Check endpoint access based on scope
    scope = token_data.get('scope', [])
    if endpoint.startswith('/admin') and 'admin' not in scope:
        raise ValueError("Insufficient permissions for admin endpoint")

    # Simulate API response
    responses = {
        '/user/profile': {'user_id': token_data['user_id'], 'name': 'John Doe', 'email': 'john@example.com'},
        '/user/settings': {'theme': 'dark', 'notifications': True},
        '/admin/stats': {'total_users': 1234, 'active_sessions': 89}
    }

    if endpoint in responses:
        return {
            'status': 'success',
            'data': responses[endpoint],
            'request': {
                'endpoint': endpoint,
                'method': method,
                'authorization': f'Bearer {token[:10]}...'
            }
        }
    else:
        raise ValueError(f"Endpoint not found: {endpoint}")

def main():
    """Demonstrate URL elicitation and authentication"""
    try:
        # Test URL validation
        validator = URLValidator()
        print("URL Validation:")
        print(f"  https://example.com: {validator.validate_url('https://example.com')}")
        print(f"  http://example.com: {validator.validate_url('http://example.com')}")
        print(f"  invalid-url: {validator.validate_url('invalid-url')}")

        # Test auth elicitation
        print("\nAuthentication Elicitation:")
        elicitation = create_auth_elicitation('google', 'https://app.example.com/callback')
        print(f"Mode: {elicitation['mode']}")
        print(f"Message: {elicitation['message']}")
        print(f"URL: {elicitation['url'][:50]}...")

        # Test OAuth flow
        print("\nOAuth Flow:")
        tokens = handle_oauth_callback('auth_code_google_123', 'secure_random')
        print(f"Access Token: {tokens['access_token'][:20]}...")

        # Test API call
        print("\nAPI Call:")
        response = secure_api_call('/user/profile', tokens['access_token'])
        print(f"Status: {response['status']}")
        print(f"User: {response['data']['name']}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
