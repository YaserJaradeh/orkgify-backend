import os
from typing import List


class Settings:
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[str]
    OPENAI_API_KEY: str
    ORKG_HOST: str
    VERBOSE: bool

    def __init__(self):
        self.PROJECT_NAME = os.getenv("PROJECT_NAME", "ORKGify API")
        self.BACKEND_CORS_ORIGINS = (
            os.getenv("BACKEND_CORS_ORIGINS", "[]")
            .replace("]", "")
            .replace("[", "")
            .split(",")
        )
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
        self.ORKG_HOST = os.getenv("ORKG_HOST", "https://orkg.org")
        self.VERBOSE = os.getenv("VERBOSE", "False").lower() == "true"


settings = Settings()
