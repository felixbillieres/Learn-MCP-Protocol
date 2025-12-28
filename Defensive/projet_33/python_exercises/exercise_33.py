# Exercise 33: SIEM Event Processing & Alerting
# Before creating SIEM MCP servers, let's practice security event processing and correlation

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import json
import re

@dataclass
class SecurityEvent:
    """Security event data structure"""
    id: int
    timestamp: str
    source: str
    event_type: str
    severity: str
    details: Dict[str, Any]

@dataclass
class Alert:
    """Security alert data structure"""
    id: int
    rule_id: str
    events: List[SecurityEvent]
    severity: str
    message: str
    created_at: str

@dataclass
class DetectionRule:
    """Detection rule for security events"""
    id: str
    name: str
    pattern: str
    severity: str
    enabled: bool = True

# TODO: Create a class called 'EventProcessor'
# - process_event: validates and enriches security events
# - normalize_event: standardizes event format
# - enrich_event: adds contextual information
# - validate_event: ensures event data integrity

# TODO: Create a class called 'AlertEngine'
# - __init__: loads detection rules
# - evaluate_rules: checks events against all rules
# - generate_alert: creates alert from triggered rule
# - correlate_events: finds related events for alerts
# - suppress_duplicates: prevents duplicate alerts

# TODO: Create a class called 'SIEMDatabase'
# - store_event: saves events with indexing
# - query_events: searches events by various criteria
# - get_recent_events: retrieves events from time window
# - aggregate_events: groups events by type/source
# - cleanup_old_events: removes events older than threshold

# TODO: Create a function called 'process_log_line'
# Parameters: log_line (str), source (str)
# Parses various log formats and creates SecurityEvent
# Supports syslog, apache logs, auth logs, etc.

# TODO: Create a function called 'analyze_threat_patterns'
# Parameters: events (List[SecurityEvent])
# Analyzes event patterns for threat detection
# Returns threat intelligence summary

# TODO: Create a function called 'generate_incident_report'
# Parameters: alert (Alert), related_events (List[SecurityEvent])
# Creates detailed incident report with timeline and analysis

class EventProcessor:
    """Processes and enriches security events"""

    def __init__(self):
        self.event_counter = 1
        # Normalization patterns
        self.field_mappings = {
            'ip': ['client_ip', 'src_ip', 'source_ip'],
            'user': ['username', 'user_id', 'account'],
            'action': ['operation', 'method', 'command']
        }

    def process_event(self, raw_event: Dict[str, Any]) -> SecurityEvent:
        """Process a raw security event"""
        # Validate required fields
        if not all(key in raw_event for key in ['source', 'event_type']):
            raise ValueError("Missing required event fields")

        # Normalize and enrich
        normalized = self.normalize_event(raw_event)
        enriched = self.enrich_event(normalized)

        event = SecurityEvent(
            id=self.event_counter,
            timestamp=enriched.get('timestamp', datetime.now().isoformat()),
            source=enriched['source'],
            event_type=enriched['event_type'],
            severity=enriched.get('severity', 'low'),
            details=enriched.get('details', {})
        )

        self.event_counter += 1
        return event

    def normalize_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize event field names and values"""
        normalized = event.copy()

        # Normalize severity levels
        severity_map = {
            'LOW': 'low', 'MEDIUM': 'medium', 'HIGH': 'high', 'CRITICAL': 'critical',
            '1': 'low', '2': 'medium', '3': 'high', '4': 'critical'
        }
        if 'severity' in normalized:
            normalized['severity'] = severity_map.get(normalized['severity'].upper(), normalized['severity'].lower())

        # Normalize event types
        type_map = {
            'LOGIN': 'login', 'LOGOUT': 'logout', 'ACCESS': 'file_access',
            'NETWORK': 'network', 'PROCESS': 'process', 'AUTH': 'authentication'
        }
        if 'event_type' in normalized:
            normalized['event_type'] = type_map.get(normalized['event_type'].upper(), normalized['event_type'].lower())

        return normalized

    def enrich_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Add contextual information to event"""
        enriched = event.copy()

        # Add timestamp if missing
        if 'timestamp' not in enriched:
            enriched['timestamp'] = datetime.now().isoformat()

        # Extract IP information
        if 'source' in enriched:
            source = enriched['source']
            if self._is_ip_address(source):
                enriched['details'] = enriched.get('details', {})
                enriched['details']['ip_type'] = self._classify_ip(source)

        # Add risk scoring
        enriched['risk_score'] = self._calculate_risk_score(enriched)

        return enriched

    def _is_ip_address(self, string: str) -> bool:
        """Check if string is an IP address"""
        import ipaddress
        try:
            ipaddress.ip_address(string)
            return True
        except ValueError:
            return False

    def _classify_ip(self, ip: str) -> str:
        """Classify IP address type"""
        if ip.startswith(('10.', '192.168.', '172.')):
            return 'private'
        elif ip.startswith('127.'):
            return 'localhost'
        else:
            return 'public'

    def _calculate_risk_score(self, event: Dict[str, Any]) -> int:
        """Calculate risk score for event (0-100)"""
        score = 0

        # Severity contribution
        severity_scores = {'low': 10, 'medium': 30, 'high': 60, 'critical': 100}
        score += severity_scores.get(event.get('severity', 'low'), 10)

        # Event type contribution
        risky_types = ['authentication', 'file_access', 'network']
        if event.get('event_type') in risky_types:
            score += 20

        # Source contribution
        if event.get('details', {}).get('ip_type') == 'public':
            score += 15

        return min(100, score)

