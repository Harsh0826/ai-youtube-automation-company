from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


class Settings:
    APP_NAME = os.getenv("APP_NAME", "ai-youtube-automation-company")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./company.db")
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
    ALLOW_PAID_SERVICES = os.getenv("ALLOW_PAID_SERVICES", "false").lower() == "true"
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    YOUTUBE_CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID", "")
    YOUTUBE_CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET", "")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"


settings = Settings()
