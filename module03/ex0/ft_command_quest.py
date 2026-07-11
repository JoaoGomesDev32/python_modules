import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print(f"Program name: {sys.argv[0]}")
        print("No arguments provided!")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        i: int = 1
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"Argument {i}: {arg}")
    print(f"Total arguments: {len(sys.argv)}\n")