class AlertEngine:
    """Engine for detecting and generating security alerts"""

    def __init__(self):
        self.rules = []
        self.alert_counter = 1

    def add_rule(self, rule: DetectionRule):
        """Add a detection rule"""
        self.rules.append(rule)

    def evaluate_rules(self, event: SecurityEvent) -> List[Alert]:
        """Evaluate event against all rules and return triggered alerts"""
        alerts = []

        for rule in self.rules:
            if not rule.enabled:
                continue

            if self._matches_rule(event, rule):
                alert = self.generate_alert(rule, [event])
                alerts.append(alert)

        return alerts

    def _matches_rule(self, event: SecurityEvent, rule: DetectionRule) -> bool:
        """Check if event matches detection rule"""
        pattern = rule.pattern.lower()
        event_text = json.dumps({
            'type': event.event_type,
            'source': event.source,
            'severity': event.severity,
            'details': event.details
        }).lower()

        # Simple pattern matching
        return pattern in event_text

    def generate_alert(self, rule: DetectionRule, events: List[SecurityEvent]) -> Alert:
        """Generate alert from triggered rule"""
        alert = Alert(
            id=self.alert_counter,
            rule_id=rule.id,
            events=events,
            severity=rule.severity,
            message=f"Alert triggered by rule '{rule.name}': {rule.pattern}",
            created_at=datetime.now().isoformat()
        )

        self.alert_counter += 1
        return alert

    def correlate_events(self, events: List[SecurityEvent], time_window: int = 300) -> List[List[SecurityEvent]]:
        """Correlate related events within time window"""
        correlated_groups = []
        processed = set()

        for i, event in enumerate(events):
            if i in processed:
                continue

            group = [event]
            processed.add(i)

            # Find related events within time window
            event_time = datetime.fromisoformat(event.timestamp.replace('Z', '+00:00'))

            for j, other_event in enumerate(events):
                if j in processed or j == i:
                    continue

                other_time = datetime.fromisoformat(other_event.timestamp.replace('Z', '+00:00'))
                time_diff = abs((event_time - other_time).total_seconds())

                if time_diff <= time_window and self._are_related(event, other_event):
                    group.append(other_event)
                    processed.add(j)

            if len(group) > 1:  # Only include correlated groups
                correlated_groups.append(group)

        return correlated_groups

    def _are_related(self, event1: SecurityEvent, event2: SecurityEvent) -> bool:
        """Check if two events are related"""
        # Same source IP
        if event1.source == event2.source:
            return True

        # Same user in details
        user1 = event1.details.get('user')
        user2 = event2.details.get('user')
        if user1 and user2 and user1 == user2:
            return True

        # Failed login followed by successful login from same IP
        if (event1.event_type == 'authentication' and
            event2.event_type == 'authentication' and
            event1.source == event2.source):
            return True

        return False

