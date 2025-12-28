# Exercise 20: OAuth Token Validation
# Before implementing OAuth validation, let's practice token management and security

import hashlib
import time
from typing import Dict, Optional, Any
import secrets

# TODO: Create a class called 'TokenManager'
# - generate_token: creates new access tokens
# - validate_token: checks token validity and permissions
# - revoke_token: invalidates a token
# - list_active_tokens: returns all valid tokens

# TODO: Create a function called 'parse_bearer_token'
# Parameters: auth_header (str)
# Extracts token from "Bearer <token>" format
# Returns token or None if invalid format

# TODO: Create a function called 'check_token_scopes'
# Parameters: token_data (dict), required_scopes (list)
# Validates that token has all required scopes
# Returns True if authorized, raises exception if not

# TODO: Create a function called 'simulate_oauth_server'
# Creates a mock OAuth server with token management
# Returns token manager instance

# TODO: Create a function called 'secure_endpoint'
# Parameters: token (str), required_scopes (list), endpoint_data (dict)
# Simulates accessing a protected endpoint
# Returns response data or raises security exception

class TokenManager:
    """Manages OAuth access tokens"""

    def __init__(self):
        self.tokens = {}
        self.revoked_tokens = set()

    def generate_token(self, user_id: str, scopes: list, expires_in: int = 3600) -> str:
        """Generate a new access token"""
        token = secrets.token_urlsafe(32)
        expiration = time.time() + expires_in

        self.tokens[token] = {
            'user_id': user_id,
            'scopes': scopes,
            'issued_at': time.time(),
            'expires_at': expiration,
            'token_type': 'Bearer'
        }

        return token

    def validate_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Validate token and return token data if valid"""
        if token in self.revoked_tokens:
            return None

        if token not in self.tokens:
            return None

        token_data = self.tokens[token]

        # Check expiration
        if time.time() > token_data['expires_at']:
            del self.tokens[token]  # Clean up expired token
            return None

        return token_data

    def revoke_token(self, token: str) -> bool:
        """Revoke a token"""
        if token in self.tokens:
            self.revoked_tokens.add(token)
            del self.tokens[token]
            return True
        return False

    def list_active_tokens(self) -> list:
        """List all active (non-expired, non-revoked) tokens"""
        active = []
        current_time = time.time()

        for token, data in self.tokens.items():
            if token not in self.revoked_tokens and current_time <= data['expires_at']:
                active.append({
                    'token_preview': token[:10] + '...',
                    'user_id': data['user_id'],
                    'scopes': data['scopes'],
                    'expires_in': int(data['expires_at'] - current_time)
                })

        return active

def parse_bearer_token(auth_header: str) -> Optional[str]:
    """Parse Bearer token from Authorization header"""
    if not auth_header or not auth_header.startswith('Bearer '):
        return None

    token = auth_header[7:].strip()  # Remove 'Bearer ' prefix
    if not token:
        return None

    return token

def check_token_scopes(token_data: Dict[str, Any], required_scopes: list) -> bool:
    """Check if token has required scopes"""
    if not token_data or 'scopes' not in token_data:
        raise ValueError("Invalid token data")

    token_scopes = set(token_data['scopes'])
    required_set = set(required_scopes)

    missing_scopes = required_set - token_scopes
    if missing_scopes:
        raise ValueError(f"Missing required scopes: {list(missing_scopes)}")

    return True

def simulate_oauth_server() -> TokenManager:
    """Create a simulated OAuth server"""
    return TokenManager()

def secure_endpoint(token: str, required_scopes: list, endpoint_data: Dict[str, Any]) -> Dict[str, Any]:
    """Access a secure endpoint with token validation"""
    manager = simulate_oauth_server()

    # Validate token
    token_data = manager.validate_token(token)
    if not token_data:
        raise ValueError("Invalid or expired token")

    # Check scopes
    check_token_scopes(token_data, required_scopes)

    # Simulate endpoint response
    endpoint_type = endpoint_data.get('type', 'data')

    if endpoint_type == 'user_profile':
        return {
            'user_id': token_data['user_id'],
            'name': 'John Doe',
            'email': f"{token_data['user_id']}@example.com",
            'scopes': token_data['scopes']
        }
    elif endpoint_type == 'admin_stats':
        if 'admin' not in token_data['scopes']:
            raise ValueError("Admin scope required")
        return {
            'total_users': 1234,
            'active_sessions': 89,
            'server_status': 'healthy'
        }
    else:
        return {'message': 'Endpoint accessed successfully', 'data': endpoint_data}

def main():
    """Demonstrate OAuth token validation"""
    try:
        print("=== OAuth Token Validation Exercise ===\n")

        # Create OAuth server
        oauth = simulate_oauth_server()

        # Generate tokens
        user_token = oauth.generate_token('user123', ['read', 'profile'])
        admin_token = oauth.generate_token('admin456', ['read', 'write', 'admin'])

        print("Generated tokens:")
        print(f"User token: {user_token[:20]}...")
        print(f"Admin token: {admin_token[:20]}...")

        # Test token validation
        user_data = oauth.validate_token(user_token)
        admin_data = oauth.validate_token(admin_token)

        print("
Token validation:")
        print(f"User token valid: {user_data is not None}")
        print(f"Admin token valid: {admin_data is not None}")

        # Test Bearer token parsing
        auth_header = f"Bearer {user_token}"
        parsed_token = parse_bearer_token(auth_header)
        print(f"\nParsed token: {parsed_token == user_token}")

        # Test secure endpoints
        print("\nTesting secure endpoints:")

        # User endpoint (should work)
        try:
            result = secure_endpoint(user_token, ['read'], {'type': 'user_profile'})
            print(f"User profile access: ✅ {result['name']}")
        except Exception as e:
            print(f"User profile access: ❌ {e}")

        # Admin endpoint with user token (should fail)
        try:
            result = secure_endpoint(user_token, ['admin'], {'type': 'admin_stats'})
            print("Admin stats access: ❌ Should have failed")
        except Exception as e:
            print(f"Admin stats access: ✅ Correctly denied - {e}")

        # Admin endpoint with admin token (should work)
        try:
            result = secure_endpoint(admin_token, ['admin'], {'type': 'admin_stats'})
            print(f"Admin stats access: ✅ {result['total_users']} users")
        except Exception as e:
            print(f"Admin stats access: ❌ {e}")

        # Token revocation
        print(f"\nActive tokens before revocation: {len(oauth.list_active_tokens())}")
        oauth.revoke_token(user_token)
        print(f"Active tokens after revocation: {len(oauth.list_active_tokens())}")

        print("\n✅ OAuth token validation demonstration completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
