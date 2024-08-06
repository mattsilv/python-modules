#!/bin/bash

# Assume we're already in the root of the GitHub repository

# Create directory structure
mkdir -p .github/workflows
mkdir -p src/pymodules/openai
mkdir -p src/pymodules/utils
mkdir -p tests/openai
mkdir -p docs

# Create files
touch .github/workflows/ci.yml
touch src/pymodules/__init__.py
touch src/pymodules/openai/__init__.py
touch src/pymodules/openai/chat_completion.py
touch src/pymodules/openai/config.py
touch src/pymodules/utils/__init__.py
touch src/pymodules/utils/logging.py
touch tests/openai/test_chat_completion.py
touch .env.example
touch .gitignore
touch README.md
touch requirements.txt
touch setup.py
touch pyproject.toml

# Populate .gitignore
echo "venv/
__pycache__/
*.pyc
.env
.pytest_cache/
.vscode/
*.egg-info/
dist/
build/" > .gitignore

# Populate .env.example
echo "OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini" > .env.example

# Populate requirements.txt
echo "openai==0.27.0
python-dotenv==0.19.2
pytest==7.1.2
black==22.3.0
flake8==4.0.1" > requirements.txt

# Populate README.md with basic content
echo "# Reusable Python Modules Repository

This repository contains a collection of reusable Python modules, primarily focused on connecting to 3rd party APIs. Each module is designed to be modular, abstracted, and easily importable into other Python applications.

## Modules

### OpenAI Chat Completion

This module provides a simple interface for interacting with the OpenAI Chat Completion API.

## Setup and Usage

1. Clone the repository
2. Create a virtual environment: \`python3 -m venv venv\`
3. Activate the virtual environment: \`source venv/bin/activate\`
4. Install dependencies: \`pip install -r requirements.txt\`
5. Copy \`.env.example\` to \`.env\` and add your API keys
6. Run tests: \`pytest\`

## Adding New Modules

To add a new module:

1. Create a new directory under \`src/pymodules/\` for your module
2. Add your module's Python files
3. Create corresponding test files under \`tests/\`
4. Update \`requirements.txt\` if needed
5. Update this README with information about your new module

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License." > README.md

# Populate setup.py with basic content
echo "from setuptools import setup, find_packages

setup(
    name='pymodules',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'openai',
        'python-dotenv',
    ],
    extras_require={
        'dev': [
            'pytest',
            'black',
            'flake8',
        ],
    },
)" > setup.py

# Populate pyproject.toml with basic content
echo "[tool.black]
line-length = 88
target-version = ['py37']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | build
  | dist
)/
'''

[tool.pytest.ini_options]
minversion = '6.0'
addopts = '-ra -q'
testpaths = [
    'tests',
]" > pyproject.toml

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Multi-module project structure created successfully!"