from openai import OpenAI

from app.components import LLMStrategy
from app.core.config import settings


class GPTStrategy(LLMStrategy):
    model: str
    client: OpenAI = None

    def __init__(self, model: str):
        self.model = model
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def execute(self, **kwargs) -> str:
        if any([not kwargs.get(key) for key in ["system_prompt", "user_prompt"]]):
            raise ValueError("Missing required arguments")

        # Extract the required arguments
        system_prompt = kwargs.pop("system_prompt")
        user_prompt = kwargs.pop("user_prompt")

        if settings.VERBOSE:
            print(
                f"Executing strategy with system_prompt={system_prompt} and user_prompt={user_prompt}"
            )

        # Make the actual request to the OpenAI API
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            **kwargs,
        )

        # Return the response
        return response.choices[0].message.content


class GPT4Strategy(GPTStrategy):
    def __init__(self):
        super().__init__("gpt-4")


class ChatGPT16KStrategy(GPTStrategy):
    def __init__(self):
        super().__init__("gpt-3.5-turbo-16k")
