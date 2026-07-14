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
        except ValueError:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError as e:
                    print(f"Error on parameter '{part.strip()}': {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    res1 = get_player_pos()
    print(f"Got a first tuple: {res1}")
    print(f"It includes: X={res1[0]}, Y={res1[1]}, Z={res1[2]}")
    x1, y1, z1 = res1
    distance_center = round(math.sqrt((x1**2) + (y1**2) + (z1**2)), 3)
    print(f"Distance to center: {distance_center}\n")
    print("Get a second set of coordinates")
    res2 = get_player_pos()
    x2, y2, z2 = res2
    distance_between_two = round(math.sqrt((x2-x1)**2 +
                                           (y2-y1)**2 + (z2-z1)**2), 3)
    print(f"Distance between the 2sets of coordinates: {distance_between_two}")
