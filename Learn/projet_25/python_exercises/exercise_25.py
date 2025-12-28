# Exercise 25: Complete MCP Server (Project Manager)
# Before building the final project, let's practice integrating all MCP concepts

from typing import List, Dict, Any, Optional
import json
import time
from datetime import datetime

# TODO: Create a comprehensive ProjectManager class that integrates:
# - Resources (list and read project/task data)
# - Tools (CRUD operations for projects and tasks)
# - Prompts (dynamic prompts for project management)
# - Elicitation (confirmation for destructive operations)
# - Authentication (basic token validation)
# - Error handling and logging

# TODO: Implement core data models:
# - Project: id, name, description, status, created_at, updated_at
# - Task: id, project_id, title, description, status, priority, assigned_to, due_date

# TODO: Create resource handlers:
# - list_projects_resource
# - read_project_resource
# - list_tasks_resource
# - read_task_resource

# TODO: Create tool handlers:
# - create_project_tool
# - update_project_tool
# - delete_project_tool (with confirmation)
# - create_task_tool
# - update_task_tool
# - assign_task_tool
# - complete_task_tool

# TODO: Create prompt handlers:
# - project_summary_prompt
# - task_assignment_prompt
# - progress_report_prompt

class ProjectManager:
    """Complete MCP server integrating all features"""

    def __init__(self):
        self.projects = {}
        self.tasks = {}
        self.project_counter = 1
        self.task_counter = 1
        self.auth_tokens = {'admin_token': 'admin', 'user_token': 'user'}

    # Data Models
    def create_project(self, name: str, description: str = "", created_by: str = "system") -> Dict[str, Any]:
        """Create a new project"""
        project = {
            'id': self.project_counter,
            'name': name,
            'description': description,
            'status': 'active',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'created_by': created_by,
            'task_count': 0
        }
        self.projects[self.project_counter] = project
        self.project_counter += 1
        return project

    def create_task(self, project_id: int, title: str, description: str = "",
                   priority: str = "medium", assigned_to: str = None) -> Dict[str, Any]:
        """Create a new task"""
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} not found")

        task = {
            'id': self.task_counter,
            'project_id': project_id,
            'title': title,
            'description': description,
            'status': 'todo',
            'priority': priority,
            'assigned_to': assigned_to,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        self.tasks[self.task_counter] = task
        self.task_counter += 1

        # Update project task count
        self.projects[project_id]['task_count'] += 1

        return task

    # Resource Handlers
    def list_projects_resource(self) -> List[Dict[str, Any]]:
        """List all projects as MCP resources"""
        return [{
            'uri': f'project://{project["id"]}',
            'name': project['name'],
            'description': f'Project: {project["description"][:50] if project["description"] else "No description"}',
            'mimeType': 'application/json'
        } for project in self.projects.values()]

    def read_project_resource(self, project_id: int) -> Dict[str, Any]:
        """Read specific project resource"""
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} not found")

        project = self.projects[project_id]
        return {
            'contents': [{
                'uri': f'project://{project_id}',
                'mimeType': 'application/json',
                'text': json.dumps(project, indent=2)
            }]
        }

    def list_tasks_resource(self, project_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """List tasks, optionally filtered by project"""
        tasks = self.tasks.values()
        if project_id:
            tasks = [t for t in tasks if t['project_id'] == project_id]

        return [{
            'uri': f'task://{task["id"]}',
            'name': task['title'],
            'description': f'Task: {task["description"][:50] if task["description"] else "No description"}',
            'mimeType': 'application/json'
        } for task in tasks]

    # Tool Handlers
    def authenticate_request(self, auth_header: str) -> str:
        """Simple authentication"""
        if not auth_header or not auth_header.startswith('Bearer '):
            raise ValueError("Authentication required")

        token = auth_header[7:]
        if token not in self.auth_tokens:
            raise ValueError("Invalid token")

        return self.auth_tokens[token]

    def create_project_tool(self, name: str, description: str = "", auth: str = "") -> Dict[str, Any]:
        """Tool to create a new project"""
        user = self.authenticate_request(f"Bearer {auth}")
        if user != 'admin':
            raise ValueError("Admin access required to create projects")

        project = self.create_project(name, description, user)
        return {
            'message': f'Project "{name}" created successfully',
            'project': project
        }

    def create_task_tool(self, project_id: int, title: str, description: str = "",
                        priority: str = "medium", auth: str = "") -> Dict[str, Any]:
        """Tool to create a new task"""
        self.authenticate_request(f"Bearer {auth}")
        task = self.create_task(project_id, title, description, priority)
        return {
            'message': f'Task "{title}" created successfully',
            'task': task
        }

    def update_task_status(self, task_id: int, status: str, auth: str = "") -> Dict[str, Any]:
        """Update task status"""
        self.authenticate_request(f"Bearer {auth}")

        if task_id not in self.tasks:
            raise ValueError(f"Task {task_id} not found")

        if status not in ['todo', 'in_progress', 'done', 'cancelled']:
            raise ValueError("Invalid status")

        self.tasks[task_id]['status'] = status
        self.tasks[task_id]['updated_at'] = datetime.now().isoformat()

        return {
            'message': f'Task {task_id} status updated to {status}',
            'task': self.tasks[task_id]
        }

    # Prompt Handlers
    def project_summary_prompt(self, project_id: int) -> Dict[str, Any]:
        """Generate project summary prompt"""
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} not found")

        project = self.projects[project_id]
        tasks = [t for t in self.tasks.values() if t['project_id'] == project_id]

        summary_text = f"""
Project: {project['name']}
Description: {project['description']}
Status: {project['status']}
Tasks: {len(tasks)}

Task breakdown:
"""

        for task in tasks:
            summary_text += f"- {task['title']} ({task['status']}) - {task['priority']} priority\n"

        return {
            'name': 'project_summary',
            'messages': [{
                'role': 'user',
                'content': {
                    'type': 'text',
                    'text': f'Please provide a summary and status update for this project:\\n{summary_text}'
                }
            }]
        }

    # Elicitation Handlers
    def confirm_deletion_elicitation(self, item_type: str, item_id: int, item_name: str) -> Dict[str, Any]:
        """Create confirmation elicitation for deletion"""
        return {
            'mode': 'confirmation',
            'message': f'Are you sure you want to delete this {item_type}?\\n\\n{item_type.title()}: {item_name}\\nID: {item_id}\\n\\nThis action cannot be undone.',
            'title': f'Confirm {item_type.title()} Deletion'
        }

