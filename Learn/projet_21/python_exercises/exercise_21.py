# Exercise 21: Token Scopes and Audiences
# Before implementing scoped tokens, let's practice granular authorization

from typing import Dict, List, Set, Optional
import time

# TODO: Create a class called 'ScopedTokenManager'
# - generate_scoped_token: creates token with specific scopes and audience
# - validate_scope: checks if token has required scope
# - validate_audience: checks if token is for correct audience
# - check_permissions: combines scope and audience validation

# TODO: Create a function called 'define_resource_permissions'
# Returns a dict mapping resources to required scopes
# Example: {'/api/users': ['read'], '/api/admin': ['admin']}

# TODO: Create a function called 'enforce_resource_access'
# Parameters: token (str), resource (str), action (str)
# Validates token has permission for resource + action
# Returns True if allowed, raises exception if denied

# TODO: Create a function called 'simulate_microservice_auth'
# Demonstrates cross-service authentication with different audiences

class ScopedTokenManager:
    """Manages tokens with scopes and audiences"""

    def __init__(self):
        self.tokens = {}
        self.resource_permissions = {
            '/api/users': ['read', 'write'],
            '/api/posts': ['read', 'write'],
            '/api/admin': ['admin'],
            '/api/analytics': ['read']
        }

    def generate_scoped_token(self, user_id: str, scopes: List[str],
                            audience: str, expires_in: int = 3600) -> str:
        """Generate token with specific scopes and audience"""
        import secrets
        token = secrets.token_urlsafe(32)

        self.tokens[token] = {
            'user_id': user_id,
            'scopes': set(scopes),
            'audience': audience,
            'issued_at': time.time(),
            'expires_at': time.time() + expires_in
        }

        return token

    def validate_token(self, token: str) -> Optional[Dict]:
        """Validate token exists and isn't expired"""
        if token not in self.tokens:
            return None

        token_data = self.tokens[token]
        if time.time() > token_data['expires_at']:
            del self.tokens[token]
            return None

        return token_data

    def validate_scope(self, token_data: Dict, required_scope: str) -> bool:
        """Check if token has required scope"""
        return required_scope in token_data.get('scopes', set())

    def validate_audience(self, token_data: Dict, required_audience: str) -> bool:
        """Check if token is for correct audience"""
        return token_data.get('audience') == required_audience

    def check_permissions(self, token: str, required_scopes: List[str],
                         required_audience: str) -> Dict:
        """Comprehensive permission check"""
        token_data = self.validate_token(token)
        if not token_data:
            raise ValueError("Invalid or expired token")

        # Check audience
        if not self.validate_audience(token_data, required_audience):
            raise ValueError(f"Token audience mismatch: expected {required_audience}")

        # Check all required scopes
        missing_scopes = []
        for scope in required_scopes:
            if not self.validate_scope(token_data, scope):
                missing_scopes.append(scope)

        if missing_scopes:
            raise ValueError(f"Missing required scopes: {missing_scopes}")

        return token_data

def define_resource_permissions() -> Dict[str, List[str]]:
    """Define permissions required for different resources"""
    return {
        '/api/users': ['read'],
        '/api/users/profile': ['read', 'write'],
        '/api/posts': ['read'],
        '/api/posts/create': ['write'],
        '/api/admin/users': ['admin'],
        '/api/admin/stats': ['admin', 'read'],
        '/api/analytics': ['read']
    }

def enforce_resource_access(token: str, resource: str, action: str) -> bool:
    """Enforce resource access control"""
    manager = ScopedTokenManager()
    permissions = define_resource_permissions()

    # Map action to scope
    scope_mapping = {
        'GET': 'read',
        'POST': 'write',
        'PUT': 'write',
        'DELETE': 'admin'
    }

    required_scope = scope_mapping.get(action.upper(), 'read')

    # Check if resource has specific permissions
    resource_scopes = permissions.get(resource, [required_scope])

    # For simplicity, assume audience is 'api-service'
    try:
        manager.check_permissions(token, resource_scopes, 'api-service')
        return True
    except ValueError as e:
        raise PermissionError(f"Access denied: {e}")

def simulate_microservice_auth():
    """Simulate authentication across microservices"""
    manager = ScopedTokenManager()

    # Generate tokens for different services
    user_service_token = manager.generate_scoped_token(
        'user123', ['read', 'write'], 'user-service'
    )

    analytics_service_token = manager.generate_scoped_token(
        'user123', ['read'], 'analytics-service'
    )

    admin_token = manager.generate_scoped_token(
        'admin456', ['admin', 'read', 'write'], 'admin-service'
    )

    return {
        'user_service': user_service_token,
        'analytics_service': analytics_service_token,
        'admin_service': admin_token,
        'manager': manager
    }

def main():
    """Demonstrate scoped token authorization"""
    try:
        print("=== Scoped Token Authorization Exercise ===\n")

        # Setup
        auth_system = simulate_microservice_auth()
        manager = auth_system['manager']

        print("Generated tokens for different services:")
        for service, token in auth_system.items():
            if service != 'manager':
                print(f"- {service}: {token[:15]}...")

        # Test resource access
        print("\nTesting resource access:")

        # User can access their profile
        try:
            enforce_resource_access(auth_system['user_service'], '/api/users/profile', 'GET')
            print("✅ User can read their profile")
        except Exception as e:
            print(f"❌ User profile access failed: {e}")

        # User cannot access admin stats
        try:
            enforce_resource_access(auth_system['user_service'], '/api/admin/stats', 'GET')
            print("❌ User should not access admin stats")
        except Exception as e:
            print(f"✅ Correctly denied admin access: {e}")

        # Admin can access admin stats
        try:
            enforce_resource_access(auth_system['admin_service'], '/api/admin/stats', 'GET')
            print("✅ Admin can access admin stats")
        except Exception as e:
            print(f"❌ Admin access failed: {e}")

        # Analytics token can access analytics but not user data
        try:
            enforce_resource_access(auth_system['analytics_service'], '/api/analytics', 'GET')
            print("✅ Analytics service can access analytics")
        except Exception as e:
            print(f"❌ Analytics access failed: {e}")

        try:
            enforce_resource_access(auth_system['analytics_service'], '/api/users', 'GET')
            print("❌ Analytics should not access user data")
        except Exception as e:
            print(f"✅ Correctly denied user data access: {e}")

        print("\n✅ Scoped token authorization demonstration completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
