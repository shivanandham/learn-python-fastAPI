"""
Roadmap Manager for Python Learning Path
Creates and manages the complete learning roadmap with all modules and sub-tasks
"""

from linear_api import RoadmapManager, console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn


class CompleteRoadmapManager(RoadmapManager):
    """Extended roadmap manager for creating the complete learning path"""

    def create_all_modules(self):
        """Create all 10 modules with their sub-tasks"""

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:

            # Module 1: Python Fundamentals
            task1 = progress.add_task(
                "Creating Module 1: Python Fundamentals...", total=6
            )
            self._create_module_1()
            progress.update(task1, completed=6)

            # Module 2: Python Advanced Features
            task2 = progress.add_task(
                "Creating Module 2: Python Advanced Features...", total=6
            )
            self._create_module_2()
            progress.update(task2, completed=6)

            # Module 3: Database Design and SQL
            task3 = progress.add_task(
                "Creating Module 3: Database Design and SQL...", total=6
            )
            self._create_module_3()
            progress.update(task3, completed=6)

            # Module 4: SQLAlchemy ORM Fundamentals
            task4 = progress.add_task(
                "Creating Module 4: SQLAlchemy ORM Fundamentals...", total=6
            )
            self._create_module_4()
            progress.update(task4, completed=6)

            # Module 5: SQLAlchemy Advanced Features
            task5 = progress.add_task(
                "Creating Module 5: SQLAlchemy Advanced Features...", total=6
            )
            self._create_module_5()
            progress.update(task5, completed=6)

            # Module 6: Building Data APIs with FastAPI
            task6 = progress.add_task(
                "Creating Module 6: Building Data APIs with FastAPI...", total=6
            )
            self._create_module_6()
            progress.update(task6, completed=6)

            # Module 7: Interactive Data Console
            task7 = progress.add_task(
                "Creating Module 7: Interactive Data Console...", total=6
            )
            self._create_module_7()
            progress.update(task7, completed=6)

            # Module 8: Database Performance and Optimization
            task8 = progress.add_task(
                "Creating Module 8: Database Performance and Optimization...", total=6
            )
            self._create_module_8()
            progress.update(task8, completed=6)

            # Module 9: Data Analysis with Pandas
            task9 = progress.add_task(
                "Creating Module 9: Data Analysis with Pandas...", total=6
            )
            self._create_module_9()
            progress.update(task9, completed=6)

            # Module 10: Complete Data Application Project
            task10 = progress.add_task(
                "Creating Module 10: Complete Data Application Project...", total=6
            )
            self._create_module_10()
            progress.update(task10, completed=6)

    def _create_module_1(self):
        """Create Module 1: Python Fundamentals"""
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
**Success Criteria:** Complete all exercises and build a simple calculator application

**Notebook:** `modules/module_1_python_fundamentals/python_fundamentals.ipynb`""",
            label_name="Python Fundamentals",
            priority=1,
        )

        # Sub-tasks for Module 1
        sub_tasks = [
            {
                "title": "Variables and Data Types",
                "description": """**Exercise:** Create variables of different types and practice type conversion.
**Expected Outcome:** Understand Python's dynamic typing system.
**Notebook Section:** Variables and Data Types""",
                "label": "Python Fundamentals",
            },
            {
                "title": "Control Structures",
                "description": """**Exercise:** Build a number guessing game using if/else and loops.
**Expected Outcome:** Master conditional logic and iteration.
**Notebook Section:** Control Structures""",
                "label": "Python Fundamentals",
            },
            {
                "title": "Functions and Scope",
                "description": """**Exercise:** Create a function library for mathematical operations.
**Expected Outcome:** Understand function definition and variable scope.
**Notebook Section:** Functions and Scope""",
                "label": "Python Fundamentals",
            },
            {
                "title": "Classes and Objects",
                "description": """**Exercise:** Build a simple bank account class with methods.
**Expected Outcome:** Master basic OOP concepts.
**Notebook Section:** Classes and Objects""",
                "label": "Python Fundamentals",
            },
            {
                "title": "File I/O and Error Handling",
                "description": """**Exercise:** Create a file processor with error handling.
