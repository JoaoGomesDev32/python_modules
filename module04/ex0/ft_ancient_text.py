import sys
import typing


def read_file(filename: str) -> None:
    print(f"Accessing file '{filename}'")
    file: typing.IO[str] | None = None
    try:
        file = open(filename, "r")
        content = file.read()
        print("---\n")
        print(content, end="")
        print("\n---")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file:
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        read_file(sys.argv[1])