class SIEMDatabase:
    """Database for storing and querying security events"""

    def __init__(self):
        self.events: List[SecurityEvent] = []
        self.max_events = 10000  # Limit for memory

    def store_event(self, event: SecurityEvent):
        """Store event with indexing"""
        self.events.append(event)

        # Maintain size limit
        if len(self.events) > self.max_events:
            self.events.pop(0)

    def query_events(self, filters: Dict[str, Any]) -> List[SecurityEvent]:
        """Query events with filters"""
        results = self.events.copy()

        for key, value in filters.items():
            if key == 'event_type':
                results = [e for e in results if e.event_type == value]
            elif key == 'source':
                results = [e for e in results if e.source == value]
            elif key == 'severity':
                results = [e for e in results if e.severity == value]
            elif key == 'time_after':
                results = [e for e in results if e.timestamp >= value]
            elif key == 'time_before':
                results = [e for e in results if e.timestamp <= value]

        return results

    def get_recent_events(self, minutes: int = 60) -> List[SecurityEvent]:
        """Get events from the last N minutes"""
        cutoff_time = datetime.now() - timedelta(minutes=minutes)
        cutoff_str = cutoff_time.isoformat()

        return [e for e in self.events if e.timestamp >= cutoff_str]

    def aggregate_events(self, group_by: str = 'event_type') -> Dict[str, int]:
        """Aggregate events by specified field"""
        aggregation = {}

        for event in self.events:
            key = getattr(event, group_by, 'unknown')
            aggregation[key] = aggregation.get(key, 0) + 1

        return aggregation

def process_log_line(log_line: str, source: str) -> Optional[SecurityEvent]:
    """Process various log formats into security events"""
    processor = EventProcessor()

    # Try different log formats
    event_data = None

    # Syslog format: timestamp hostname process[pid]: message
    syslog_pattern = r'(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+)\s+(\S+)\[(\d+)\]:\s+(.+)'
    match = re.match(syslog_pattern, log_line)
    if match:
        timestamp, hostname, process, pid, message = match.groups()
        event_data = {
            'source': hostname,
            'event_type': 'system',
            'details': {'process': process, 'pid': pid, 'message': message}
        }

    # Apache access log format
    apache_pattern = r'(\S+)\s+\-\s+(\S+)\s+\[([^\]]+)\]\s+"([^"]+)"\s+(\d+)\s+(\d+)'
    match = re.match(apache_pattern, log_line)
    if match:
        ip, user, timestamp, request, status, size = match.groups()
        event_data = {
            'source': ip,
            'event_type': 'web_access',
            'details': {'user': user, 'request': request, 'status': status, 'size': size}
        }

    # Auth log format
    if 'sshd' in log_line and ('Accepted' in log_line or 'Failed' in log_line):
        if 'Accepted' in log_line:
            event_data = {
                'source': source,
                'event_type': 'login',
                'severity': 'low',
                'details': {'result': 'success', 'service': 'ssh'}
            }
        else:
            event_data = {
                'source': source,
                'event_type': 'authentication',
                'severity': 'medium',
                'details': {'result': 'failure', 'service': 'ssh'}
            }

    if event_data:
        return processor.process_event(event_data)

    return None

def analyze_threat_patterns(events: List[SecurityEvent]) -> Dict[str, Any]:
    """Analyze events for threat patterns"""
    analysis = {
        'total_events': len(events),
        'severity_distribution': {},
        'top_sources': {},
        'threat_indicators': [],
        'recommendations': []
    }

    # Severity distribution
    for event in events:
        analysis['severity_distribution'][event.severity] = \
            analysis['severity_distribution'].get(event.severity, 0) + 1

    # Top sources
    for event in events:
        analysis['top_sources'][event.source] = \
            analysis['top_sources'].get(event.source, 0) + 1

    # Threat indicators
    failed_auths = sum(1 for e in events if e.event_type == 'authentication' and
                      e.details.get('result') == 'failure')
    if failed_auths > 5:
        analysis['threat_indicators'].append(f"High failed authentication attempts: {failed_auths}")

    unusual_ips = [e.source for e in events if e.details.get('ip_type') == 'public']
    if len(set(unusual_ips)) > 3:
        analysis['threat_indicators'].append("Multiple external IPs accessing system")

    # Recommendations
    if analysis['severity_distribution'].get('high', 0) > 0:
        analysis['recommendations'].append("Investigate high-severity events immediately")

    if failed_auths > 0:
        analysis['recommendations'].append("Review authentication policies and brute-force protection")

    return analysis

