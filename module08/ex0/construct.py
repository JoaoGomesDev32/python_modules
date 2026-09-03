import sys

def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def show_status() -> None:
    if not is_in_venv():
        print("Should detect no virtual environment and provide instructions")
    else:
        print(
            "source matrix_env/bin/activate\n"
            "(matrix_env) $> python3 construct.py\n"
            "# Should detect virtual environment and show details\n"
        )


def main() -> None:
    show_status()


if __name__ == "__main__":
    main()
