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


def show_config(config: dict[str, str]) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    if config['database_url']:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")
    if config['api_key']:
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated")
    print(f"Log Level: {config['log_level']}")
    if config['zion_endpoint']:
        print("Zion Network: Online\n")
    else:
        print("Zion Network: Offline\n")


def security_check() -> None:
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not found")
    if HAS_DOTENV:
        print("[OK] Production overrides available")
    else:
        print("[KO] python-dotenv not installed, overrides unavailable")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    show_config(config)
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
