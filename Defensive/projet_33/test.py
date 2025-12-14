"""
Test script for project 33
This script verifies the SIEM system
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
    
    if not hasattr(solution, 'SecurityEvent'):
        print("The model 'SecurityEvent' does not exist")
        return False
    
    if not hasattr(solution, 'Rule'):
        print("The model 'Rule' does not exist")
        return False
    
    if not hasattr(solution, 'Alert'):
        print("The model 'Alert' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_collect_event():
    """Test event collection"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'events'):
        solution.events.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.collect_event(
            "firewall", "blocked", "high", {"ip": "1.2.3.4"}, mock_ctx
        )
        
        if not isinstance(result, solution.SecurityEvent):
            print(f"collect_event should return SecurityEvent, but returned {type(result)}")
            return False
        
        if result.source != "firewall":
            print(f"Event source should be 'firewall', but is '{result.source}'")
            return False
        
        if len(solution.events) != 1:
            print(f"Event should be added, but list contains {len(solution.events)} events")
            return False
        
        print("collect_event works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_analyze_events():
    """Test event analysis and alert generation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'events'):
        solution.events.clear()
    if hasattr(solution, 'alerts'):
        solution.alerts.clear()
    
    mock_ctx = AsyncMock()
    
    # Collect some events first
    await solution.collect_event("firewall", "blocked", "high", {"ip": "1.2.3.4"}, mock_ctx)
    await solution.collect_event("firewall", "blocked", "high", {"ip": "1.2.3.4"}, mock_ctx)
    
    try:
        result = await solution.analyze_events(None, mock_ctx)
        
        if not isinstance(result, list):
            print(f"analyze_events should return a list, but returned {type(result)}")
            return False
        
        print(f"analyze_events works: generated {len(result)} alerts")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_create_rule():
    """Test rule creation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'rules'):
        solution.rules.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.create_rule(
            "Multiple Failed Logins",
            "3 failed login attempts in 5 minutes",
            "high",
            mock_ctx
        )
        
        if not isinstance(result, solution.Rule):
            print(f"create_rule should return Rule, but returned {type(result)}")
            return False
        
        if result.name != "Multiple Failed Logins":
            print(f"Rule name should be 'Multiple Failed Logins', but is '{result.name}'")
            return False
        
        if hasattr(solution, 'rules') and len(solution.rules) == 0:
            print("Rule should be stored in rules dictionary")
            return False
        
        print("create_rule works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_list_alerts():
    """Test listing alerts with filters"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'events'):
        solution.events.clear()
    if hasattr(solution, 'alerts'):
        solution.alerts.clear()
    
    mock_ctx = AsyncMock()
    
    # Create some events and analyze them
    await solution.collect_event("firewall", "blocked", "high", {"ip": "1.2.3.4"}, mock_ctx)
    await solution.collect_event("ids", "intrusion", "critical", {"attack": "sql_injection"}, mock_ctx)
    await solution.analyze_events(None, mock_ctx)
    
    try:
        # Test list all
        all_alerts = await solution.list_alerts(None, mock_ctx)
        if not isinstance(all_alerts, list):
            print(f"list_alerts should return a list, but returned {type(all_alerts)}")
            return False
        
        # Test filter by severity
        high_alerts = await solution.list_alerts("high", mock_ctx)
        if not isinstance(high_alerts, list):
            print(f"list_alerts should return a list when filtered, but returned {type(high_alerts)}")
            return False
        
        print(f"list_alerts works: found {len(all_alerts)} total alerts, {len(high_alerts)} high severity")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 33\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing collect_event...")
    success = asyncio.run(test_collect_event()) and success
    print()
    
    print("Testing analyze_events...")
    success = asyncio.run(test_analyze_events()) and success
    print()
    
    print("Testing create_rule...")
    success = asyncio.run(test_create_rule()) and success
    print()
    
    print("Testing list_alerts...")
    success = asyncio.run(test_list_alerts()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional SIEM system!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
