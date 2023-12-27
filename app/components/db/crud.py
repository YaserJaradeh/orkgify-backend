from dataclasses import dataclass
from typing import List, Optional

from pocketbase import PocketBase

from app.core.config import settings

COLLECTION_NAME = "questions"


@dataclass
class DatabaseQuestion:
    level: int
    type: str
    question: str
    candidates: List[str]
    ai_help: Optional[str] = None
    context: Optional[str] = None

    def to_dict(self):
        return {
            "level": self.level,
            "type": self.type,
            "question": self.question,
            "candidates": self.candidates,
            "ai_help": self.ai_help,
            "context": self.context,
        }


class Database:
    """
    The database class, that provides a connection to the database
    """

    _client: PocketBase
    _token: Optional[str]

    def __init__(self):
        self._client = PocketBase(settings.POCKETBASE_HOST)
        self._token = self.get_token()

    @property
    def connection(self) -> PocketBase:
        """
        Returns the connection to the database
        :return: The connection to the database
        """
        return self._client

    def get_token(self) -> Optional[str]:
        """
        Returns the token for the database
        :return: The authorization token
        """
        if settings.POCKETBASE_USERNAME is None or settings.POCKETBASE_PASSWORD is None:
            raise None
        return (
            self.connection.collection("users")
            .auth_with_password(
                settings.POCKETBASE_USERNAME, settings.POCKETBASE_PASSWORD
            )
            .token
        )

    def insert_question(self, question: DatabaseQuestion) -> None:
        """
        Inserts a question into the database
        :param question: The question to insert
        """
        self.connection.collection(COLLECTION_NAME).create(
            question.to_dict(), {"Authorization": self._token}
        )
