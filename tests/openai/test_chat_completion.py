# tests/openai/test_chat_completion.py

import pytest
from unittest.mock import patch, MagicMock
from src.pymodules.openai.chat_completion import OpenAIChatCompletion

@pytest.fixture
def openai_client():
    with patch.dict('os.environ', {'OPENAI_API_KEY': 'test_key'}):
        return OpenAIChatCompletion()

def test_generate_completion(openai_client):
    with patch('openai.ChatCompletion.create') as mock_create:
        mock_create.return_value.choices[0].message = {'content': 'Test response'}
        
        messages = [{"role": "user", "content": "Say this is a test!"}]
        response = openai_client.generate_completion(messages)
        
        assert response == 'Test response'
        mock_create.assert_called_once_with(
            model=openai_client.model,
            messages=messages,
            temperature=0.7,
            max_tokens=None
        )

def test_stream_completion(openai_client):
    with patch('openai.ChatCompletion.create') as mock_create:
        mock_create.return_value = [
            MagicMock(choices=[MagicMock(delta=MagicMock(content='Test '))]),
            MagicMock(choices=[MagicMock(delta=MagicMock(content='response'))])
        ]
        
        messages = [{"role": "user", "content": "Say this is a test!"}]
        response = list(openai_client.stream_completion(messages))
        
        assert response == ['Test ', 'response']
        mock_create.assert_called_once_with(
            model=openai_client.model,
            messages=messages,
            temperature=0.7,
            max_tokens=None,
            stream=True
        )

def test_missing_api_key():
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(ValueError, match="OPENAI_API_KEY not found in environment variables"):
            OpenAIChatCompletion()