# Python Learning Roadmap - Setup Guide

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Or install core dependencies manually
pip install jupyter ipython nbformat
```

### 2. Start Learning

```bash
# Start Jupyter Notebook
jupyter notebook

# Or start JupyterLab (recommended)
jupyter lab
```

### 3. Navigate to Module 1

Open `modules/module_1_python_fundamentals/README.ipynb` and follow the learning path!

## 📚 Learning Structure

Each module follows this structure:
- **📖 explanation.ipynb** - Learn concepts
- **✏️ exercise.ipynb** - Practice with exercises
- **✅ validation.ipynb** - Check your work
- **💡 solution.ipynb** - See solutions (only if needed!)

## 🔧 Troubleshooting

### Common Issues

#### "ModuleNotFoundError: No module named 'nbformat'"
```bash
pip install nbformat
```

#### Validation can't find your functions
- Make sure you've run all function definition cells in the exercise notebook first
- The validation uses `%run` magic to import functions from exercise notebooks

#### Jupyter won't start
```bash
# Try installing jupyterlab instead
pip install jupyterlab
jupyter lab
```

## 📖 Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)

## 🎯 Learning Path

1. **Module 1**: Python Fundamentals
2. **Module 2**: Python Advanced Features  
3. **Module 3**: Database Design and SQL
4. **Module 4**: SQLAlchemy ORM Fundamentals
5. **Module 5**: SQLAlchemy Advanced Features
6. **Module 6**: Building Data APIs with FastAPI
7. **Module 7**: Interactive Console/REPL
8. **Module 8**: Database Performance and Optimization
9. **Module 9**: Complete Data Application Project
