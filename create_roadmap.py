#!/usr/bin/env python3
"""
Quick script to create the complete Python learning roadmap in Linear
"""

import sys
from pathlib import Path

# Add the linear_integration directory to the path
sys.path.append(str(Path("linear_integration")))


def main():
    """Create the complete roadmap in Linear"""
    try:
        from rich.console import Console
        from roadmap_manager import CompleteRoadmapManager

        console = Console()

        console.print("[bold blue]🐍 Python Learning Roadmap Creator[/bold blue]")
        console.print("=" * 50)

        # Check if .env file exists
        if not Path(".env").exists():
            console.print("[red]❌ .env file not found![/red]")
            console.print(
                "[yellow]Please create a .env file with your Linear API credentials:[/yellow]"
            )
            console.print("LINEAR_API_KEY=your_api_key_here")
            console.print("LINEAR_TEAM_ID=your_team_id_here")
            return

        # Create the roadmap manager
        manager = CompleteRoadmapManager()

        # Setup labels first
        console.print("\n[blue]📋 Setting up labels...[/blue]")
        manager.setup_labels()

        # Ask user if they want to create all modules
        choice = console.input(
            "\n[bold]Would you like to create all 10 modules with sub-tasks? (y/n): [/bold]"
        )

        if choice.lower() == "y":
            console.print("\n[blue]🚀 Creating complete roadmap...[/blue]")
            manager.create_all_modules()
            console.print("\n[green]✅ Complete roadmap created successfully![/green]")
        else:
            console.print(
                "\n[yellow]ℹ️  Only labels were created. Run this script again to create modules.[/yellow]"
            )

        console.print("\n[bold green]🎉 Setup completed![/bold green]")
        console.print(
            "[blue]You can now view your roadmap in Linear and start learning![/blue]"
        )

    except ImportError as e:
        console.print(f"[red]❌ Error importing modules: {e}[/red]")
        console.print(
            "[yellow]Make sure you have installed all requirements: pip install -r requirements.txt[/yellow]"
        )
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")
        console.print(
            "[yellow]Make sure your Linear API credentials are correctly set in the .env file.[/yellow]"
        )


if __name__ == "__main__":
    main()
