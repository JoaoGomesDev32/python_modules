import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            coords = tuple(float(p.strip()) for p in parts)
            return coords  # type: ignore
        except ValueError as e:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError as ve:
                    print(f"Error on parameter '{part.strip()}': {ve}")


if __name__ == "__main__":
    print(f"=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    res1 = get_player_pos()
    print(f"Got a first tuple: {res1}")
    print(f"It includes: X={res1[0]}, Y={res1[1]}, Z={res1[2]}")
    print("Get a second set of coordinates")
    res2 = get_player_pos()
