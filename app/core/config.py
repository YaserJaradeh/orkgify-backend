import os
from typing import List

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[str]
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str
    ORKG_HOST: str
    VERBOSE: bool
    POCKETBASE_HOST: str
    POCKETBASE_USERNAME: str
    POCKETBASE_PASSWORD: str

    def __init__(self):
        self.PROJECT_NAME = os.getenv("PROJECT_NAME", "ORKGify API")
        self.BACKEND_CORS_ORIGINS = (
            os.getenv("BACKEND_CORS_ORIGINS", "[]")
            .replace("]", "")
            .replace("[", "")
            .split(",")
        )
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
        self.ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
        self.ORKG_HOST = os.getenv("ORKG_HOST", "https://orkg.org")
        self.VERBOSE = os.getenv("VERBOSE", "False").lower() == "true"
        self.POCKETBASE_HOST = os.getenv("POCKETBASE_HOST", "http://127.0.0.1:8090")
        self.POCKETBASE_USERNAME = os.getenv("POCKETBASE_USERNAME", None)
        self.POCKETBASE_PASSWORD = os.getenv("POCKETBASE_PASSWORD", None)


settings = Settings()
