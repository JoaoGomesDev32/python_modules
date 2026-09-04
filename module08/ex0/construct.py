import os
import site
import sys


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def show_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


def show_inside_venv() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    packages_path = site.getsitepackages()[0]
    print(f"Package installation path:\n{packages_path}")


def show_status() -> None:
    if not is_in_venv():
        show_outside_venv()
    else:
        show_inside_venv()


def main() -> None:
    show_status()


if __name__ == "__main__":
    main()
