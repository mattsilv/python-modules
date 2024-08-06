# Reusable Python Modules Repository

This repository contains a collection of reusable Python modules, primarily focused on connecting to 3rd party APIs. Each module is designed to be modular, abstracted, and easily importable into other Python applications.

## Modules

### OpenAI Chat Completion

This module provides a simple interface for interacting with the OpenAI Chat Completion API.

## Setup and Usage

1. Clone the repository
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and add your API keys
6. Run tests: `pytest`

## Adding New Modules

To add a new module:

1. Create a new directory under `src/pymodules/` for your module
2. Add your module's Python files
3. Create corresponding test files under `tests/`
4. Update `requirements.txt` if needed
5. Update this README with information about your new module

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
