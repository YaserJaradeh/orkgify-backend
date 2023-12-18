from abc import ABC, abstractmethod
from typing import Callable, List, Optional, Tuple


class LLMStrategy(ABC):
    keywords: List[str] = []

    def __call__(self, **kwargs) -> str:
        """
        Calls the strategy, shorthand for execute
        :param kwargs: Additional arguments to pass to the strategy
        :return: The result of the strategy
        """
        return self.execute(**kwargs)

    @abstractmethod
    def execute(self, **kwargs) -> str:
        """
        Executes the strategy
        :param kwargs: Additional arguments to pass to the strategy
        :return: The result of the strategy
        """
        raise NotImplementedError()


class LLMConnector:
    strategies: List[LLMStrategy] = []

    @property
    def primed(self) -> bool:
        """
        Checks if the connector can be called safely
        :return: True if the connector has at least one strategy
        """
        return len(self.strategies) > 0

    def add_strategy(self, strategy: LLMStrategy) -> "LLMConnector":
        """
        Adds a strategy to the connector
        :param strategy: The strategy to add
        :return: The connector
        """
        self.strategies.append(strategy)
        return self

    def remove_strategy(self, strategy: LLMStrategy) -> "LLMConnector":
        """
        Removes a strategy from the connector
        :param strategy: The strategy to remove
        :return: The connector
        """
        self.strategies.remove(strategy)
        return self

    def execute(
        self, post_processor: Optional[Callable] = None, **kwargs
    ) -> List[Tuple[LLMStrategy, str]]:
        """
        Executes all strategies and returns their results
        :param post_processor: A function to post-process the results
        :param kwargs: Additional arguments to pass to the strategies
        :return: A list of tuples containing the strategy and its result
        """
        if not self.primed:
            raise Exception("No strategies have been added to the LLMConnector")
        responses = []
        for strategy in self.strategies:
            text = strategy(**kwargs)
            if post_processor is not None:
                text = post_processor(text)
            responses.append((strategy, text))
        return responses