def generate_incident_report(alert: Alert, related_events: List[SecurityEvent]) -> Dict[str, Any]:
    """Generate detailed incident report"""
    report = {
        'alert_summary': {
            'alert_id': alert.id,
            'rule_id': alert.rule_id,
            'severity': alert.severity,
            'message': alert.message,
            'created_at': alert.created_at
        },
        'timeline': [],
        'affected_systems': set(),
        'recommended_actions': []
    }

    # Build timeline
    all_events = alert.events + related_events
    sorted_events = sorted(all_events, key=lambda e: e.timestamp)

    for event in sorted_events:
        report['timeline'].append({
            'timestamp': event.timestamp,
            'event_type': event.event_type,
            'source': event.source,
            'severity': event.severity,
            'details': event.details
        })
        report['affected_systems'].add(event.source)

    report['affected_systems'] = list(report['affected_systems'])

    # Recommended actions based on alert type
    if 'authentication' in alert.message.lower():
        report['recommended_actions'].extend([
            "Enable multi-factor authentication",
            "Implement account lockout policies",
            "Review recent password changes"
        ])
    elif 'network' in alert.message.lower():
        report['recommended_actions'].extend([
            "Review firewall rules",
            "Check network segmentation",
            "Monitor for unusual traffic patterns"
        ])

    return report

def main():
    """Demonstrate SIEM event processing and alerting"""
    try:
        print("=== SIEM Event Processing & Alerting Exercise ===\n")

        # Setup components
        processor = EventProcessor()
        alert_engine = AlertEngine()
        database = SIEMDatabase()

        # Add detection rules
        rules = [
            DetectionRule("auth_failures", "Multiple Authentication Failures",
                          "authentication.*failure", "medium"),
            DetectionRule("high_risk_login", "High Risk Login",
                          "login.*public", "high"),
            DetectionRule("suspicious_network", "Suspicious Network Activity",
                          "network.*unusual", "medium")
        ]

        for rule in rules:
            alert_engine.add_rule(rule)

        # Process sample events
        print("Processing security events...")

        sample_events_data = [
            {
                'source': '192.168.1.100',
                'event_type': 'authentication',
                'severity': 'medium',
                'details': {'result': 'failure', 'service': 'ssh', 'user': 'admin'}
            },
            {
                'source': '192.168.1.100',
                'event_type': 'login',
                'severity': 'low',
                'details': {'result': 'success', 'service': 'ssh', 'user': 'admin'}
            },
            {
                'source': '10.0.0.50',
                'event_type': 'network',
                'severity': 'high',
                'details': {'action': 'unusual_traffic', 'bytes': 1000000}
            }
        ]

        processed_events = []
        for event_data in sample_events_data:
            event = processor.process_event(event_data)
            processed_events.append(event)
            database.store_event(event)

            # Check for alerts
            alerts = alert_engine.evaluate_rules(event)
            for alert in alerts:
                print(f"🚨 Alert triggered: {alert.message}")

        # Analyze threat patterns
        print("\\nThreat Analysis:")
        analysis = analyze_threat_patterns(processed_events)
        print(f"Total events: {analysis['total_events']}")
        print(f"Severity distribution: {analysis['severity_distribution']}")
        if analysis['threat_indicators']:
            print(f"Threat indicators: {analysis['threat_indicators']}")

        # Generate incident report for first alert
        alerts = []  # In real implementation, collect from alert engine
        if alerts:
            report = generate_incident_report(alerts[0], processed_events)
            print(f"\\nIncident report generated for alert {report['alert_summary']['alert_id']}")
            print(f"Affected systems: {report['affected_systems']}")
            print(f"Recommended actions: {report['recommended_actions']}")

        # Database queries
        print("\\nDatabase Queries:")
        recent_events = database.get_recent_events(60)
        print(f"Recent events (60min): {len(recent_events)}")

        auth_events = database.query_events({'event_type': 'authentication'})
        print(f"Authentication events: {len(auth_events)}")

        aggregation = database.aggregate_events('event_type')
        print(f"Events by type: {aggregation}")

        print("\\n✅ SIEM event processing and alerting demonstration completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
