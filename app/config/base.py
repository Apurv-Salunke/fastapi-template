from pydantic_settings import BaseSettings

class DBSettings(BaseSettings):
    DB_HOSTNAME: str
    DB_PORT: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env.local"

class Settings(DBSettings):
    SECRET_KEY: str
    SLACK_WEBHOOK_URL: str | None
    ALLOWED_HOSTS: list = ["*"]

    class Config:
        env_file = ".env.local"

    def check_environment_variables(self):
        if not self.DB_HOSTNAME or not self.DB_PORT or not self.DB_NAME or not self.DB_USERNAME or not self.DB_PASSWORD:
            raise ValueError("Database environment variables are not set")

        if not self.SECRET_KEY:
            raise ValueError("SECRET_KEY is not set")

settings = Settings()
