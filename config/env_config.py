from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class DBConfig(BaseModel):
    HOST: str = "localhost"
    PORT: int = 5432
    USER: str = "postgres"
    PASSWORD: str = "postgres"
    NAME: str = "dev"


class AuthConfig(BaseModel):
    ACCESS_TOKEN_LIFETIME_MINUTES: int = 15
    REFRESH_TOKEN_LIFETIME_MINUTES: int = 60 * 24 * 7  # 1 week
    ROTATE_REFRESH_TOKEN: bool = True


class CorsConfig(BaseModel):
    ALLOW_ALL_ORIGINS: bool = True
    ALLOW_CREDENTIALS: bool = False
    ALLOWED_ORIGINS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]


class ProductsConfig(BaseModel):
    MAX_FAV_PER_USER: int = 5


class EnvConfig(BaseSettings):
    ENV: Literal["DEV", "PROD"] = "DEV"
    DJANGO_SK: str = "not_a_secret"
    BASE_DIR: Path = BASE_DIR
    ALLOWED_HOSTS: list[str] = ["*"]

    DB: DBConfig = DBConfig()
    AUTH: AuthConfig = AuthConfig()
    CORS: CorsConfig = CorsConfig()

    PRODUCTS: ProductsConfig = ProductsConfig()

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=False,
        env_nested_delimiter="__",
    )


@lru_cache
def get_env_config() -> EnvConfig:
    return EnvConfig()


env_config = get_env_config()
