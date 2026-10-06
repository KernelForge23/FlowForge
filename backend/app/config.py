from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[1] / ".env",
        extra="ignore",
    )

    database_url: str = "sqlite:///./flowforge.db"
    supabase_url: str = ""
    supabase_anon_key: str = ""
    http_action_timeout_seconds: float = 10.0
    http_action_max_payload_bytes: int = 64_000
    http_action_max_retries: int = 2
    github_webhook_secret: str = ""
    frontend_origin: str = "http://localhost:5173"
    email_provider: str = "resend"
    email_api_key: str = ""
    email_from: str = ""
    email_max_recipients: int = 50
    email_max_message_bytes: int = 100_000
    google_client_id: str = ""
    google_client_secret: str = ""
    google_redirect_uri: str = "http://localhost:8000/api/integrations/gmail/callback"
    token_encryption_key: str = ""


settings = Settings()
