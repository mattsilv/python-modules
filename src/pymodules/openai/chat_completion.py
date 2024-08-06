# src/pymodules/openai/chat_completion.py

import os
from typing import List, Dict, Optional, Generator
import openai
from dotenv import load_dotenv
from ..utils.logging import setup_logger

# Load environment variables
load_dotenv()

# Setup logging
logger = setup_logger(__name__)

class OpenAIChatCompletion:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        openai.api_key = self.api_key

    def generate_completion(
        self, 
        messages: List[Dict[str, str]], 
        temperature: float = 0.7, 
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Generate a chat completion using the OpenAI API.

        Args:
            messages (List[Dict[str, str]]): A list of message dictionaries.
            temperature (float, optional): Controls randomness. Defaults to 0.7.
            max_tokens (int, optional): Maximum number of tokens to generate.

        Returns:
            str: The generated chat completion text.

        Raises:
            openai.error.OpenAIError: If there's an error with the OpenAI API request.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message['content']
        except openai.error.OpenAIError as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise

    def stream_completion(
        self, 
        messages: List[Dict[str, str]], 
        temperature: float = 0.7, 
        max_tokens: Optional[int] = None
    ) -> Generator[str, None, None]:
        """
        Stream a chat completion using the OpenAI API.

        Args:
            messages (List[Dict[str, str]]): A list of message dictionaries.
            temperature (float, optional): Controls randomness. Defaults to 0.7.
            max_tokens (int, optional): Maximum number of tokens to generate.

        Yields:
            str: Chunks of the generated chat completion text.

        Raises:
            openai.error.OpenAIError: If there's an error with the OpenAI API request.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True
            )
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
        except openai.error.OpenAIError as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise