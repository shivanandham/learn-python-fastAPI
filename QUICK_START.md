# 🚀 Quick Start Guide

## Get Started in 5 Minutes

### 1. Setup Environment
```bash
# Navigate to the project directory
cd /Users/itachiuchiha/training/python

# Run the setup script
python setup_learning_environment.py
```

### 2. Start Learning (Choose One)

#### Option A: Jupyter Notebooks (Recommended)
```bash
# Start Jupyter
jupyter notebook

# Navigate to: modules/module_1_python_fundamentals/python_fundamentals.ipynb
# Begin with the first exercise!
```

#### Option B: Linear Integration (Optional)
```bash
# Create .env file with your Linear credentials
cp env.example .env
# Edit .env with your LINEAR_API_KEY and LINEAR_TEAM_ID

# Create the roadmap in Linear
python create_roadmap.py
```

### 3. First Exercise
Open `modules/module_1_python_fundamentals/python_fundamentals.ipynb` and complete:
- **Exercise 1:** Create variables for your personal information
- **Exercise 2:** Build a number guessing game

### 4. Track Progress
- Complete exercises in each notebook
- Mark tasks complete in Linear (if using)
- Move to the next module when ready

## 🎯 Learning Path

```
Module 1: Python Fundamentals (2-3 weeks)
    ↓
Module 2: Python Advanced Features (2-3 weeks)
    ↓
Module 3: Database Design and SQL (3-4 weeks)
    ↓
Module 4: SQLAlchemy ORM Fundamentals (2-3 weeks)
    ↓
Module 5: SQLAlchemy Advanced Features (2-3 weeks)
    ↓
Module 6: Building Data APIs with FastAPI (3-4 weeks)
    ↓
Module 7: Interactive Data Console (2-3 weeks)
    ↓
Module 8: Database Performance and Optimization (2-3 weeks)
    ↓
Module 9: Data Analysis with Pandas (2-3 weeks)
    ↓
Module 10: Complete Data Application Project (4-6 weeks)
```

## 🛠️ Essential Commands

```bash
# Start Jupyter Notebook
jupyter notebook

# Run FastAPI server
uvicorn modules.module_6_fastapi_apis.fastapi_apis:app --reload

# Create Linear roadmap
python create_roadmap.py

# Install new packages
pip install package_name

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

## 📚 Key Files

- **`README.md`** - Main project documentation
- **`PROJECT_OVERVIEW.md`** - Detailed project overview
- **`requirements.txt`** - Python dependencies
- **`modules/`** - Learning modules with Jupyter notebooks
- **`linear_integration/`** - Linear API integration scripts

## 🆘 Need Help?

1. **Check the notebook exercises** - Each has hints and solutions
2. **Review Linear task descriptions** - Detailed explanations
3. **Read the documentation** - Comprehensive guides
4. **Practice regularly** - Consistency is key to learning

## 🎉 Success Tips

- **Start with Module 1** - Don't skip the fundamentals
- **Complete all exercises** - Hands-on practice is essential
- **Take your time** - Learning is a journey, not a race
- **Experiment** - Try variations of the exercises
- **Build projects** - Apply what you learn

Happy learning! 🐍✨