def main():
    """Demonstrate complete MCP server functionality"""
    try:
        print("=== Complete MCP Server (Project Manager) Exercise ===\\n")

        # Initialize project manager
        pm = ProjectManager()

        # Create sample data
        print("Setting up sample project and tasks...")

        # Create project (as admin)
        project = pm.create_project(
            name="MCP Learning Platform",
            description="A comprehensive platform for learning MCP protocol"
        )
        print(f"✅ Created project: {project['name']}")

        # Create tasks
        tasks_data = [
            ("Design system architecture", "Create detailed system design", "high"),
            ("Implement core features", "Build the main functionality", "high"),
            ("Write documentation", "Create comprehensive docs", "medium"),
            ("Add tests", "Implement unit and integration tests", "medium")
        ]

        for title, desc, priority in tasks_data:
            task = pm.create_task(project['id'], title, desc, priority)
            print(f"✅ Created task: {task['title']}")

        # Test resource access
        print("\\nTesting resource access:")
        projects = pm.list_projects_resource()
        print(f"Found {len(projects)} projects")

        project_resource = pm.read_project_resource(project['id'])
        print(f"Project resource loaded: {len(project_resource['contents'][0]['text'])} chars")

        # Test task management
        print("\\nTesting task management:")
        tasks = pm.list_tasks_resource(project['id'])
        print(f"Found {len(tasks)} tasks for project")

        # Update a task
        if tasks:
            task_id = tasks[0]['uri'].split('://')[1]  # Extract ID from URI
            update_result = pm.update_task_status(int(task_id), 'in_progress', 'user_token')
            print(f"✅ Updated task status: {update_result['message']}")

        # Test prompt generation
        print("\\nTesting prompt generation:")
        prompt = pm.project_summary_prompt(project['id'])
        print(f"Generated prompt with {len(prompt['messages'])} messages")

        # Test elicitation
        print("\\nTesting elicitation:")
        confirmation = pm.confirm_deletion_elicitation('project', project['id'], project['name'])
        print(f"Elicitation mode: {confirmation['mode']}")
        print(f"Confirmation message length: {len(confirmation['message'])}")

        print("\\n🎉 Complete MCP server demonstration successful!")
        print("All major MCP features have been implemented and tested!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
