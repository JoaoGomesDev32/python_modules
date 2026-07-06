#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is {temp_str}")
    temp = int(temp_str)
    if 0 <= temp <= 40:
        print(f"Temperature is now {temp}°C\n")
        return temp
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    for temp in ["25", "abc", "100", "-50"]:
        try:
            input_temperature(temp)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
