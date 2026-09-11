from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    station_one = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2026, 9, 11),
        is_operational=True,
    )

    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {station_one.station_id}")
    print(f"Name: {station_one.name}")
    print(f"Crew: {station_one.crew_size} people")
    print(f"Power: {station_one.power_level}%")
    print(f"Oxygen: {station_one.oxygen_level}%")
    status = "Operational" if station_one.is_operational else "Not Operational"
    print(f"Status: {status}")
    print("\n========================================")
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="National Bus Station",
            crew_size=25,
            power_level=68.2,
            oxygen_level=28.6,
            last_maintenance=datetime(2001, 6, 18),
            is_operational=False,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
