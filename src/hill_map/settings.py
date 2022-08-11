from functools import cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    mapbox_token: str = Field(default=...)

    class Config:
        env_file = ".env"


@cache
def get_settings() -> Settings:
    return Settings()
