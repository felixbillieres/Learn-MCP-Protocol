# Project 29 : Pentest Session Manager

## Objective

Create an MCP server to manage exploitation sessions (SSH, WinRM, PsExec, etc.) with real-time notifications.

## Concepts to Learn

### Session Management in Pentesting

During a pentest, you establish multiple sessions:
- **SSH sessions** : Remote shell access
- **WinRM sessions** : Windows Remote Management
- **PsExec sessions** : Windows remote execution
- **Web shells** : Web-based command execution

### MCP Architecture

- **Tools** : Create, list, and manage sessions
- **Resources** : Expose active sessions
- **Subscriptions** : Notify when new sessions are established
- **Authorization** : Protect session access

## Use Cases

- Track all active sessions during a pentest
- Get notified when new access is gained
- Manage credentials and session metadata
- Generate session reports

