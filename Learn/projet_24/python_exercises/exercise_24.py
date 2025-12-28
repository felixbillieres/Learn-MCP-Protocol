# Exercise 24: Transport Configuration
# Before implementing multi-transport servers, let's practice transport detection and optimization

from typing import Dict, Any, Optional
import os
import sys

# TODO: Create a class called 'TransportDetector'
# - detect_transport: identifies current transport (stdio, http, websocket)
# - get_transport_config: returns optimal config for transport
# - validate_transport_support: checks if transport is supported

# TODO: Create a class called 'ServerConfig'
# - __init__: sets base configuration
# - optimize_for_transport: adjusts config based on transport
# - get_config: returns current configuration
# - validate_config: ensures config is valid

# TODO: Create a function called 'auto_configure_server'
# Detects transport and returns optimized server config
# Demonstrates automatic configuration

class TransportDetector:
    """Detects and analyzes MCP transport types"""

    def detect_transport(self) -> str:
        """Detect the current transport mechanism"""
        # Check environment variables (common in MCP)
        if os.environ.get('MCP_TRANSPORT') == 'http':
            return 'http'
        elif os.environ.get('MCP_TRANSPORT') == 'websocket':
            return 'websocket'
        elif os.environ.get('MCP_TRANSPORT') == 'stdio':
            return 'stdio'

        # Check for HTTP indicators
        if 'REQUEST_METHOD' in os.environ:
            return 'http'

        # Check for stdio indicators (parent process, pipes)
        if hasattr(sys.stdin, 'isatty') and not sys.stdin.isatty():
            return 'stdio'

        # Default to stdio for safety
        return 'stdio'

    def get_transport_config(self, transport: str) -> Dict[str, Any]:
        """Get optimal configuration for transport"""
        configs = {
            'stdio': {
                'buffer_size': 8192,
                'encoding': 'utf-8',
                'timeout': 30,
                'concurrency': 1
            },
            'http': {
                'buffer_size': 65536,
                'encoding': 'utf-8',
                'timeout': 60,
                'concurrency': 100,
                'max_request_size': '10MB'
            },
            'websocket': {
                'buffer_size': 32768,
                'encoding': 'utf-8',
                'timeout': 300,
                'concurrency': 1000,
                'heartbeat_interval': 30
            }
        }
        return configs.get(transport, configs['stdio'])

    def validate_transport_support(self, transport: str) -> bool:
        """Check if transport is supported"""
        supported = ['stdio', 'http', 'websocket']
        return transport in supported

class ServerConfig:
    """Server configuration optimized for different transports"""

    def __init__(self):
        self.base_config = {
            'host': 'localhost',
            'port': 3000,
            'debug': False,
            'log_level': 'info'
        }
        self.transport_config = {}

    def optimize_for_transport(self, transport: str):
        """Optimize configuration for specific transport"""
        detector = TransportDetector()
        transport_config = detector.get_transport_config(transport)

        # Apply transport-specific optimizations
        if transport == 'stdio':
            self.base_config.update({
                'debug': True,
                'log_level': 'debug',
                'structured_logging': False
            })
        elif transport == 'http':
            self.base_config.update({
                'debug': False,
                'log_level': 'warning',
                'structured_logging': True,
                'cors_enabled': True
            })
        elif transport == 'websocket':
            self.base_config.update({
                'debug': False,
                'log_level': 'info',
                'structured_logging': True,
                'compression_enabled': True
            })

        self.transport_config = transport_config

    def get_config(self) -> Dict[str, Any]:
        """Get complete server configuration"""
        config = self.base_config.copy()
        config['transport'] = self.transport_config
        return config

    def validate_config(self) -> bool:
        """Validate current configuration"""
        config = self.get_config()

        # Basic validations
        if not isinstance(config.get('port'), int) or config['port'] <= 0:
            return False

        if config.get('log_level') not in ['debug', 'info', 'warning', 'error']:
            return False

        return True

def auto_configure_server() -> Dict[str, Any]:
    """Automatically configure server based on detected transport"""
    detector = TransportDetector()
    config = ServerConfig()

    transport = detector.detect_transport()
    print(f"Detected transport: {transport}")

    config.optimize_for_transport(transport)

    if not config.validate_config():
        raise ValueError("Invalid configuration generated")

    return config.get_config()

def main():
    """Demonstrate transport-based server configuration"""
    try:
        print("=== Transport-Based Server Configuration Exercise ===\n")

        # Test transport detection
        detector = TransportDetector()

        print("Transport detection:")
        transport = detector.detect_transport()
        print(f"Current transport: {transport}")

        # Test configurations for different transports
        transports = ['stdio', 'http', 'websocket']

        print("\nTransport configurations:")
        for t in transports:
            config = detector.get_transport_config(t)
            print(f"{t.upper()}: buffer={config['buffer_size']}, timeout={config['timeout']}, concurrency={config['concurrency']}")

        # Test server configuration
        print("\nServer configuration optimization:")

        for transport in transports:
            server_config = ServerConfig()
            server_config.optimize_for_transport(transport)
            config = server_config.get_config()

            print(f"\n{transport.upper()} optimized config:")
            print(f"  Debug: {config['debug']}")
            print(f"  Log level: {config['log_level']}")
            print(f"  Buffer size: {config['transport']['buffer_size']}")
            print(f"  Concurrency: {config['transport']['concurrency']}")

        # Test auto-configuration
        print("\nAuto-configuration:")
        try:
            auto_config = auto_configure_server()
            print("✅ Auto-configuration successful"            print(f"Final config keys: {list(auto_config.keys())}")
        except Exception as e:
            print(f"❌ Auto-configuration failed: {e}")

        print("\n✅ Transport configuration demonstration completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
