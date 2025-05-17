from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or .env file.
    Uses Pydantic's BaseSettings for automatic environment variable parsing.
    """

    # Application metadata
    app_name: str = Field(..., json_schema_extra={"env": "APP_NAME"})
    app_summary: str = Field(..., json_schema_extra={"env": "APP_SUMMARY"})
    app_description: str = Field(..., json_schema_extra={"env": "APP_DESCRIPTION"})
    app_version: str = Field(..., json_schema_extra={"env": "APP_VERSION"})
    debug: bool = Field(False, json_schema_extra={"env": "DEBUG"})
    secret_key: str = Field(..., json_schema_extra={"env": "SECRET_KEY"})


    # Database configuration
    db_user: Optional[str] = Field(None, json_schema_extra={"env": "DB_USER"})
    db_password: Optional[str] = Field(None, json_schema_extra={"env": "DB_PASSWORD"})
    db_server: Optional[str] = Field(None, json_schema_extra={"env": "DB_SERVER"})
    db_port: Optional[str] = Field(None, json_schema_extra={"env": "DB_PORT"})
    db_name: Optional[str] = Field(None, json_schema_extra={"env": "DB_NAME"})
    database_url: str = Field(..., json_schema_extra={"env": "DATABASE_URL"})


    # JWT and authentication settings
    access_token_expire_minutes: int = Field(30, json_schema_extra={"env": "ACCESS_TOKEN_EXPIRE_MINUTES"})
    algorithm: str = Field("HS256", json_schema_extra={"env": "ALGORITHM"})


    # CORS configuration
    cors_allow_origins: Optional[str] = Field("*", json_schema_extra={"env": "CORS_ALLOW_ORIGINS"})
    cors_allow_credentials: bool = Field(True, json_schema_extra={"env": "CORS_ALLOW_CREDENTIALS"})
    cors_allow_methods: Optional[str] = Field("*", json_schema_extra={"env": "CORS_ALLOW_METHODS"})
    cors_allow_headers: Optional[str] = Field("*", json_schema_extra={"env": "CORS_ALLOW_HEADERS"})


    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")


settings = Settings()
