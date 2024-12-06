from __future__ import annotations

import os

from pydantic import BaseSettings


def get_env_file():
    if os.getenv("ENVIRONMENT_NAME") == "production":
        print("Using production env file")
        return ".env.production"
    elif os.getenv("ENVIRONMENT_NAME") == "docker":
        print("Using docker env file")
        return ".env.docker"
    else:
        print("Using local env file")
        return ".env.local"


class DBSettings(BaseSettings):
    DB_HOSTNAME: str
    DB_PORT: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file = get_env_file()


class Settings(DBSettings):
    SECRET_KEY: str
    REDIS_URL: str
    # SLACK_WEBHOOK_URL: str | None
    ALLOWED_HOSTS: list = ["*"]
    CACHE_MAX_AGE: int = 60

    class Config:
        env_file = get_env_file()

    def check_environment_variables(self):
        if not self.DB_HOSTNAME or not self.DB_PORT or not self.DB_NAME or not self.DB_USERNAME or not self.DB_PASSWORD:
            raise ValueError("Database environment variables are not set")

        if not self.SECRET_KEY:
            raise ValueError("SECRET_KEY is not set")

        if not self.REDIS_URL:
            raise ValueError("REDIS_URL is not set")


class CachedEndpoints(BaseSettings):
    CACHED_ENDPOINTS: list = ["/cache-sample/"]


class CelerySettings(BaseSettings):
    RESULT_EXPIRES: int
    RESULT_PERSISTENT: bool
    WORKER_SEND_TASK_EVENT: bool
    WORKER_PREFETCH_MULTIPLIER: int

    class Config:
        env_file = ".config.celery"


settings = Settings()
celery_settings = CelerySettings()
cached_endpoints = CachedEndpoints()