**Expected Outcome:** Handle file operations and exceptions gracefully.
**Notebook Section:** File I/O and Error Handling""",
                "label": "Python Fundamentals",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_1", task["title"], task["description"], task["label"]
            )

    def _create_module_2(self):
        """Create Module 2: Python Advanced Features"""
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
**Success Criteria:** Build a decorator-based caching system and optimize a data processing script

**Notebook:** `modules/module_2_python_advanced/python_advanced.ipynb`""",
            label_name="Python Advanced",
            priority=1,
        )

        sub_tasks = [
            {
                "title": "Decorators and Context Managers",
                "description": """**Exercise:** Create a timing decorator and a database connection context manager.
**Expected Outcome:** Master decorator patterns and resource management.
**Notebook Section:** Decorators and Context Managers""",
                "label": "Python Advanced",
            },
            {
                "title": "Generators and Iterators",
                "description": """**Exercise:** Build a Fibonacci generator and custom iterator class.
**Expected Outcome:** Understand memory-efficient iteration patterns.
**Notebook Section:** Generators and Iterators""",
                "label": "Python Advanced",
            },
            {
                "title": "Functional Programming",
                "description": """**Exercise:** Process a dataset using map, filter, and reduce operations.
**Expected Outcome:** Master functional programming paradigms.
**Notebook Section:** Functional Programming""",
                "label": "Python Advanced",
            },
            {
                "title": "Advanced Data Structures",
                "description": """**Exercise:** Implement a custom data structure using collections module.
**Expected Outcome:** Work with advanced Python data structures.
**Notebook Section:** Advanced Data Structures""",
                "label": "Python Advanced",
            },
            {
                "title": "Performance Optimization",
                "description": """**Exercise:** Profile and optimize a slow data processing function.
**Expected Outcome:** Learn performance analysis and optimization techniques.
**Notebook Section:** Performance Optimization""",
                "label": "Python Advanced",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_2", task["title"], task["description"], task["label"]
            )

    def _create_module_3(self):
        """Create Module 3: Database Design and SQL"""
        module3_id = self.create_module_issue(
            module_num=3,
            title="Database Design and SQL",
            description="""**Learning Objectives:**
- Master database design principles
- Learn SQL fundamentals and advanced queries
- Understand indexing and performance optimization
- Practice database normalization

**Topics Covered:**
- Database design principles and ER modeling
- SQL DDL, DML, and DCL
- Advanced SQL queries (joins, subqueries, window functions)
- Database indexing and optimization
- Normalization and denormalization

**Time Estimate:** 3-4 weeks
**Success Criteria:** Design a normalized database schema and write complex SQL queries

**Notebook:** `modules/module_3_database_design/database_design.ipynb`""",
            label_name="Database Design",
            priority=1,
        )

        sub_tasks = [
            {
                "title": "Database Design Principles",
                "description": """**Exercise:** Design an ER diagram for an e-commerce system.
**Expected Outcome:** Master entity-relationship modeling.
**Notebook Section:** Database Design Principles""",
                "label": "Database Design",
            },
            {
                "title": "SQL Fundamentals",
                "description": """**Exercise:** Create tables, insert data, and write basic SELECT queries.
**Expected Outcome:** Master basic SQL operations.
**Notebook Section:** SQL Fundamentals""",
                "label": "Database Design",
            },
            {
                "title": "Advanced SQL Queries",
                "description": """**Exercise:** Write complex queries with joins, subqueries, and window functions.
**Expected Outcome:** Handle complex data retrieval scenarios.
**Notebook Section:** Advanced SQL Queries""",
                "label": "Database Design",
            },
            {
                "title": "Database Indexing",
                "description": """**Exercise:** Analyze query performance and create appropriate indexes.
**Expected Outcome:** Optimize database performance through indexing.
**Notebook Section:** Database Indexing""",
                "label": "Database Design",
            },
            {
                "title": "Database Normalization",
                "description": """**Exercise:** Normalize a denormalized database to 3NF.
**Expected Outcome:** Apply normalization principles to reduce redundancy.
**Notebook Section:** Database Normalization""",
                "label": "Database Design",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_3", task["title"], task["description"], task["label"]
            )

    def _create_module_4(self):
        """Create Module 4: SQLAlchemy ORM Fundamentals"""
        module4_id = self.create_module_issue(
            module_num=4,
            title="SQLAlchemy ORM Fundamentals",
            description="""**Learning Objectives:**
- Master SQLAlchemy ORM concepts and setup
- Learn model definition and relationships
- Practice basic CRUD operations
- Understand database migrations

**Topics Covered:**
- SQLAlchemy setup and configuration
- Model definition and relationships
- Basic CRUD operations
- Database migrations with Alembic
- Query building and filtering

**Time Estimate:** 2-3 weeks
**Success Criteria:** Build a complete CRUD application with SQLAlchemy

**Notebook:** `modules/module_4_sqlalchemy_fundamentals/sqlalchemy_fundamentals.ipynb`""",
            label_name="SQLAlchemy Fundamentals",
            priority=1,
        )

        sub_tasks = [
            {
                "title": "SQLAlchemy Setup and Configuration",
                "description": """**Exercise:** Set up SQLAlchemy with SQLite and PostgreSQL.
**Expected Outcome:** Configure database connections and engines.
**Notebook Section:** SQLAlchemy Setup""",
                "label": "SQLAlchemy Fundamentals",
            },
            {
                "title": "Model Definition and Relationships",
                "description": """**Exercise:** Create models for a blog system with user-post relationships.
**Expected Outcome:** Master model definition and relationship mapping.
**Notebook Section:** Models and Relationships""",
                "label": "SQLAlchemy Fundamentals",
            },
            {
                "title": "Basic CRUD Operations",
                "description": """**Exercise:** Implement full CRUD operations for a product catalog.
**Expected Outcome:** Master create, read, update, and delete operations.
**Notebook Section:** CRUD Operations""",
                "label": "SQLAlchemy Fundamentals",
            },
            {
                "title": "Database Migrations",
                "description": """**Exercise:** Use Alembic to create and manage database migrations.
**Expected Outcome:** Handle database schema changes safely.
**Notebook Section:** Database Migrations""",
                "label": "SQLAlchemy Fundamentals",
            },
            {
                "title": "Query Building and Filtering",
                "description": """**Exercise:** Build complex queries with filtering, sorting, and pagination.
**Expected Outcome:** Master SQLAlchemy query building.
**Notebook Section:** Query Building""",
                "label": "SQLAlchemy Fundamentals",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_4", task["title"], task["description"], task["label"]
            )

    def _create_module_5(self):
        """Create Module 5: SQLAlchemy Advanced Features"""
        module5_id = self.create_module_issue(
            module_num=5,
            title="SQLAlchemy Advanced Features",
            description="""**Learning Objectives:**
- Master advanced SQLAlchemy features
- Learn complex query patterns and joins
- Understand custom SQL and raw queries
- Practice database sessions and transactions

**Topics Covered:**
- Advanced queries and joins
- Custom SQL and raw queries
- Database sessions and transactions
- Performance optimization
- Advanced relationship patterns

**Time Estimate:** 2-3 weeks
**Success Criteria:** Build a complex reporting system with advanced queries

**Notebook:** `modules/module_5_sqlalchemy_advanced/sqlalchemy_advanced.ipynb`""",
            label_name="SQLAlchemy Advanced",
            priority=1,
        )

        sub_tasks = [
            {
                "title": "Advanced Queries and Joins",
                "description": """**Exercise:** Build complex queries with multiple joins and aggregations.
**Expected Outcome:** Master advanced query patterns.
**Notebook Section:** Advanced Queries""",
                "label": "SQLAlchemy Advanced",
            },
            {
                "title": "Custom SQL and Raw Queries",
                "description": """**Exercise:** Execute raw SQL queries and integrate with ORM.
**Expected Outcome:** Combine ORM with custom SQL when needed.
**Notebook Section:** Custom SQL""",
                "label": "SQLAlchemy Advanced",
            },
            {
                "title": "Database Sessions and Transactions",
                "description": """**Exercise:** Implement transaction management and session handling.
**Expected Outcome:** Master database transaction patterns.
**Notebook Section:** Sessions and Transactions""",
                "label": "SQLAlchemy Advanced",
            },
            {
                "title": "Performance Optimization",
                "description": """**Exercise:** Optimize slow queries and implement caching strategies.
**Expected Outcome:** Improve application performance.
**Notebook Section:** Performance Optimization""",
                "label": "SQLAlchemy Advanced",
            },
            {
                "title": "Advanced Relationship Patterns",
                "description": """**Exercise:** Implement many-to-many, polymorphic, and self-referential relationships.
**Expected Outcome:** Master complex relationship patterns.
**Notebook Section:** Advanced Relationships""",
                "label": "SQLAlchemy Advanced",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_5", task["title"], task["description"], task["label"]
            )

    def _create_module_6(self):
        """Create Module 6: Building Data APIs with FastAPI"""
        module6_id = self.create_module_issue(
            module_num=6,
            title="Building Data APIs with FastAPI",
            description="""**Learning Objectives:**
- Master FastAPI fundamentals
- Learn API design and documentation
- Practice data validation with Pydantic
- Understand authentication and security

**Topics Covered:**
- FastAPI setup and routing
- API design and documentation
- Data validation with Pydantic
- Authentication and security
- Database integration with FastAPI

**Time Estimate:** 3-4 weeks
**Success Criteria:** Build a complete REST API with authentication and documentation

**Notebook:** `modules/module_6_fastapi_apis/fastapi_apis.ipynb`""",
            label_name="API Development",
            priority=1,
        )

        sub_tasks = [
            {
                "title": "FastAPI Setup and Routing",
                "description": """**Exercise:** Create a FastAPI application with multiple routes and endpoints.
**Expected Outcome:** Master FastAPI application structure and routing.
**Notebook Section:** FastAPI Setup""",
                "label": "API Development",
            },
            {
                "title": "API Design and Documentation",
                "description": """**Exercise:** Design RESTful APIs with proper HTTP methods and status codes.
**Expected Outcome:** Create well-documented APIs with OpenAPI/Swagger.
**Notebook Section:** API Design""",
                "label": "API Development",
            },
            {
                "title": "Data Validation with Pydantic",
                "description": """**Exercise:** Implement request/response models with validation.
**Expected Outcome:** Master data validation and serialization.
**Notebook Section:** Data Validation""",
                "label": "API Development",
            },
            {
                "title": "Authentication and Security",
                "description": """**Exercise:** Implement JWT authentication and security middleware.
**Expected Outcome:** Secure APIs with proper authentication.
**Notebook Section:** Authentication""",
                "label": "API Development",
            },
            {
                "title": "Database Integration",
                "description": """**Exercise:** Integrate FastAPI with SQLAlchemy for data persistence.
**Expected Outcome:** Build data-driven APIs with database integration.
**Notebook Section:** Database Integration""",
                "label": "API Development",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_6", task["title"], task["description"], task["label"]
            )

    def _create_module_7(self):
        """Create Module 7: Interactive Data Console"""
        module7_id = self.create_module_issue(
            module_num=7,
            title="Interactive Data Console",
            description="""**Learning Objectives:**
- Build a Rails console-like interface
- Create interactive data exploration tools
- Implement REPL for data manipulation
- Practice real-time data analysis

**Topics Covered:**
- Interactive Python shells and REPLs
- Data exploration interfaces
- Real-time data analysis
- Custom command-line tools
- Database query interfaces

**Time Estimate:** 2-3 weeks
**Success Criteria:** Build a fully functional data exploration console

**Notebook:** `modules/module_7_interactive_console/interactive_console.ipynb`""",
            label_name="Interactive Tools",
            priority=2,
        )

        sub_tasks = [
            {
                "title": "Interactive Python Shells",
                "description": """**Exercise:** Create custom IPython extensions and magic commands.
**Expected Outcome:** Master interactive Python environments.
**Notebook Section:** Interactive Shells""",
                "label": "Interactive Tools",
            },
            {
                "title": "Data Exploration Interface",
                "description": """**Exercise:** Build a web-based data exploration dashboard.
**Expected Outcome:** Create intuitive data exploration tools.
**Notebook Section:** Data Exploration""",
                "label": "Interactive Tools",
            },
            {
                "title": "Real-time Data Analysis",
                "description": """**Exercise:** Implement streaming data analysis with live updates.
**Expected Outcome:** Handle real-time data processing.
**Notebook Section:** Real-time Analysis""",
                "label": "Interactive Tools",
            },
            {
                "title": "Custom Command-line Tools",
                "description": """**Exercise:** Build CLI tools for database management and data processing.
**Expected Outcome:** Create powerful command-line interfaces.
**Notebook Section:** CLI Tools""",
                "label": "Interactive Tools",
            },
            {
                "title": "Database Query Interface",
                "description": """**Exercise:** Create an interactive SQL query interface with autocomplete.
**Expected Outcome:** Build user-friendly database query tools.
**Notebook Section:** Query Interface""",
                "label": "Interactive Tools",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_7", task["title"], task["description"], task["label"]
            )

    def _create_module_8(self):
        """Create Module 8: Database Performance and Optimization"""
        module8_id = self.create_module_issue(
            module_num=8,
            title="Database Performance and Optimization",
            description="""**Learning Objectives:**
- Master query optimization techniques
- Learn database indexing strategies
- Understand caching and connection pooling
- Practice monitoring and profiling

**Topics Covered:**
- Query optimization and execution plans
- Database indexing strategies
- Caching and connection pooling
- Monitoring and profiling
- Performance tuning best practices

**Time Estimate:** 2-3 weeks
**Success Criteria:** Optimize a slow application and implement monitoring

**Notebook:** `modules/module_8_performance_optimization/performance_optimization.ipynb`""",
            label_name="Performance",
            priority=2,
        )

        sub_tasks = [
            {
                "title": "Query Optimization",
                "description": """**Exercise:** Analyze and optimize slow SQL queries using execution plans.
**Expected Outcome:** Master query optimization techniques.
**Notebook Section:** Query Optimization""",
                "label": "Performance",
            },
            {
                "title": "Database Indexing Strategies",
                "description": """**Exercise:** Design and implement effective indexing strategies.
**Expected Outcome:** Optimize database performance through indexing.
**Notebook Section:** Indexing Strategies""",
                "label": "Performance",
            },
            {
                "title": "Caching and Connection Pooling",
                "description": """**Exercise:** Implement Redis caching and database connection pooling.
**Expected Outcome:** Improve application performance through caching.
**Notebook Section:** Caching and Pooling""",
                "label": "Performance",
            },
            {
                "title": "Monitoring and Profiling",
                "description": """**Exercise:** Set up application monitoring and performance profiling.
**Expected Outcome:** Monitor application performance in production.
**Notebook Section:** Monitoring""",
                "label": "Performance",
            },
            {
                "title": "Performance Tuning Best Practices",
                "description": """**Exercise:** Apply performance tuning best practices to a real application.
**Expected Outcome:** Master performance optimization methodologies.
**Notebook Section:** Best Practices""",
                "label": "Performance",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_8", task["title"], task["description"], task["label"]
            )

    def _create_module_9(self):
        """Create Module 9: Data Analysis with Pandas"""
        module9_id = self.create_module_issue(
            module_num=9,
            title="Data Analysis with Pandas",
            description="""**Learning Objectives:**
- Master data manipulation and analysis with Pandas
- Learn data cleaning and preprocessing
- Practice statistical analysis
- Understand data export and import

**Topics Covered:**
- Pandas data structures (DataFrame, Series)
- Data manipulation and transformation
- Data cleaning and preprocessing
- Statistical analysis and aggregation
- Data visualization with Pandas

**Time Estimate:** 2-3 weeks
**Success Criteria:** Complete a comprehensive data analysis project

**Notebook:** `modules/module_9_data_analysis/data_analysis.ipynb`""",
            label_name="Data Analysis",
            priority=2,
        )

        sub_tasks = [
            {
                "title": "Pandas Data Structures",
                "description": """**Exercise:** Work with DataFrames and Series, practice data selection and indexing.
**Expected Outcome:** Master Pandas data structures and operations.
**Notebook Section:** Data Structures""",
                "label": "Data Analysis",
            },
            {
                "title": "Data Manipulation and Transformation",
                "description": """**Exercise:** Transform and reshape data using groupby, pivot, and merge operations.
**Expected Outcome:** Master data transformation techniques.
**Notebook Section:** Data Manipulation""",
                "label": "Data Analysis",
            },
            {
                "title": "Data Cleaning and Preprocessing",
                "description": """**Exercise:** Clean messy data, handle missing values, and detect outliers.
**Expected Outcome:** Prepare data for analysis.
**Notebook Section:** Data Cleaning""",
                "label": "Data Analysis",
            },
            {
                "title": "Statistical Analysis",
                "description": """**Exercise:** Perform statistical analysis and create summary reports.
**Expected Outcome:** Extract insights from data.
**Notebook Section:** Statistical Analysis""",
                "label": "Data Analysis",
            },
            {
                "title": "Data Visualization",
                "description": """**Exercise:** Create charts and visualizations using Pandas plotting capabilities.
**Expected Outcome:** Visualize data effectively.
**Notebook Section:** Data Visualization""",
                "label": "Data Analysis",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_9", task["title"], task["description"], task["label"]
            )

    def _create_module_10(self):
        """Create Module 10: Complete Data Application Project"""
        module10_id = self.create_module_issue(
            module_num=10,
            title="Complete Data Application Project",
            description="""**Learning Objectives:**
- Build an end-to-end data application
- Integrate all learned concepts
- Practice deployment and monitoring
- Create a portfolio-worthy project

**Topics Covered:**
- Project planning and architecture
- Data pipeline implementation
- API development and testing
- Frontend integration
- Deployment and monitoring

**Time Estimate:** 4-6 weeks
**Success Criteria:** Deploy a complete data application to production

**Notebook:** `modules/module_10_complete_project/complete_project.ipynb`""",
            label_name="Complete Project",
            priority=1,
        )

        sub_tasks = [
            {
                "title": "Project Planning and Architecture",
                "description": """**Exercise:** Design the architecture for a data-driven e-commerce analytics platform.
**Expected Outcome:** Create a comprehensive project plan and architecture.
**Notebook Section:** Project Planning""",
                "label": "Complete Project",
            },
            {
                "title": "Data Pipeline Implementation",
                "description": """**Exercise:** Build ETL pipelines for processing e-commerce data.
**Expected Outcome:** Implement robust data processing pipelines.
**Notebook Section:** Data Pipeline""",
                "label": "Complete Project",
            },
            {
                "title": "API Development and Testing",
                "description": """**Exercise:** Create REST APIs for data access and implement comprehensive testing.
**Expected Outcome:** Build and test production-ready APIs.
**Notebook Section:** API Development""",
                "label": "Complete Project",
            },
            {
                "title": "Frontend Integration",
                "description": """**Exercise:** Build a dashboard for data visualization and interaction.
**Expected Outcome:** Create an intuitive user interface.
**Notebook Section:** Frontend Integration""",
                "label": "Complete Project",
            },
            {
                "title": "Deployment and Monitoring",
                "description": """**Exercise:** Deploy the application and implement monitoring and logging.
**Expected Outcome:** Successfully deploy and monitor a production application.
**Notebook Section:** Deployment""",
                "label": "Complete Project",
            },
        ]

        for task in sub_tasks:
            self.create_sub_issue(
                "module_10", task["title"], task["description"], task["label"]
            )


def main():
    """Main function to create the complete roadmap"""
    try:
        console.print(
            Panel.fit(
                "[bold blue]Complete Python Learning Roadmap Creator[/bold blue]\n\n"
                "This will create all 10 modules with detailed sub-tasks in Linear.\n"
                "Make sure you have set LINEAR_API_KEY and LINEAR_TEAM_ID in your .env file.",
                title="Roadmap Creator",
            )
        )

        manager = CompleteRoadmapManager()

        # Setup labels first
        console.print("\n[blue]Setting up labels...[/blue]")
        manager.setup_labels()

        # Create all modules
        console.print("\n[blue]Creating complete roadmap...[/blue]")
        manager.create_all_modules()

        console.print("\n[green]✓ Complete roadmap created successfully![/green]")
        console.print(
            "[yellow]You can now view your roadmap in Linear and start learning![/yellow]"
        )

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        console.print(
            "[yellow]Make sure your Linear API credentials are correctly set in the .env file.[/yellow]"
        )


if __name__ == "__main__":
    main()
