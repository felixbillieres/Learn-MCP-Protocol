"""
Test script for Python Exercise 33
Tests SIEM event processing and alerting
"""

import sys
import importlib.util

def test_event_processor():
    """Test event processing functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_33.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    processor = exercise.EventProcessor()

    # Test event processing
    raw_event = {
        'source': '192.168.1.100',
        'event_type': 'LOGIN',
        'severity': 'HIGH',
        'details': {'user': 'admin'}
    }

    event = processor.process_event(raw_event)

    assert isinstance(event, exercise.SecurityEvent)
    assert event.source == '192.168.1.100'
    assert event.event_type == 'login'  # Normalized
    assert event.severity == 'high'  # Normalized
    assert 'risk_score' in event.details

    print("✓ EventProcessor works correctly")
    return True

def test_alert_engine():
    """Test alert generation and correlation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_33.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    engine = exercise.AlertEngine()

    # Add a rule
    rule = exercise.DetectionRule("test_rule", "Test Rule", "authentication.*failure", "medium")
    engine.add_rule(rule)

    # Create a matching event
    processor = exercise.EventProcessor()
    event = processor.process_event({
        'source': '192.168.1.100',
        'event_type': 'authentication',
        'severity': 'medium',
        'details': {'result': 'failure'}
    })

    # Test rule evaluation
    alerts = engine.evaluate_rules(event)
    assert len(alerts) == 1
    assert alerts[0].rule_id == "test_rule"
    assert alerts[0].severity == "medium"

    print("✓ AlertEngine works correctly")
    return True

def test_siem_database():
    """Test database storage and querying"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_33.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    database = exercise.SIEMDatabase()
    processor = exercise.EventProcessor()

    # Store some events
    events = []
    for i in range(3):
        event = processor.process_event({
            'source': f'192.168.1.{100+i}',
            'event_type': 'login',
            'severity': 'low',
            'details': {'user': f'user{i}'}
        })
        database.store_event(event)
        events.append(event)

    # Test querying
    all_events = database.query_events({})
    assert len(all_events) == 3

    login_events = database.query_events({'event_type': 'login'})
    assert len(login_events) == 3

    # Test aggregation
    aggregation = database.aggregate_events('event_type')
    assert aggregation.get('login', 0) == 3

    print("✓ SIEMDatabase works correctly")
    return True

def test_log_processing():
    """Test log line processing"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_33.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test auth log processing
    log_line = "sshd: Accepted publickey for user from 192.168.1.100 port 22"
    event = exercise.process_log_line(log_line, "192.168.1.100")

    assert event is not None
    assert event.event_type == 'login'
    assert event.severity == 'low'

    print("✓ Log processing works correctly")
    return True

def test_threat_analysis():
    """Test threat pattern analysis"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_33.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    processor = exercise.EventProcessor()

    # Create test events
    events = []
    for i in range(7):  # Multiple failed auths
        event = processor.process_event({
            'source': '192.168.1.100',
            'event_type': 'authentication',
            'severity': 'medium',
            'details': {'result': 'failure', 'user': 'admin'}
        })
        events.append(event)

    # Analyze patterns
    analysis = exercise.analyze_threat_patterns(events)

    assert analysis['total_events'] == 7
    assert 'threat_indicators' in analysis
    assert len(analysis['threat_indicators']) > 0  # Should detect high failed attempts

    print("✓ Threat analysis works correctly")
    return True

def test_incident_reporting():
    """Test incident report generation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_33.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Create a test alert
    processor = exercise.EventProcessor()
    event = processor.process_event({
        'source': '192.168.1.100',
        'event_type': 'authentication',
        'severity': 'high',
        'details': {'result': 'failure'}
    })

    alert = exercise.Alert(
        id=1,
        rule_id="test_rule",
        events=[event],
        severity="high",
        message="Test alert",
        created_at="2024-01-01T12:00:00Z"
    )

    # Generate report
    report = exercise.generate_incident_report(alert, [event])

    assert 'alert_summary' in report
    assert 'timeline' in report
    assert 'affected_systems' in report
    assert 'recommended_actions' in report

    assert report['alert_summary']['alert_id'] == 1
    assert len(report['timeline']) > 0

    print("✓ Incident reporting works correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 33 - SIEM Event Processing & Alerting\n")

    tests = [
        test_event_processor,
        test_alert_engine,
        test_siem_database,
        test_log_processing,
        test_threat_analysis,
        test_incident_reporting
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
        print("🎉 All tests passed! You're ready for Defensive Project 33!")
        print("You've mastered SIEM event processing, alerting, and threat analysis!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
