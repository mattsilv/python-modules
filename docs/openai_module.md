# OpenAI Module Documentation

## Overview

The `openai` module provides a simple interface for interacting with the OpenAI Chat Completion API. It includes functionality for generating and streaming chat completions.

## Configuration

The module relies on environment variables for configuration. Ensure the following variables are set in your `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `OPENAI_MODEL`: The model to use for chat completions (default is `gpt-4o-mini`).

## Classes

### `OpenAIChatCompletion`

This class handles interactions with the OpenAI Chat Completion API.

**Initialization:**

```python:src/pymodules/openai/chat_completion.py
startLine: 15
endLine: 23
```

- **Raises**: `ValueError` if `OPENAI_API_KEY` is not found in environment variables.

**Methods:**

#### `generate_completion`

Generates a chat completion using the OpenAI API.

```python:src/pymodules/openai/chat_completion.py
startLine: 25
endLine: 55
```

- **Args**:
  - `messages` (List[Dict[str, str]]): A list of message dictionaries.
  - `temperature` (float, optional): Controls randomness. Defaults to 0.7.
  - `max_tokens` (int, optional): Maximum number of tokens to generate.
- **Returns**: `str` - The generated chat completion text.
- **Raises**: `openai.error.OpenAIError` if there's an error with the OpenAI API request.

#### `stream_completion`

Streams a chat completion using the OpenAI API.

```python:src/pymodules/openai/chat_completion.py
startLine: 57
endLine: 87
```

- **Args**:
  - `messages` (List[Dict[str, str]]): A list of message dictionaries.
  - `temperature` (float, optional): Controls randomness. Defaults to 0.7.
  - `max_tokens` (int, optional): Maximum number of tokens to generate.
- **Yields**: `str` - Chunks of the generated chat completion text.
- **Raises**: `openai.error.OpenAIError` if there's an error with the OpenAI API request.

## Logging

The module uses a custom logger for error handling and debugging.

```python:src/pymodules/utils/logging.py
startLine: 1
endLine: 10
```

## Example Usage

```python
from src.pymodules.openai.chat_completion import OpenAIChatCompletion

# Initialize the client
client = OpenAIChatCompletion()

# Generate a completion
messages = [{"role": "user", "content": "Say this is a test!"}]
response = client.generate_completion(messages)
print(response)

# Stream a completion
for chunk in client.stream_completion(messages):
    print(chunk, end='')
```

## Testing

Tests for the `openai` module are located in `tests/openai/test_chat_completion.py`.

```python:tests/openai/test_chat_completion.py
startLine: 1
endLine: 49
```

- **Fixtures**: `openai_client`
- **Test Cases**:
  - `test_generate_completion`
  - `test_stream_completion`
  - `test_missing_api_key`
