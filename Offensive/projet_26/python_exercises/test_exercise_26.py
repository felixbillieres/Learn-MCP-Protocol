"""
Test script for Python Exercise 26
Tests network port scanning and analysis
"""

import sys
import time
import importlib.util

def test_port_scanner():
    """Test the PortScanner functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_26.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    scanner = exercise.PortScanner(timeout=0.1)  # Short timeout for testing

    # Test port scanning (using localhost)
    port_info = scanner.scan_port("127.0.0.1", 80)  # Usually closed on localhost
    assert isinstance(port_info, exercise.PortInfo)
    assert port_info.port == 80
    assert port_info.state in [exercise.PortState.OPEN, exercise.PortState.CLOSED, exercise.PortState.FILTERED]

    print("✓ PortScanner basic functionality works")
    return True

def test_service_identification():
    """Test service identification"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_26.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    scanner = exercise.PortScanner()

    # Test known ports
    assert scanner._identify_service(22) in ["SSH", "OpenSSH", "PuTTY"]
    assert scanner._identify_service(80) in ["HTTP", "Apache", "nginx", "IIS"]
    assert scanner._identify_service(3306) in ["MySQL", "MariaDB"]

    # Test unknown port
    assert scanner._identify_service(9999) is None

    print("✓ Service identification works")
    return True

def test_scan_result():
    """Test scan result creation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_26.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Create a mock scan result
    ports = [
        exercise.PortInfo(22, exercise.PortState.OPEN, "SSH"),
        exercise.PortInfo(80, exercise.PortState.CLOSED),
        exercise.PortInfo(443, exercise.PortState.FILTERED)
    ]

    scan_result = exercise.ScanResult(
        target="example.com",
        ports=ports,
        timestamp="2024-01-01T12:00:00Z",
        scan_type=exercise.ScanType.QUICK,
        duration=1.5,
        scan_id=1234
    )

    assert scan_result.target == "example.com"
    assert len(scan_result.ports) == 3
    assert scan_result.scan_type == exercise.ScanType.QUICK

    print("✓ ScanResult structure works")
    return True

def test_service_analyzer():
    """Test service analysis functionality"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_26.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    analyzer = exercise.ServiceAnalyzer()

    # Test analysis of open port with service
    port_info = exercise.PortInfo(80, exercise.PortState.OPEN, "Apache", "2.4.41")
    analysis = analyzer.analyze_service(port_info)

    assert analysis["status"] == "analyzed"
    assert analysis["service"] == "Apache"
    assert "vulnerabilities" in analysis
    assert "recommendations" in analysis

    # Test analysis of closed port
    closed_port = exercise.PortInfo(9999, exercise.PortState.CLOSED)
    closed_analysis = analyzer.analyze_service(closed_port)
    assert closed_analysis["status"] == "no_service"

    print("✓ ServiceAnalyzer works correctly")
    return True

def test_report_generation():
    """Test security report generation"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_26.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Create mock scan result
    ports = [
        exercise.PortInfo(22, exercise.PortState.OPEN, "OpenSSH", "8.2p1"),
        exercise.PortInfo(80, exercise.PortState.OPEN, "Apache", "2.4.41"),
        exercise.PortInfo(443, exercise.PortState.CLOSED)
    ]

    scan_result = exercise.ScanResult(
        target="vulnerable.example.com",
        ports=ports,
        timestamp="2024-01-01T12:00:00Z",
        scan_type=exercise.ScanType.FULL,
        duration=2.5,
        scan_id=5678
    )

    analyzer = exercise.ServiceAnalyzer()
    report = exercise.generate_scan_report(scan_result, analyzer)

    # Verify report structure
    assert "scan_summary" in report
    assert "port_summary" in report
    assert "services_detected" in report
    assert "vulnerabilities_found" in report
    assert "security_recommendations" in report

    # Verify content
    assert report["scan_summary"]["target"] == "vulnerable.example.com"
    assert report["port_summary"]["open_ports"] == 2
    assert len(report["services_detected"]) == 2

    print("✓ Report generation works correctly")
    return True

def test_network_scanning():
    """Test network range scanning"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_26.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    # Test network scanning (will use simulation)
    results = exercise.scan_network_range("192.168.1.0/24", [80, 443])

    assert isinstance(results, list)
    if results:  # May be empty if network scanning fails
        assert isinstance(results[0], exercise.ScanResult)
        assert results[0].scan_type == exercise.ScanType.QUICK

    print("✓ Network scanning works correctly")
    return True

def test_scan_performance():
    """Test scanning performance and types"""
    spec = importlib.util.spec_from_file_location("exercise", "exercise_26.py")
    exercise = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(exercise)
    except Exception as e:
        print(f"Error loading exercise: {e}")
        return False

    scanner = exercise.PortScanner(timeout=0.05)  # Very short timeout

    # Test different scan types
    quick_result = scanner.scan_range("127.0.0.1", [22, 80, 443], exercise.ScanType.QUICK)
    assert quick_result.scan_type == exercise.ScanType.QUICK

    # Quick scan should scan fewer ports (simulation)
    ports_scanned = len(quick_result.ports)
    assert ports_scanned <= 20  # Limited for quick scan

    print("✓ Scan performance and types work correctly")
    return True

if __name__ == "__main__":
    print("Testing Python Exercise 26 - Network Port Scanning & Analysis\n")

    tests = [
        test_port_scanner,
        test_service_identification,
        test_scan_result,
        test_service_analyzer,
        test_report_generation,
        test_network_scanning,
        test_scan_performance
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
        print("🎉 All tests passed! You're ready for Offensive Project 26!")
        print("You've mastered port scanning, service identification, and vulnerability analysis!")
    else:
        print("❌ Some tests failed. Review your code and try again!")
        sys.exit(1)
