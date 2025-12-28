# Exercise 26: Network Port Scanning & Analysis
# Before creating MCP port scanners, let's practice network scanning concepts and service analysis

import socket
import random
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

class PortState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    FILTERED = "filtered"

class ScanType(Enum):
    QUICK = "quick"
    FULL = "full"
    STEALTH = "stealth"

@dataclass
class PortInfo:
    """Information about a scanned port"""
    port: int
    state: PortState
    service: Optional[str] = None
    version: Optional[str] = None
    banner: Optional[str] = None

@dataclass
class ScanResult:
    """Complete scan result"""
    target: str
    ports: List[PortInfo]
    timestamp: str
    scan_type: ScanType
    duration: float
    scan_id: int

# TODO: Create a class called 'PortScanner'
# - __init__: takes timeout, max_workers
# - scan_port: scans a single port using socket connection
# - scan_range: scans multiple ports concurrently
# - identify_service: attempts to identify service running on port
# - simulate_scan: creates realistic simulated scan results

# TODO: Create a class called 'ServiceAnalyzer'
# - __init__: loads service signatures database
# - analyze_service: analyzes detected service for vulnerabilities
# - get_service_info: returns detailed service information
# - check_common_vulnerabilities: checks for known vulnerabilities

# TODO: Create a function called 'generate_scan_report'
# Parameters: scan_result (ScanResult), analyzer (ServiceAnalyzer)
# Generates a comprehensive security report
# Includes open ports, services, potential vulnerabilities

# TODO: Create a function called 'perform_target_analysis'
# Parameters: target (str), scan_type (ScanType)
# Performs complete analysis of target
# Returns ScanResult with full analysis

# TODO: Create a function called 'scan_network_range'
# Parameters: network (str like "192.168.1.0/24"), ports (List[int])
# Scans multiple targets in a network range
# Returns list of ScanResult

