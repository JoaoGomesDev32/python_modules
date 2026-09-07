try:
    from dotenv import load_dotenv
    HAS_DOTENV = True
except ImportError:
    HAS_DOTENV = False


import os


def load_config() -> dict[str, str]:
    if HAS_DOTENV:
        load_dotenv()

    mode = os.getenv("MATRIX_MODE", "production")
    database_url = os.getenv(
        "DATABASE_URL", "postgresql://localhost:5432/matrix_db"
    )
    api_key = os.getenv("API_KEY", "sk_test_fake_key_12345")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv(
        "ZION_ENDPOINT", "https://zion.resistence.net/api"
    )

    return {
        "mode": mode,
        "database_url": database_url,
        "api_key": api_key,
        "log_level": log_level,
        "zion_endpoint": zion_endpoint
    }
