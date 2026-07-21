import sys
import typing


def read_file(filename: str) -> str | None:
    print(f"Accessing file '{filename}'")
    file: typing.IO[str] | None = None
    try:
        file = open(filename, "r")
        content = file.read()
        print("---\n")
        print(content, end="")
        print("\n---")
        return content
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        return None
    finally:
        if file:
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        content = read_file(sys.argv[1])
        if content is not None:
            lines = content.splitlines()
            new_content = "\n".join(line + "#" for line in lines) + "\n"
            print("\nTransform data:")
            print("---\n")
            print(new_content, end="")
            print("\n---")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            save_mode = sys.stdin.readline().strip()
            if save_mode:
                new_file: typing.IO[str] | None = None
                try:
                    new_file = open(save_mode, "w")
                    new_file.write(new_content)
                    print(f"Saving data to '{save_mode}'")
                    print(f"Data saved in file '{save_mode}'.")
                except OSError as e:
                    sys.stderr.write(f"[STDERR]Error opening file"
                                     f" '{save_mode}': {e}\n")
                    sys.stderr.flush()
                    print("Data not saved.")
                finally:
                    if new_file:
                        new_file.close()
            else:
                print("Not saving data.")
