from enum import Enum
from functools import lru_cache

from pydantic import Field, PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TESTING = "testing" 


class Settings(BaseSettings):
    app_name: str = "HR Copilot AI"
    app_version: str = "0.1.0"

    environment: Environment = Environment.DEVELOPMENT

    debug: bool = True

    database_url: PostgresDsn = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/hr_copilot_ai",
        description="PostgreSQL connection URL",
    )

    secret_key: str = Field(
        default="change-this-development-secret-key-only",
        min_length=32,
        description="JWT signing secret key",
    )

    access_token_expire_minutes: int = Field(
        default=30,
        gt= 0,
    )  

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @field_validator("secret_key")
    @classmethod
    def validate_secret_key(cls, value: str) -> str:
        if value == "change-this-development-secret-key-only":
            # Development is allowed to use the placeholder.
            return value

        return value

@lru_cache()
def get_settings() -> Settings:
    return Settings()