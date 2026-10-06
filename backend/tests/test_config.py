from pathlib import Path

from app.config import Settings


def test_settings_load_backend_env_file_independent_of_working_directory() -> None:
    env_file = Path(__file__).resolve().parents[1] / ".env"
    assert Settings.model_config["env_file"] == env_file
