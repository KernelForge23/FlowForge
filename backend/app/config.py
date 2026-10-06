from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "sqlite:///./flowforge.db"
    supabase_url: str = ""
    supabase_anon_key: str = ""
    http_action_timeout_seconds: float = 10.0
    http_action_max_payload_bytes: int = 64_000
    http_action_max_retries: int = 2
    github_webhook_secret: str = ""
    frontend_origin: str = "http://localhost:5173"


settings = Settings()
