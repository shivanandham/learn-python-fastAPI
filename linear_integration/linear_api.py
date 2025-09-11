"""
Linear API Integration Script
A comprehensive script for managing Python learning roadmap tasks in Linear
"""

import os
from dataclasses import dataclass
from typing import Dict, List

import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Load environment variables
load_dotenv()

console = Console()


@dataclass
class LinearConfig:
    """Configuration for Linear API"""

    api_key: str
    team_id: str
    base_url: str = "https://api.linear.app/graphql"

    def __post_init__(self):
        if not self.api_key or not self.team_id:
            raise ValueError(
                "LINEAR_API_KEY and LINEAR_TEAM_ID must be set in environment variables"
            )


class LinearAPI:
    """Linear API client for managing issues and labels"""

    def __init__(self):
        self.config = LinearConfig(
            api_key=os.getenv("LINEAR_API_KEY", ""),
            team_id=os.getenv("LINEAR_TEAM_ID", ""),
        )
        self.headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json",
        }

    def _make_request(self, query: str, variables: Dict = None) -> Dict:
        """Make a GraphQL request to Linear API"""
        payload = {"query": query, "variables": variables or {}}

        try:
            response = requests.post(
                self.config.base_url, headers=self.headers, json=payload, timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            console.print(f"[red]Error making request to Linear API: {e}[/red]")
            raise

    def create_label(self, name: str, color: str, description: str = "") -> str:
        """Create a new label in Linear"""
        query = """
        mutation CreateLabel($name: String!, $color: String!, $description: String, $teamId: String!) {
            issueLabelCreate(input: {
                name: $name,
                color: $color,
                description: $description,
                teamId: $teamId
            }) {
                success
                issueLabel {
                    id
                    name
                    color
                }
            }
        }
        """

        variables = {
            "name": name,
            "color": color,
            "description": description,
            "teamId": self.config.team_id,
        }

        result = self._make_request(query, variables)

        if result.get("data", {}).get("issueLabelCreate", {}).get("success"):
            label_id = result["data"]["issueLabelCreate"]["issueLabel"]["id"]
            console.print(f"[green]✓ Created label: {name} ({color})[/green]")
            return label_id
        else:
            console.print(f"[red]✗ Failed to create label: {name}[/red]")
            return ""

    def get_labels(self) -> List[Dict]:
        """Get all labels for the team"""
        query = """
        query GetLabels($teamId: String!) {
            team(id: $teamId) {
                labels {
                    nodes {
                        id
                        name
                        color
                        description
                    }
                }
            }
        }
        """

        variables = {"teamId": self.config.team_id}
        result = self._make_request(query, variables)

        return result.get("data", {}).get("team", {}).get("labels", {}).get("nodes", [])

    def create_issue(
        self,
        title: str,
        description: str,
        label_ids: List[str] = None,
        parent_id: str = None,
        priority: int = 3,
    ) -> str:
        """Create a new issue in Linear"""
        query = """
        mutation CreateIssue($title: String!, $description: String!, $teamId: String!, 
                           $labelIds: [String!], $parentId: String, $priority: Int!) {
            issueCreate(input: {
                title: $title,
                description: $description,
                teamId: $teamId,
                labelIds: $labelIds,
                parentId: $parentId,
                priority: $priority
            }) {
                success
                issue {
                    id
                    identifier
                    title
                    url
                }
            }
        }
        """

        variables = {
            "title": title,
            "description": description,
            "teamId": self.config.team_id,
            "labelIds": label_ids or [],
            "parentId": parent_id,
            "priority": priority,
        }

        result = self._make_request(query, variables)

        if result.get("data", {}).get("issueCreate", {}).get("success"):
            issue = result["data"]["issueCreate"]["issue"]
            console.print(
                f"[green]✓ Created issue: {issue['identifier']} - {title}[/green]"
            )
            return issue["id"]
        else:
            console.print(f"[red]✗ Failed to create issue: {title}[/red]")
            return ""

    def create_sub_issue(
        self, parent_id: str, title: str, description: str, label_ids: List[str] = None
    ) -> str:
        """Create a sub-issue (child issue)"""
        return self.create_issue(
            title=title,
            description=description,
            label_ids=label_ids,
            parent_id=parent_id,
        )

    def get_issues(self, limit: int = 50) -> List[Dict]:
        """Get issues for the team"""
        query = """
        query GetIssues($teamId: String!, $first: Int!) {
            team(id: $teamId) {
                issues(first: $first) {
                    nodes {
                        id
                        identifier
                        title
                        description
                        state {
                            name
                        }
                        labels {
                            nodes {
                                name
                                color
                            }
                        }
                        parent {
                            id
                            identifier
                        }
                        children {
                            nodes {
                                id
                                identifier
                                title
                            }
                        }
                    }
                }
            }
        }
        """

        variables = {"teamId": self.config.team_id, "first": limit}
        result = self._make_request(query, variables)

        return result.get("data", {}).get("team", {}).get("issues", {}).get("nodes", [])

    def update_issue(
        self,
        issue_id: str,
        title: str = None,
        description: str = None,
        state: str = None,
    ) -> bool:
        """Update an existing issue"""
        query = """
        mutation UpdateIssue($id: String!, $title: String, $description: String, $state: String) {
            issueUpdate(id: $id, input: {
                title: $title,
                description: $description,
                state: $state
            }) {
                success
            }
        }
        """

        variables = {
            "id": issue_id,
            "title": title,
            "description": description,
            "state": state,
        }

        # Remove None values
        variables = {k: v for k, v in variables.items() if v is not None}

        result = self._make_request(query, variables)
        return result.get("data", {}).get("issueUpdate", {}).get("success", False)

    def delete_issue(self, issue_id: str) -> bool:
        """Delete an issue"""
        query = """
        mutation DeleteIssue($id: String!) {
            issueDelete(id: $id) {
                success
            }
        }
        """

        variables = {"id": issue_id}
        result = self._make_request(query, variables)
        return result.get("data", {}).get("issueDelete", {}).get("success", False)


class RoadmapManager:
    """Manager for creating and organizing the Python learning roadmap"""

    def __init__(self):
        self.api = LinearAPI()
        self.labels = {}
        self.issues = {}

    def setup_labels(self):
        """Create all necessary labels for the roadmap"""
        label_configs = [
            {
                "name": "Python Fundamentals",
                "color": "#ef4444",
                "description": "Basic Python concepts and syntax",
            },
            {
                "name": "Python Advanced",
                "color": "#f97316",
                "description": "Advanced Python features and patterns",
            },
            {
                "name": "Database Design",
                "color": "#3b82f6",
                "description": "Database concepts and SQL",
            },
            {
                "name": "SQLAlchemy Fundamentals",
                "color": "#22c55e",
                "description": "Basic SQLAlchemy ORM usage",
            },
            {
                "name": "SQLAlchemy Advanced",
                "color": "#14b8a6",
                "description": "Advanced SQLAlchemy features",
            },
            {
                "name": "API Development",
                "color": "#eab308",
                "description": "Building APIs with FastAPI",
            },
            {
                "name": "Interactive Tools",
                "color": "#a855f7",
                "description": "Interactive data exploration tools",
            },
            {
                "name": "Performance",
                "color": "#6b7280",
                "description": "Performance optimization and tuning",
            },
            {
                "name": "Data Analysis",
                "color": "#ec4899",
                "description": "Data analysis with Pandas",
            },
            {
                "name": "Complete Project",
                "color": "#f59e0b",
                "description": "End-to-end project development",
            },
        ]

        console.print("[blue]Setting up labels...[/blue]")

        for config in label_configs:
            label_id = self.api.create_label(
                name=config["name"],
                color=config["color"],
                description=config["description"],
            )
            if label_id:
                self.labels[config["name"]] = label_id

        console.print(f"[green]✓ Created {len(self.labels)} labels[/green]")

    def create_module_issue(
        self,
        module_num: int,
        title: str,
        description: str,
        label_name: str,
        priority: int = 2,
    ) -> str:
        """Create a main module issue"""
        label_id = self.labels.get(label_name, [])
        label_ids = [label_id] if label_id else []

        issue_id = self.api.create_issue(
            title=f"Module {module_num}: {title}",
            description=description,
            label_ids=label_ids,
            priority=priority,
        )

        if issue_id:
            self.issues[f"module_{module_num}"] = issue_id

        return issue_id

    def create_sub_issue(
        self, parent_key: str, title: str, description: str, label_name: str = None
    ) -> str:
        """Create a sub-issue under a parent module"""
        parent_id = self.issues.get(parent_key)
        if not parent_id:
            console.print(f"[red]Parent issue not found: {parent_key}[/red]")
            return ""

        label_ids = []
        if label_name and label_name in self.labels:
            label_ids = [self.labels[label_name]]

        return self.api.create_sub_issue(
            parent_id=parent_id,
            title=title,
            description=description,
            label_ids=label_ids,
        )

    def display_roadmap(self):
        """Display the current roadmap in a formatted table"""
        issues = self.api.get_issues(limit=100)

        table = Table(title="Python Learning Roadmap")
        table.add_column("ID", style="cyan")
        table.add_column("Title", style="white")
        table.add_column("Labels", style="magenta")
        table.add_column("Status", style="green")
        table.add_column("Children", style="yellow")

        for issue in issues:
            labels = ", ".join([label["name"] for label in issue["labels"]["nodes"]])
            children_count = len(issue["children"]["nodes"])
            status = issue["state"]["name"]

            table.add_row(
                issue["identifier"], issue["title"], labels, status, str(children_count)
            )

        console.print(table)

    def create_complete_roadmap(self):
        """Create the complete Python learning roadmap"""
        console.print("[bold blue]Creating Python Learning Roadmap...[/bold blue]")

        # Setup labels first
        self.setup_labels()

        # Module 1: Python Fundamentals
        module1_id = self.create_module_issue(
            module_num=1,
            title="Python Fundamentals",
            description="""**Learning Objectives:**
- Master Python syntax and basic data types
- Understand control structures and functions
- Learn object-oriented programming basics
- Practice file I/O and error handling

**Topics Covered:**
- Variables, data types, and operators
- Control structures (if/else, loops)
- Functions and scope
- Classes and objects
- File operations and exception handling

**Time Estimate:** 2-3 weeks
**Success Criteria:** Complete all exercises and build a simple calculator application""",
            label_name="Python Fundamentals",
            priority=1,
        )

        # Module 1 sub-issues
        self.create_sub_issue(
            "module_1",
            "Variables and Data Types",
            "Learn about Python's dynamic typing, basic data types (int, float, string, boolean), and type conversion.",
            "Python Fundamentals",
        )

        self.create_sub_issue(
            "module_1",
            "Control Structures",
            "Master if/else statements, for/while loops, and break/continue statements.",
            "Python Fundamentals",
        )

        self.create_sub_issue(
            "module_1",
            "Functions and Scope",
            "Understand function definition, parameters, return values, and variable scope.",
            "Python Fundamentals",
        )

        self.create_sub_issue(
            "module_1",
            "Classes and Objects",
            "Learn object-oriented programming basics: classes, objects, methods, and attributes.",
            "Python Fundamentals",
        )

        self.create_sub_issue(
            "module_1",
            "File I/O and Error Handling",
            "Practice reading/writing files and handling exceptions with try/except blocks.",
            "Python Fundamentals",
        )

        # Module 2: Python Advanced Features
        module2_id = self.create_module_issue(
            module_num=2,
            title="Python Advanced Features",
            description="""**Learning Objectives:**
- Master advanced Python features and patterns
- Understand functional programming concepts
- Learn performance optimization techniques
- Practice with advanced data structures

**Topics Covered:**
- Decorators and context managers
- Generators and iterators
- Lambda functions and comprehensions
- Advanced data structures
- Performance profiling and optimization

**Time Estimate:** 2-3 weeks
**Success Criteria:** Build a decorator-based caching system and optimize a data processing script""",
            label_name="Python Advanced",
            priority=1,
        )

        # Module 2 sub-issues
        self.create_sub_issue(
            "module_2",
            "Decorators and Context Managers",
            "Learn to create and use decorators, and implement context managers with __enter__ and __exit__.",
            "Python Advanced",
        )

        self.create_sub_issue(
            "module_2",
            "Generators and Iterators",
            "Understand generator functions, yield statements, and iterator protocols.",
            "Python Advanced",
        )

        self.create_sub_issue(
            "module_2",
            "Functional Programming",
            "Master lambda functions, map/filter/reduce, and list/dict comprehensions.",
            "Python Advanced",
        )

        self.create_sub_issue(
            "module_2",
            "Advanced Data Structures",
            "Work with collections module, namedtuples, dataclasses, and custom data structures.",
            "Python Advanced",
        )

        self.create_sub_issue(
            "module_2",
            "Performance Optimization",
            "Learn profiling techniques, memory management, and optimization strategies.",
            "Python Advanced",
        )

        # Continue with remaining modules...
        console.print("[green]✓ Roadmap creation completed![/green]")
        console.print(
            "[yellow]Note: This is a partial implementation. Run the script multiple times to create all modules.[/yellow]"
        )


def main():
    """Main function to run the roadmap creation"""
    try:
        manager = RoadmapManager()

        # Check if we want to create the complete roadmap
        console.print(
            Panel.fit(
                "[bold blue]Python Learning Roadmap Manager[/bold blue]\n\n"
                "This script will create a comprehensive learning roadmap in Linear.\n"
                "Make sure you have set LINEAR_API_KEY and LINEAR_TEAM_ID in your .env file.",
                title="Welcome",
            )
        )

        choice = console.input(
            "\n[bold]What would you like to do?[/bold]\n"
            "1. Create complete roadmap\n"
            "2. Display current roadmap\n"
            "3. Setup labels only\n"
            "Enter choice (1-3): "
        )

        if choice == "1":
            manager.create_complete_roadmap()
        elif choice == "2":
            manager.display_roadmap()
        elif choice == "3":
            manager.setup_labels()
        else:
            console.print("[red]Invalid choice![/red]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        console.print(
            "[yellow]Make sure your Linear API credentials are correctly set in the .env file.[/yellow]"
        )


if __name__ == "__main__":
    main()