class PortScanner:
    """Network port scanner implementation"""

    def __init__(self, timeout: float = 1.0, max_workers: int = 10):
        self.timeout = timeout
        self.max_workers = max_workers

        # Common service signatures
        self.service_signatures = {
            22: ["SSH", "OpenSSH", "PuTTY"],
            80: ["HTTP", "Apache", "nginx", "IIS"],
            443: ["HTTPS", "SSL/TLS"],
            3306: ["MySQL", "MariaDB"],
            5432: ["PostgreSQL"],
            8080: ["HTTP Proxy", "Tomcat", "Jetty"],
            21: ["FTP", "vsftpd", "FileZilla"],
            25: ["SMTP", "Postfix", "Sendmail"],
            53: ["DNS", "BIND", "PowerDNS"]
        }

    def scan_port(self, target: str, port: int) -> PortInfo:
        """Scan a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((target, port))
            sock.close()

            if result == 0:
                # Port is open
                service = self._identify_service(port)
                version = self._get_service_version(service)
                return PortInfo(port=port, state=PortState.OPEN, service=service, version=version)
            else:
                # Port is closed or filtered
                state = PortState.CLOSED if result == 111 else PortState.FILTERED
                return PortInfo(port=port, state=state)

        except (socket.timeout, socket.error):
            return PortInfo(port=port, state=PortState.FILTERED)

    def _identify_service(self, port: int) -> Optional[str]:
        """Identify service based on port number"""
        if port in self.service_signatures:
            return random.choice(self.service_signatures[port])
        return None

    def _get_service_version(self, service: Optional[str]) -> Optional[str]:
        """Get a simulated version for the service"""
        if not service:
            return None

        versions = {
            "Apache": ["2.4.41", "2.4.52", "2.4.54"],
            "nginx": ["1.18.0", "1.20.1", "1.22.1"],
            "OpenSSH": ["8.2p1", "8.9p1", "9.0p1"],
            "MySQL": ["8.0.30", "8.0.32", "8.0.33"],
            "PostgreSQL": ["13.7", "14.3", "15.1"]
        }

        if service in versions:
            return random.choice(versions[service])

        # Generic version for unknown services
        return f"1.{random.randint(0, 9)}.{random.randint(0, 99)}"

    def scan_range(self, target: str, ports: List[int], scan_type: ScanType = ScanType.QUICK) -> ScanResult:
        """Scan multiple ports"""
        start_time = time.time()

        # Adjust ports based on scan type
        if scan_type == ScanType.QUICK:
            ports = ports[:20]  # Limit to first 20 ports
        elif scan_type == ScanType.STEALTH:
            time.sleep(0.1)  # Add delay for stealth

        scanned_ports = []
        for port in ports:
            port_info = self.scan_port(target, port)
            scanned_ports.append(port_info)

            # Small delay between scans for politeness
            time.sleep(0.01)

        duration = time.time() - start_time

        return ScanResult(
            target=target,
            ports=scanned_ports,
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            scan_type=scan_type,
            duration=duration,
            scan_id=random.randint(1000, 9999)
        )

class ServiceAnalyzer:
    """Service analysis and vulnerability detection"""

    def __init__(self):
        self.vulnerabilities = {
            "Apache 2.4.41": ["CVE-2021-41773", "CVE-2021-42013"],
            "Apache 2.4.52": ["CVE-2022-31813"],
            "nginx 1.18.0": ["CVE-2020-11724"],
            "OpenSSH 8.2p1": ["CVE-2021-28041"],
            "MySQL 8.0.30": ["CVE-2022-21594"]
        }

    def analyze_service(self, port_info: PortInfo) -> Dict[str, Any]:
        """Analyze a service for information and vulnerabilities"""
        if not port_info.service or port_info.state != PortState.OPEN:
            return {"status": "no_service", "vulnerabilities": []}

        analysis = {
            "port": port_info.port,
            "service": port_info.service,
            "version": port_info.version,
            "status": "analyzed",
            "vulnerabilities": [],
            "recommendations": []
        }

        # Check for known vulnerabilities
        service_key = f"{port_info.service} {port_info.version}" if port_info.version else port_info.service
        if service_key in self.vulnerabilities:
            analysis["vulnerabilities"] = self.vulnerabilities[service_key]
            analysis["recommendations"].append("Update to latest version")

        # Add general recommendations
        if port_info.port in [22, 80, 443]:
            analysis["recommendations"].append("Consider using key-based authentication")
        if port_info.port == 21:
            analysis["recommendations"].append("FTP is insecure, consider SFTP")

        return analysis

    def get_service_info(self, service_name: str) -> Dict[str, Any]:
        """Get detailed information about a service"""
        service_db = {
            "SSH": {
                "description": "Secure Shell protocol for remote access",
                "default_ports": [22],
                "security_notes": "Use key-based authentication, disable root login"
            },
            "HTTP": {
                "description": "HyperText Transfer Protocol for web content",
                "default_ports": [80],
                "security_notes": "Use HTTPS, keep software updated"
            },
            "HTTPS": {
                "description": "Secure HTTP with SSL/TLS encryption",
                "default_ports": [443],
                "security_notes": "Use strong certificates, enable HSTS"
            },
            "MySQL": {
                "description": "Popular relational database",
                "default_ports": [3306],
                "security_notes": "Use strong passwords, restrict network access"
            }
        }

        return service_db.get(service_name, {
            "description": "Unknown service",
            "default_ports": [],
            "security_notes": "Research this service for security best practices"
        })

def generate_scan_report(scan_result: ScanResult, analyzer: ServiceAnalyzer) -> Dict[str, Any]:
    """Generate a comprehensive security scan report"""
    report = {
        "scan_summary": {
            "target": scan_result.target,
            "scan_type": scan_result.scan_type.value,
            "duration": f"{scan_result.duration:.2f}s",
            "timestamp": scan_result.timestamp,
            "scan_id": scan_result.scan_id
        },
        "port_summary": {
            "total_ports_scanned": len(scan_result.ports),
            "open_ports": len([p for p in scan_result.ports if p.state == PortState.OPEN]),
            "closed_ports": len([p for p in scan_result.ports if p.state == PortState.CLOSED]),
            "filtered_ports": len([p for p in scan_result.ports if p.state == PortState.FILTERED])
        },
        "services_detected": [],
        "vulnerabilities_found": [],
        "security_recommendations": []
    }

    # Analyze each open port
    for port_info in scan_result.ports:
        if port_info.state == PortState.OPEN:
            service_analysis = analyzer.analyze_service(port_info)

            service_info = {
                "port": port_info.port,
                "service": port_info.service or "unknown",
                "version": port_info.version,
                "analysis": service_analysis
            }
            report["services_detected"].append(service_info)

            # Collect vulnerabilities
            if service_analysis["vulnerabilities"]:
                report["vulnerabilities_found"].extend(service_analysis["vulnerabilities"])

            # Collect recommendations
            report["security_recommendations"].extend(service_analysis["recommendations"])

    # Remove duplicates
    report["vulnerabilities_found"] = list(set(report["vulnerabilities_found"]))
    report["security_recommendations"] = list(set(report["security_recommendations"]))

    return report

def perform_target_analysis(target: str, scan_type: ScanType = ScanType.QUICK) -> ScanResult:
    """Perform complete target analysis"""
    scanner = PortScanner()

    # Define port ranges based on scan type
    if scan_type == ScanType.QUICK:
        ports = [22, 80, 443, 3306, 5432, 8080]  # Common ports
    elif scan_type == ScanType.FULL:
        ports = list(range(1, 1025))  # First 1024 ports
    else:  # STEALTH
        ports = [22, 80, 443, 21, 25, 53]  # Essential services

    return scanner.scan_range(target, ports, scan_type)

def scan_network_range(network: str, ports: List[int]) -> List[ScanResult]:
    """Scan multiple targets in a network range"""
    # Simple implementation - just scan a few IPs
    # In reality, you'd parse CIDR notation and scan all IPs

    if "/24" in network:
        base_ip = network.replace("/24", "")
        # Simulate scanning .1 to .10
        targets = [f"{base_ip}.{i}" for i in range(1, 11)]
    else:
        targets = [network]  # Single target

    results = []
    for target in targets:
        try:
            result = perform_target_analysis(target, ScanType.QUICK)
            results.append(result)
        except Exception as e:
            print(f"Failed to scan {target}: {e}")

    return results

def main():
    """Demonstrate port scanning and analysis"""
    try:
        print("=== Network Port Scanning & Analysis Exercise ===\n")

        # Create scanner and analyzer
        scanner = PortScanner()
        analyzer = ServiceAnalyzer()

        # Test single port scan
        print("1. Single Port Scan:")
        port_info = scanner.scan_port("scanme.nmap.org", 80)
        print(f"Port 80: {port_info.state.value}")
        if port_info.service:
            print(f"Service: {port_info.service} {port_info.version or ''}")

        # Test range scan
        print("\n2. Port Range Scan:")
        scan_result = scanner.scan_range("scanme.nmap.org", [22, 80, 443, 3306], ScanType.QUICK)
        print(f"Scanned {len(scan_result.ports)} ports in {scan_result.duration:.2f}s")
        open_ports = [p for p in scan_result.ports if p.state == PortState.OPEN]
        print(f"Open ports: {[p.port for p in open_ports]}")

        # Test service analysis
        print("\n3. Service Analysis:")
        for port_info in open_ports[:2]:  # Analyze first 2 open ports
            analysis = analyzer.analyze_service(port_info)
            print(f"Port {port_info.port}: {analysis['status']}")
            if analysis['vulnerabilities']:
                print(f"  Vulnerabilities: {analysis['vulnerabilities']}")

        # Generate report
        print("\n4. Security Report Generation:")
        report = generate_scan_report(scan_result, analyzer)
        print(f"Report for {report['scan_summary']['target']}:")
        print(f"  Open ports: {report['port_summary']['open_ports']}")
        print(f"  Services detected: {len(report['services_detected'])}")
        if report['vulnerabilities_found']:
            print(f"  Vulnerabilities: {report['vulnerabilities_found']}")

        print("\n✅ Network scanning and analysis demonstration completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
