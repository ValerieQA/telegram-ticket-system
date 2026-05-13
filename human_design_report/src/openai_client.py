import json
import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

from config import OPENAI_MODEL, OPENAI_TEMPERATURE


load_dotenv()


class OpenAIClient:
    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set. Add it to your .env file.")
        self.client = OpenAI(api_key=api_key)

    def generate_text(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.responses.create(
            model=OPENAI_MODEL,
            temperature=OPENAI_TEMPERATURE,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.output_text.strip()

    def generate_json(self, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        response = self.client.responses.create(
            model=OPENAI_MODEL,
            temperature=OPENAI_TEMPERATURE,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return json.loads(response.output_text)
