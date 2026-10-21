from pathlib import Path

from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseModel):
    app_name: str = "ai-youtube-automation-company"
    database_url: str = "sqlite:///./company.db"
    frontend_url: str = "http://localhost:5173"
    allow_paid_services: bool = False
    ollama_base_url: str = "http://localhost:11434"
    youtube_client_id: str = ""
    youtube_client_secret: str = ""
    log_level: str = "INFO"

    class Config:
        extra = "ignore"


settings = Settings()
