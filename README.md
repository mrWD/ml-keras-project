# Keras Project

This is a Keras machine learning project with a properly configured virtual environment.

## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

- `examples/` - Example Keras models and tutorials
- `data/` - Data files and datasets
- `models/` - Saved model files
- `notebooks/` - Jupyter notebooks for experimentation

## Getting Started

Check out the examples in the `examples/` directory to get started with Keras.

### Running Python Scripts

To run Python scripts with the virtual environment activated, use one of these methods:

1. **From terminal (recommended)**:
   ```bash
   source venv/bin/activate
   python your_script.py
   ```

2. **Using the helper script**:
   ```bash
   python run.py your_script.py
   ```

3. **Direct virtual environment Python**:
   ```bash
   ./venv/bin/python your_script.py
   ```

## Virtual Environment

This project uses a virtual environment to avoid conflicts with system Python packages. Always activate the virtual environment before working on this project:

```bash
source venv/bin/activate
```

To deactivate the virtual environment:
```bash
deactivate
```