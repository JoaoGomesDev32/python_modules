def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        x = 10 / 0
    elif operation_number == 2:
        open("sem/destino/arquivo")
    elif operation_number == 3:
        x = "text" + 5
    else:
        return


def test_error_types() -> None:
    for test in range(1):
        print("Testing operation 0...")
        try:
            garden_operations(0)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        try:
            garden_operations(1)
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        try:
            garden_operations(2)
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        try:
            garden_operations(3)
        except TypeError as e:
            print(f"Caught TypeError: {e}")

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
