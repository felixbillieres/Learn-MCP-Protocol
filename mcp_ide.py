#!/usr/bin/env python3
"""
MCP Learning IDE - Interactive Terminal Interface
Navigate through MCP projects, view exercises, run tests, and track progress.
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.live import Live
from rich.spinner import Spinner
from rich.columns import Columns
from rich.align import Align
from rich.layout import Layout

console = Console()

class MCPLearningIDE:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.current_project: Optional[str] = None
        self.current_exercise: Optional[str] = None
        self.progress_file = self.base_path / ".mcp_progress.json"

        # Load progress
        self.completed_projects = self.load_progress()

    def load_progress(self) -> Dict[str, Dict[str, bool]]:
        """Load completion progress from file"""
        if self.progress_file.exists():
            import json
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}

    def save_progress(self):
        """Save completion progress to file"""
        import json
        with open(self.progress_file, 'w') as f:
            json.dump(self.completed_projects, f, indent=2)

    def mark_completed(self, project: str, exercise_type: str):
        """Mark an exercise as completed"""
        if project not in self.completed_projects:
            self.completed_projects[project] = {}
        self.completed_projects[project][exercise_type] = True
        self.save_progress()

    def is_completed(self, project: str, exercise_type: str) -> bool:
        """Check if an exercise is completed"""
        return self.completed_projects.get(project, {}).get(exercise_type, False)

    def get_projects(self) -> List[str]:
        """Get all available MCP projects"""
        projects = []
        for i in range(1, 41):  # Projects 01-40
            proj_name = f"projet_{i:02d}"
            proj_path = self.base_path / "Learn" / proj_name
            if proj_path.exists():
                projects.append(proj_name)

        # Add Offensive and Defensive projects
        for category in ["Offensive", "Defensive"]:
            cat_path = self.base_path / category
            if cat_path.exists():
                for proj_path in sorted(cat_path.glob("projet_*")):
                    projects.append(f"{category.lower()}/{proj_path.name}")

        return projects

    def get_project_info(self, project: str) -> Dict:
        """Get information about a specific project"""
        if "/" in project:
            category, proj_name = project.split("/")
            proj_path = self.base_path / category.capitalize() / proj_name
        else:
            proj_path = self.base_path / "Learn" / project

        info = {
            "path": proj_path,
            "name": project,
            "has_mcp": False,
            "has_python_exercises": False,
            "mcp_files": [],
            "python_files": []
        }

        if proj_path.exists():
            # Check for MCP files
            mcp_files = []
            for ext in ["py", "md"]:
                mcp_files.extend(list(proj_path.glob(f"*.{ext}")))
            info["mcp_files"] = sorted([f.name for f in mcp_files])
            info["has_mcp"] = len(mcp_files) > 0

            # Check for Python exercises
            py_exercises_path = proj_path / "python_exercises"
            if py_exercises_path.exists():
                py_files = list(py_exercises_path.glob("*.py"))
                info["python_files"] = sorted([f.name for f in py_files])
                info["has_python_exercises"] = len(py_files) > 0

        return info

    def run_test(self, project: str, test_file: str) -> tuple[bool, str]:
        """Run a test file and return (success, output)"""
        if "/" in project:
            category, proj_name = project.split("/")
            test_path = self.base_path / category.capitalize() / proj_name / "python_exercises" / test_file
        else:
            test_path = self.base_path / "Learn" / project / "python_exercises" / test_file

        if not test_path.exists():
            return False, f"Test file not found: {test_path}"

        try:
            with console.status(f"Running {test_file}..."):
                result = subprocess.run(
                    [sys.executable, str(test_path)],
                    capture_output=True,
                    text=True,
                    timeout=30
                )

            success = result.returncode == 0
            output = result.stdout + result.stderr

            return success, output

        except subprocess.TimeoutExpired:
            return False, "Test execution timed out"
        except Exception as e:
            return False, f"Error running test: {e}"

    def display_file_content(self, file_path: Path, title: str = "File Content"):
        """Display the content of a file with syntax highlighting"""
        if not file_path.exists():
            console.print(f"[red]File not found: {file_path}[/red]")
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            from rich.syntax import Syntax
            syntax = Syntax(content, "python", theme="monokai", line_numbers=True)

            console.print(Panel(syntax, title=f"[bold blue]{title}[/bold blue]"))

        except Exception as e:
            console.print(f"[red]Error reading file: {e}[/red]")

    def show_main_menu(self):
        """Display the main menu"""
        console.clear()

        # Title
        title = Text("🚀 MCP Learning IDE", style="bold magenta")
        console.print(Panel(Align.center(title), border_style="magenta"))

        # Progress summary
        total_projects = len(self.get_projects())
        completed_count = sum(
            1 for proj in self.completed_projects.values()
            for exercise in proj.values()
            if exercise
        )

        progress_table = Table(title="📊 Learning Progress")
        progress_table.add_column("Category", style="cyan")
        progress_table.add_column("Completed", style="green")
        progress_table.add_column("Total", style="yellow")

        progress_table.add_row("All Exercises", str(completed_count), str(total_projects * 2))  # MCP + Python per project

        console.print(progress_table)
        console.print()

        # Main options
        options = [
            "1. Browse MCP Projects (Learn 01-25)",
            "2. Browse Offensive Projects (26-32)",
            "3. Browse Defensive Projects (33-40)",
            "4. View Progress Details",
            "5. Run All Tests",
            "6. Exit"
        ]

        for option in options:
            console.print(f"[bold cyan]{option}[/bold cyan]")

        choice = Prompt.ask("\nChoose an option", choices=["1", "2", "3", "4", "5", "6"])

        return choice

    def browse_projects(self, category: str):
        """Browse projects in a specific category"""
        if category == "learn":
            projects = [p for p in self.get_projects() if not "/" in p]
            title = "📚 Learn Projects (01-25)"
        elif category == "offensive":
            projects = [p for p in self.get_projects() if p.startswith("offensive/")]
            title = "⚔️ Offensive Projects (26-32)"
        elif category == "defensive":
            projects = [p for p in self.get_projects() if p.startswith("defensive/")]
            title = "🛡️ Defensive Projects (33-40)"
        else:
            return

        while True:
            console.clear()

            # Project list
            table = Table(title=title)
            table.add_column("Project", style="cyan", no_wrap=True)
            table.add_column("MCP", style="green")
            table.add_column("Python", style="yellow")
            table.add_column("Status", style="magenta")

            for project in projects:
                info = self.get_project_info(project)
                mcp_status = "✅" if info["has_mcp"] else "❌"
                py_status = "✅" if info["has_python_exercises"] else "❌"

                # Check completion status
                mcp_completed = self.is_completed(project, "mcp")
                py_completed = self.is_completed(project, "python")

                if mcp_completed and py_completed:
                    status = "[green]✓ Complete[/green]"
                elif mcp_completed or py_completed:
                    status = "[yellow]⟳ Partial[/yellow]"
                else:
                    status = "[red]○ Not Started[/red]"

                table.add_row(project, mcp_status, py_status, status)

            console.print(table)
            console.print(f"\n[bold]Enter project name to explore (or 'back' to return):[/bold]")

            choice = Prompt.ask("Project").lower()

            if choice == "back":
                break
            elif choice in [p.lower() for p in projects]:
                # Find the correct project name
                selected_project = next(p for p in projects if p.lower() == choice)
                self.explore_project(selected_project)
            else:
                console.print("[red]Invalid project name. Try again.[/red]")
                console.input("Press Enter to continue...")

    def explore_project(self, project: str):
        """Explore a specific project"""
        while True:
            console.clear()
            info = self.get_project_info(project)

            console.print(f"[bold blue]Exploring: {project}[/bold blue]")
            console.print(f"Path: {info['path']}")
            console.print()

            # Project content overview
            if info["has_mcp"]:
                console.print(f"[green]📄 MCP Files ({len(info['mcp_files'])}):[/green]")
                for file in info["mcp_files"]:
                    console.print(f"  • {file}")
                console.print()

            if info["has_python_exercises"]:
                console.print(f"[yellow]🐍 Python Exercises ({len(info['python_files'])}):[/yellow]")
                for file in info["python_files"]:
                    console.print(f"  • {file}")
                console.print()

            # Options
            options = [
                "1. View MCP Instructions",
                "2. View MCP Solution",
                "3. View Python Exercise Code",
                "4. Run Python Tests",
                "5. Mark MCP as Completed",
                "6. Mark Python Exercise as Completed",
                "7. Back to Project List"
            ]

            for option in options:
                console.print(f"[bold cyan]{option}[/bold cyan]")

            choice = Prompt.ask("\nChoose an option", choices=["1", "2", "3", "4", "5", "6", "7"])

            if choice == "1":
                self.view_instructions(project)
            elif choice == "2":
                self.view_solution(project)
            elif choice == "3":
                self.view_python_exercise(project)
            elif choice == "4":
                self.run_python_tests(project)
            elif choice == "5":
                self.mark_completed(project, "mcp")
                console.print("[green]✓ MCP project marked as completed![/green]")
                console.input("Press Enter to continue...")
            elif choice == "6":
                self.mark_completed(project, "python")
                console.print("[green]✓ Python exercise marked as completed![/green]")
                console.input("Press Enter to continue...")
            elif choice == "7":
                break

    def view_instructions(self, project: str):
        """View project instructions"""
        info = self.get_project_info(project)
        instructions_file = info["path"] / "INSTRUCTIONS.md"

        if instructions_file.exists():
            self.display_file_content(instructions_file, "📋 MCP Instructions")
        else:
            console.print("[red]Instructions file not found[/red]")

        console.input("Press Enter to continue...")

    def view_solution(self, project: str):
        """View project solution"""
        info = self.get_project_info(project)
        solution_file = info["path"] / "solution.py"

        if solution_file.exists():
            self.display_file_content(solution_file, "💡 MCP Solution")
        else:
            console.print("[red]Solution file not found[/red]")

        console.input("Press Enter to continue...")

    def view_python_exercise(self, project: str):
        """View Python exercise files"""
        info = self.get_project_info(project)
        py_path = info["path"] / "python_exercises"

        if not py_path.exists():
            console.print("[red]Python exercises not found[/red]")
            console.input("Press Enter to continue...")
            return

        py_files = [f for f in info["python_files"] if not f.startswith("test_")]

        if not py_files:
            console.print("[red]No Python exercise files found[/red]")
            console.input("Press Enter to continue...")
            return

        console.print("[yellow]Available Python exercises:[/yellow]")
        for i, file in enumerate(py_files, 1):
            console.print(f"{i}. {file}")

        try:
            choice = int(Prompt.ask("Choose exercise to view", choices=[str(i) for i in range(1, len(py_files) + 1)]))
            selected_file = py_files[choice - 1]
            file_path = py_path / selected_file
            self.display_file_content(file_path, f"🐍 Python Exercise: {selected_file}")
        except (ValueError, IndexError):
            console.print("[red]Invalid choice[/red]")

        console.input("Press Enter to continue...")

    def run_python_tests(self, project: str):
        """Run Python tests for a project"""
        info = self.get_project_info(project)
        py_path = info["path"] / "python_exercises"

        if not py_path.exists():
            console.print("[red]Python exercises not found[/red]")
            console.input("Press Enter to continue...")
            return

        test_files = [f for f in info["python_files"] if f.startswith("test_")]

        if not test_files:
            console.print("[red]No test files found[/red]")
            console.input("Press Enter to continue...")
            return

        console.print("[yellow]Available test files:[/yellow]")
        for i, file in enumerate(test_files, 1):
            console.print(f"{i}. {file}")

        try:
            choice = int(Prompt.ask("Choose test to run", choices=[str(i) for i in range(1, len(test_files) + 1)]))
            selected_file = test_files[choice - 1]

            console.print(f"\n[bold blue]Running: {selected_file}[/bold blue]")

            success, output = self.run_test(project, selected_file)

            if success:
                console.print("[green]✅ Test passed![/green]")
            else:
                console.print("[red]❌ Test failed![/red]")

            console.print("\n[bold]Test Output:[/bold]")
            console.print(Panel(output, border_style="blue"))

        except (ValueError, IndexError):
            console.print("[red]Invalid choice[/red]")

        console.input("Press Enter to continue...")

    def run(self):
        """Main application loop"""
        while True:
            choice = self.show_main_menu()

            if choice == "1":
                self.browse_projects("learn")
            elif choice == "2":
                self.browse_projects("offensive")
            elif choice == "3":
                self.browse_projects("defensive")
            elif choice == "4":
                self.show_progress_details()
            elif choice == "5":
                self.run_all_tests()
            elif choice == "6":
                console.print("[bold green]Thank you for using MCP Learning IDE! 👋[/bold green]")
                break

    def show_progress_details(self):
        """Show detailed progress information"""
        console.clear()
        console.print("[bold blue]📊 Detailed Progress[/bold blue]")

        table = Table(title="Project Completion Status")
        table.add_column("Project", style="cyan")
        table.add_column("MCP", style="green")
        table.add_column("Python", style="yellow")
        table.add_column("Overall", style="magenta")

        for project in self.get_projects():
            mcp_done = self.is_completed(project, "mcp")
            py_done = self.is_completed(project, "python")

            mcp_status = "✅" if mcp_done else "❌"
            py_status = "✅" if py_done else "❌"

            if mcp_done and py_done:
                overall = "[green]Complete[/green]"
            elif mcp_done or py_done:
                overall = "[yellow]Partial[/yellow]"
            else:
                overall = "[red]Not Started[/red]"

            table.add_row(project, mcp_status, py_status, overall)

        console.print(table)
        console.input("\nPress Enter to return to main menu...")

    def run_all_tests(self):
        """Run all available tests"""
        console.clear()
        console.print("[bold blue]🧪 Running All Tests[/bold blue]")

        total_tests = 0
        passed_tests = 0
        failed_tests = 0

        progress_table = Table()
        progress_table.add_column("Project", style="cyan")
        progress_table.add_column("Test File", style="yellow")
        progress_table.add_column("Status", style="green")

        for project in self.get_projects():
            info = self.get_project_info(project)

            if not info["has_python_exercises"]:
                continue

            py_path = info["path"] / "python_exercises"
            test_files = [f for f in info["python_files"] if f.startswith("test_")]

            for test_file in test_files:
                total_tests += 1

                with console.status(f"Testing {project} - {test_file}..."):
                    success, output = self.run_test(project, test_file)

                if success:
                    passed_tests += 1
                    status = "[green]✅ PASS[/green]"
                else:
                    failed_tests += 1
                    status = "[red]❌ FAIL[/red]"

                progress_table.add_row(project, test_file, status)

        console.print(progress_table)
        console.print(f"\n[bold]Summary:[/bold]")
        console.print(f"Total tests: {total_tests}")
        console.print(f"[green]Passed: {passed_tests}[/green]")
        console.print(f"[red]Failed: {failed_tests}[/red]")

        console.input("\nPress Enter to return to main menu...")


def main():
    """Main entry point"""
    try:
        ide = MCPLearningIDE()
        ide.run()
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Application interrupted. Goodbye! 👋[/bold yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
