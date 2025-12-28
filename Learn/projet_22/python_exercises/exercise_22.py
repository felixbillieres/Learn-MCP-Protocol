# Exercise 22: Advanced Security Features
# Before implementing advanced security, let's practice rate limiting and access control

from typing import Dict, List
import time
import threading

# TODO: Create a class called 'RateLimiter'
# - __init__: sets rate limits per user/IP
# - check_rate_limit: validates if request is within limits
# - record_request: logs request for rate tracking
# - get_remaining_requests: returns remaining allowed requests

# TODO: Create a class called 'SecurityMonitor'
# - detect_suspicious_activity: identifies potential security threats
# - log_security_event: records security-related events
# - block_ip: temporarily blocks suspicious IPs
# - generate_security_report: summarizes security events

# TODO: Create a function called 'secure_api_gateway'
# Parameters: request_data (dict)
# Simulates API gateway with rate limiting and security checks
# Returns response or raises security exception

class RateLimiter:
    """Implements rate limiting for API requests"""

    def __init__(self, requests_per_minute: int = 60):
        self.requests_per_minute = requests_per_minute
        self.requests = {}  # user_id -> list of timestamps
        self.lock = threading.Lock()

    def check_rate_limit(self, user_id: str) -> bool:
        """Check if user is within rate limits"""
        with self.lock:
            current_time = time.time()
            window_start = current_time - 60  # 1 minute window

            # Clean old requests
            if user_id in self.requests:
                self.requests[user_id] = [
                    req_time for req_time in self.requests[user_id]
                    if req_time > window_start
                ]

            # Check current count
            current_requests = len(self.requests.get(user_id, []))
            return current_requests < self.requests_per_minute

    def record_request(self, user_id: str):
        """Record a request for rate limiting"""
        with self.lock:
            if user_id not in self.requests:
                self.requests[user_id] = []
            self.requests[user_id].append(time.time())

    def get_remaining_requests(self, user_id: str) -> int:
        """Get remaining allowed requests"""
        with self.lock:
            current_requests = len(self.requests.get(user_id, []))
            return max(0, self.requests_per_minute - current_requests)

class SecurityMonitor:
    """Monitors and responds to security events"""

    def __init__(self):
        self.security_events = []
        self.blocked_ips = set()
        self.failed_attempts = {}  # ip -> count

    def detect_suspicious_activity(self, ip: str, user_agent: str, endpoint: str) -> bool:
        """Detect potentially suspicious activity"""
        # Simple heuristics
        suspicious = False

        if ip in self.blocked_ips:
            suspicious = True

        if self.failed_attempts.get(ip, 0) > 5:
            suspicious = True

        if endpoint.startswith('/admin') and 'suspicious' in user_agent.lower():
            suspicious = True

        return suspicious

    def log_security_event(self, event_type: str, details: Dict):
        """Log security event"""
        event = {
            'timestamp': time.time(),
            'type': event_type,
            'details': details
        }
        self.security_events.append(event)

    def block_ip(self, ip: str, duration_minutes: int = 15):
        """Temporarily block an IP address"""
        self.blocked_ips.add(ip)
        # In real implementation, would schedule unblocking
        self.log_security_event('ip_blocked', {'ip': ip, 'duration': duration_minutes})

    def record_failed_attempt(self, ip: str):
        """Record failed authentication attempt"""
        self.failed_attempts[ip] = self.failed_attempts.get(ip, 0) + 1

        if self.failed_attempts[ip] >= 5:
            self.block_ip(ip)

    def generate_security_report(self) -> Dict:
        """Generate security summary report"""
        return {
            'total_events': len(self.security_events),
            'blocked_ips': list(self.blocked_ips),
            'failed_attempts_by_ip': self.failed_attempts,
            'recent_events': self.security_events[-10:]  # Last 10 events
        }

def secure_api_gateway(request_data: Dict) -> Dict:
    """Secure API gateway with rate limiting and security checks"""
    rate_limiter = RateLimiter()
    security_monitor = SecurityMonitor()

    ip = request_data.get('ip', 'unknown')
    user_id = request_data.get('user_id', 'anonymous')
    endpoint = request_data.get('endpoint', '/')
    user_agent = request_data.get('user_agent', '')

    # Security checks
    if security_monitor.detect_suspicious_activity(ip, user_agent, endpoint):
        security_monitor.log_security_event('suspicious_activity_detected',
                                          {'ip': ip, 'endpoint': endpoint})
        raise SecurityException("Suspicious activity detected")

    # Rate limiting
    if not rate_limiter.check_rate_limit(user_id):
        security_monitor.log_security_event('rate_limit_exceeded',
                                          {'user_id': user_id, 'ip': ip})
        raise SecurityException("Rate limit exceeded")

    # Authentication check (simplified)
    if request_data.get('auth_token') != 'valid_token':
        security_monitor.record_failed_attempt(ip)
        raise SecurityException("Authentication failed")

    # Record successful request
    rate_limiter.record_request(user_id)
    security_monitor.log_security_event('successful_request',
                                      {'user_id': user_id, 'endpoint': endpoint})

    return {
        'status': 'success',
        'message': f'Welcome {user_id}!',
        'remaining_requests': rate_limiter.get_remaining_requests(user_id)
    }

class SecurityException(Exception):
    """Custom security exception"""
    pass

def main():
    """Demonstrate advanced security features"""
    try:
        print("=== Advanced Security Features Exercise ===\n")

        # Test rate limiting
        print("1. Rate Limiting:")
        limiter = RateLimiter(requests_per_minute=5)

        user_id = "test_user"
        for i in range(7):
            allowed = limiter.check_rate_limit(user_id)
            if allowed:
                limiter.record_request(user_id)
                print(f"Request {i+1}: ✅ Allowed ({limiter.get_remaining_requests(user_id)} remaining)")
            else:
                print(f"Request {i+1}: ❌ Rate limited")
                break

        # Test security monitoring
        print("\n2. Security Monitoring:")
        monitor = SecurityMonitor()

        # Normal request
        suspicious = monitor.detect_suspicious_activity("192.168.1.1", "Mozilla/5.0", "/api/users")
        print(f"Normal request suspicious: {suspicious}")

        # Failed attempts leading to blocking
        for i in range(6):
            monitor.record_failed_attempt("192.168.1.100")
            print(f"Failed attempt {i+1}")

        blocked = "192.168.1.100" in monitor.blocked_ips
        print(f"IP blocked after failed attempts: {blocked}")

        # Test API gateway
        print("\n3. Secure API Gateway:")

        # Valid request
        try:
            response = secure_api_gateway({
                'ip': '10.0.0.1',
                'user_id': 'user123',
                'auth_token': 'valid_token',
                'endpoint': '/api/profile',
                'user_agent': 'Mozilla/5.0'
            })
            print(f"✅ Valid request: {response['message']}")
        except SecurityException as e:
            print(f"❌ Unexpected error: {e}")

        # Suspicious request
        try:
            response = secure_api_gateway({
                'ip': '192.168.1.100',  # Blocked IP
                'user_id': 'hacker',
                'auth_token': 'valid_token',
                'endpoint': '/api/admin',
                'user_agent': 'suspicious scanner'
            })
            print("❌ Suspicious request should have been blocked")
        except SecurityException as e:
            print(f"✅ Suspicious request blocked: {e}")

        print("\n✅ Advanced security features demonstration completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
