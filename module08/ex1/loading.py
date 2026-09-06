try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

try:
    import matplotlib as mp
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

try:
    import requests as rq
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

def check_dependencies() -> None:
    print("Checking dependencies:")

    if HAS_PANDAS:
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    else:
        print("[MISSING] pandas - Data manipulation unavailable")

    if HAS_NUMPY:
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    else:
        print("[MISSING] numpy - Numerical computation unavailable")

    if HAS_REQUESTS:
        print(f"[OK] requests ({rq.__version__}) - Network access ready")
    else:
        print("[MISSING] requests - Network access unavailable")

    if HAS_MATPLOTLIB:
        print(f"[OK] matplotlib ({mp.__version__}) - Visualization ready")
    else:
        print("[MISSING] matplotlib - Visualization unavailable")


def all_required_available() -> bool:
    return HAS_PANDAS and HAS_NUMPY and HAS_MATPLOTLIB


def print_instructions() -> None:
    if not all_required_available():
        print("Missing dependencies. Install with:\n")
        print("Using pip:")
        print("pip install -r requirements.txt\n")
        print("Using Poetry:")
        print("poetry install")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    check_dependencies()
    print()
    if all_required_available():
        pass
    else:
        print_instructions()


if __name__ == "__main__":
    main()