from typing import List

from pydantic import BaseSettings

from shared.models.settings.environment import Environment
from shared.models.settings.log_level import LogLevel


class Settings(BaseSettings):
    title: str = "Fastapi poetry ML template"
    description: str = "Fastapi poetry ML template"
    version: str = "0.0.1"
    environment: Environment = Environment.development
    log_level: LogLevel = LogLevel.debug
    allowed_hosts: List[str] = []
    api_key_header: str = "x-api-key"
    api_key: str
    init_model: bool = False

    class Config:
        env_file = ".env"
