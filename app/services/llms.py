from app.models import LLM


class LLMsService:

    @staticmethod
    def complete(llm: LLM, **kwargs) -> str:
        return LLM.get_strategy(llm)().execute(**kwargs)
