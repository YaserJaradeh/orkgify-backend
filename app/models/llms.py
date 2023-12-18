from enum import Enum
from typing import Optional

from pydantic import BaseModel

from app.components import ChatGPT16KStrategy, GPT4Strategy, Claude21Strategy


class LLM(Enum):
    ChatGPT = "ChatGPT"
    GPT4 = "GPT4"
    Claude2 = "Claude2.1"

    @staticmethod
    def get_strategy(enum_value):
        strategies = {
            "ChatGPT": ChatGPT16KStrategy,
            "GPT4": GPT4Strategy,
            "Claude2.1": Claude21Strategy
        }
        return strategies.get(enum_value.value)


class CompletionRequest(BaseModel):
    model: LLM
    user_prompt: str
    system_prompt: Optional[str] = ""
    temperature: Optional[float] = 0
    max_tokens_to_sample: Optional[int] = 4000
    max_tokens: Optional[int] = 4000
    top_p: Optional[float] = 1
    frequency_penalty: Optional[float] = 0
    presence_penalty: Optional[float] = 0

