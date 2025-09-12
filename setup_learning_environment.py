#!/usr/bin/env python3
"""
Setup script for Python Learning Environment
This script helps set up the learning environment and create the Linear roadmap
"""

import subprocess
import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True


def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False


def setup_environment():
    """Setup environment configuration"""
    print("\n🔧 Setting up environment...")

    env_file = Path(".env")
    env_example = Path("env.example")

    if not env_file.exists() and env_example.exists():
        # Copy example to .env
        with open(env_example, "r") as f:
            content = f.read()

        with open(env_file, "w") as f:
            f.write(content)

        print("✅ Created .env file from template")
        print("⚠️  Please update .env with your Linear API credentials")
    else:
        print("ℹ️  .env file already exists or template not found")


def create_data_directory():
    """Create data directory for databases"""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    print("✅ Created data directory")


def run_linear_setup():
    """Run Linear roadmap setup"""
    print("\n🚀 Setting up Linear roadmap...")

    # Check if .env has required variables
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found. Please create it first.")
        return False

    # Check for required environment variables
    with open(env_file, "r") as f:
        content = f.read()

    if "LINEAR_API_KEY" not in content or "LINEAR_TEAM_ID" not in content:
        print("❌ Please set LINEAR_API_KEY and LINEAR_TEAM_ID in .env file")
        return False

    try:
        # Import and run the roadmap manager
        sys.path.append(str(Path("linear_integration")))
        from roadmap_manager import CompleteRoadmapManager

        manager = CompleteRoadmapManager()
        manager.setup_labels()
        print("✅ Linear labels created successfully!")

        choice = input("\nWould you like to create the complete roadmap? (y/n): ")
        if choice.lower() == "y":
            manager.create_all_modules()
            print("✅ Complete roadmap created in Linear!")

        return True

    except ImportError as e:
        print(f"❌ Error importing roadmap manager: {e}")
        return False
    except Exception as e:
        print(f"❌ Error setting up Linear: {e}")
        return False


def display_next_steps():
    """Display next steps for the user"""
    print("\n🎉 Setup completed successfully!")
    print("\n📚 Next Steps:")
    print("1. Run 'jupyter lab' to start learning")
    print(
        "2. Navigate to modules/module_1_python_fundamentals/topic_01_variables/ to begin"
    )
    print("3. Start with explanation.ipynb, then exercise.ipynb")
    print("4. Follow the exercises in each notebook")
    print("5. Track your progress (optional: use Linear integration)")

    print("\n🔗 Useful Commands:")
    print("- Start Jupyter Lab: jupyter lab")
    print("- Start Jupyter Notebook: jupyter notebook")
    print(
        "- Run FastAPI: uvicorn modules.module_6_fastapi_apis.fastapi_apis:app --reload"
    )
    print("- Create Linear roadmap: python create_roadmap.py")

    print("\n📖 Learning Path:")
    print(
        "Module 1 (Python Fundamentals) → Module 2 (Advanced Features) → Module 3 (Database Design)"
    )
    print(
        "→ Module 4 (SQLAlchemy Fundamentals) → Module 5 (SQLAlchemy Advanced) → Module 6 (FastAPI)"
    )
    print(
        "→ Module 7 (Interactive Console) → Module 8 (Performance) → Module 9 (Data Analysis) → Module 10 (Complete Project)"
    )

    print("\n🎯 First Exercise:")
    print(
        "Open: modules/module_1_python_fundamentals/topic_01_variables/explanation.ipynb"
    )


def main():
    """Main setup function"""
    print("🐍 Python Learning Environment Setup")
    print("=" * 50)

    # Check Python version
    if not check_python_version():
        return

    # Install requirements
    if not install_requirements():
        return

    # Setup environment
    setup_environment()

    # Create data directory
    create_data_directory()

    # Setup Linear (optional)
    choice = input("\nWould you like to set up Linear integration? (y/n): ")
    if choice.lower() == "y":
        run_linear_setup()

    # Display next steps
    display_next_steps()


if __name__ == "__main__":
    main()
