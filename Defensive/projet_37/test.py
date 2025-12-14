"""
Test script for project 37
This script verifies the firewall rules manager
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock

def test_models_exist():
    """Test that models exist"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error during import: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    if not hasattr(solution, 'FirewallRule'):
        print("The model 'FirewallRule' does not exist")
        return False
    
    if not hasattr(solution, 'NetworkPolicy'):
        print("The model 'NetworkPolicy' does not exist")
        return False
    
    print("Models exist")
    return True

def test_validation_helpers():
    """Test validation helper functions"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'validate_ip'):
        assert solution.validate_ip("192.168.1.1") == True
        assert solution.validate_ip("invalid") == False
        print("validate_ip works")
    
    if hasattr(solution, 'validate_port'):
        assert solution.validate_port(80) == True
        assert solution.validate_port(70000) == False
        print("validate_port works")
    
    return True

async def test_create_rule():
    """Test firewall rule creation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'rules'):
        solution.rules.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.create_rule(
            "Allow SSH",
            "allow",
            source_ip="192.168.1.0/24",
            dest_port=22,
            protocol="tcp",
            ctx=mock_ctx
        )
        
        if not isinstance(result, solution.FirewallRule):
            print(f"create_rule should return FirewallRule, but returned {type(result)}")
            return False
        
        if result.name != "Allow SSH":
            print(f"Rule name should be 'Allow SSH', but is '{result.name}'")
            return False
        
        if len(solution.rules) != 1:
            print(f"Rule should be added, but list contains {len(solution.rules)} rules")
            return False
        
        print("create_rule works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_list_rules():
    """Test listing firewall rules"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'rules'):
        solution.rules.clear()
    
    mock_ctx = AsyncMock()
    
    # Create multiple rules
    r1 = await solution.create_rule("Rule 1", "allow", ctx=mock_ctx)
    r2 = await solution.create_rule("Rule 2", "deny", ctx=mock_ctx)
    
    try:
        all_rules = await solution.list_rules(False, mock_ctx)
        if len(all_rules) != 2:
            print(f"Should return 2 rules, but returned {len(all_rules)}")
            return False
        
        enabled_rules = await solution.list_rules(True, mock_ctx)
        if not isinstance(enabled_rules, list):
            print(f"list_rules should return a list")
            return False
        
        print("list_rules works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_modify_rule():
    """Test modifying a firewall rule with authorization"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'rules'):
        solution.rules.clear()
    
    mock_ctx = AsyncMock()
    
    rule = await solution.create_rule("Test Rule", "allow", ctx=mock_ctx)
    
    try:
        result = await solution.modify_rule(
            rule.id,
            token="Bearer valid_token",
            action="deny",
            ctx=mock_ctx
        )
        
        if not isinstance(result, solution.FirewallRule):
            print(f"modify_rule should return FirewallRule, but returned {type(result)}")
            return False
        
        if result.action != "deny":
            print("Rule action should be updated to 'deny'")
            return False
        
        print("modify_rule works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_delete_rule():
    """Test deleting a firewall rule with authorization"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'rules'):
        solution.rules.clear()
    
    mock_ctx = AsyncMock()
    
    rule = await solution.create_rule("To Delete", "allow", ctx=mock_ctx)
    rule_id = rule.id
    
    try:
        result = await solution.delete_rule(rule_id, "Bearer valid_token", mock_ctx)
        
        if not isinstance(result, bool):
            print(f"delete_rule should return a bool, but returned {type(result)}")
            return False
        
        if not result:
            print("delete_rule should return True on success")
            return False
        
        # Verify rule is removed
        rules = await solution.list_rules(False, mock_ctx)
        if len(rules) != 0:
            print("Rule should be removed from the list")
            return False
        
        print("delete_rule works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_create_policy():
    """Test creating a network policy"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'rules'):
        solution.rules.clear()
    
    mock_ctx = AsyncMock()
    
    r1 = await solution.create_rule("Rule 1", "allow", ctx=mock_ctx)
    r2 = await solution.create_rule("Rule 2", "allow", ctx=mock_ctx)
    
    try:
        result = await solution.create_policy(
            "Web Policy",
            [r1.id, r2.id],
            ["server1", "server2"],
            ctx=mock_ctx
        )
        
        if not isinstance(result, solution.NetworkPolicy):
            print(f"create_policy should return NetworkPolicy, but returned {type(result)}")
            return False
        
        if result.name != "Web Policy":
            print(f"Policy name should be 'Web Policy', but is '{result.name}'")
            return False
        
        print("create_policy works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 37\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    success = test_validation_helpers() and success
    print()
    
    print("Testing create_rule...")
    success = asyncio.run(test_create_rule()) and success
    print()
    
    print("Testing list_rules...")
    success = asyncio.run(test_list_rules()) and success
    print()
    
    print("Testing modify_rule...")
    success = asyncio.run(test_modify_rule()) and success
    print()
    
    print("Testing delete_rule...")
    success = asyncio.run(test_delete_rule()) and success
    print()
    
    print("Testing create_policy...")
    success = asyncio.run(test_create_policy()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional firewall manager!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
