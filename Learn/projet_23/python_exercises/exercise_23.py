# Exercise 23: Roots and Path Authorization
# Before implementing root-based authorization, let's practice path validation

from typing import List, Set, Optional
import os
from pathlib import Path

# TODO: Create a class called 'PathValidator'
# - __init__: stores authorized root directories
# - add_root: adds an authorized root path
# - validate_path: checks if path is within authorized roots
# - resolve_path: safely resolves relative paths
# - get_relative_path: gets path relative to root

# TODO: Create a function called 'setup_project_roots'
# Creates a set of authorized project directories
# Returns PathValidator instance

# TODO: Create a function called 'secure_file_operation'
# Parameters: operation (str), file_path (str), validator (PathValidator)
# Validates path before allowing file operation
# Returns operation result or raises SecurityError

class PathValidator:
    """Validates file paths against authorized root directories"""

    def __init__(self):
        self.authorized_roots: Set[str] = set()

    def add_root(self, root_path: str):
        """Add an authorized root directory"""
        # Normalize path
        normalized = os.path.abspath(root_path)
        self.authorized_roots.add(normalized)

    def validate_path(self, file_path: str) -> bool:
        """Check if file path is within authorized roots"""
        try:
            abs_file_path = os.path.abspath(file_path)

            for root in self.authorized_roots:
                # Check if file path starts with root path
                if abs_file_path.startswith(root + os.sep) or abs_file_path == root:
                    return True

            return False
        except:
            return False

    def resolve_path(self, relative_path: str, root: str) -> Optional[str]:
        """Safely resolve relative path within root"""
        try:
            # Ensure root is authorized
            if not self.validate_path(root):
                return None

            # Resolve the path
            full_path = os.path.join(root, relative_path)
            abs_path = os.path.abspath(full_path)

            # Ensure result is still within root
            if not abs_path.startswith(root + os.sep) and abs_path != root:
                return None

            return abs_path
        except:
            return None

    def get_relative_path(self, file_path: str) -> Optional[str]:
        """Get path relative to appropriate root"""
        abs_path = os.path.abspath(file_path)

        for root in self.authorized_roots:
            try:
                if abs_path.startswith(root + os.sep):
                    return os.path.relpath(abs_path, root)
                elif abs_path == root:
                    return "."
            except:
                continue

        return None

def setup_project_roots() -> PathValidator:
    """Setup validator with common project directories"""
    validator = PathValidator()

    # Add common project roots (simulated)
    validator.add_root("/home/user/projects")
    validator.add_root("/home/user/documents")
    validator.add_root("/tmp/safe_zone")

    return validator

def secure_file_operation(operation: str, file_path: str, validator: PathValidator) -> str:
    """Perform secure file operation with path validation"""
    if not validator.validate_path(file_path):
        raise SecurityError(f"Access denied: {file_path} is outside authorized roots")

    # Simulate file operations
    if operation == "read":
        try:
            with open(file_path, 'r') as f:
                return f"Read {len(f.read())} characters from {file_path}"
        except FileNotFoundError:
            return f"File not found: {file_path}"
        except Exception as e:
            return f"Read error: {e}"

    elif operation == "write":
        try:
            with open(file_path, 'w') as f:
                f.write("Secure file content")
            return f"Successfully wrote to {file_path}"
        except Exception as e:
            return f"Write error: {e}"

    elif operation == "list":
        try:
            if os.path.isdir(file_path):
                items = os.listdir(file_path)
                return f"Directory {file_path} contains: {items}"
            else:
                return f"Not a directory: {file_path}"
        except Exception as e:
            return f"List error: {e}"

    else:
        raise ValueError(f"Unsupported operation: {operation}")

class SecurityError(Exception):
    """Security-related exception"""
    pass

def main():
    """Demonstrate root-based path authorization"""
    try:
        print("=== Root-Based Path Authorization Exercise ===\n")

        # Setup validator
        validator = setup_project_roots()

        print("Authorized roots:")
        for root in validator.authorized_roots:
            print(f"- {root}")

        # Test path validation
        print("\nPath validation:")

        valid_paths = [
            "/home/user/projects/main.py",
            "/home/user/documents/notes.txt",
            "/tmp/safe_zone/data.json"
        ]

        invalid_paths = [
            "/etc/passwd",  # System file
            "/home/otheruser/secret.txt",  # Different user
            "../../../etc/shadow"  # Path traversal attempt
        ]

        for path in valid_paths + invalid_paths:
            is_valid = validator.validate_path(path)
            status = "✅" if is_valid else "❌"
            print(f"{status} {path}")

        # Test secure operations
        print("\nSecure file operations:")

        # Valid operation
        try:
            # Create a test file in temp directory
            test_file = "/tmp/safe_zone/test.txt"
            with open(test_file, 'w') as f:
                f.write("test content")

            result = secure_file_operation("read", test_file, validator)
            print(f"✅ {result}")
        except Exception as e:
            print(f"❌ Error: {e}")

        # Invalid operation (outside roots)
        try:
            result = secure_file_operation("read", "/etc/hostname", validator)
            print("❌ Should have been blocked")
        except SecurityError as e:
            print(f"✅ Correctly blocked: {e}")

        # Test path resolution
        print("\nPath resolution:")
        resolved = validator.resolve_path("subdir/file.txt", "/home/user/projects")
        if resolved:
            print(f"✅ Resolved: {resolved}")
        else:
            print("❌ Resolution failed")

        print("\n✅ Root-based path authorization demonstration completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
