from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        has_commander_or_captain = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_commander_or_captain:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            total_crew = len(self.crew)
            if experienced_count < total_crew / 2:
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)"
                )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be activate")
        return self


def main() -> None:
    crew_list = [
        CrewMember(
            member_id="C01",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=37,
            specialization="Mission Command",
            years_experience=12,
            is_active=True,
        ),
        CrewMember(
            member_id="C02",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=18,
            specialization="Navigation",
            years_experience=5,
            is_active=True,
        ),
        CrewMember(
            member_id="C03",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=19,
            specialization="Engineering",
            years_experience=6,
            is_active=True,
        ),
    ]
    mission_one = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2026, 9, 17, 13, 54),
        duration_days=900,
        crew=crew_list,
        budget_millions=2500.0,
    )

    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {mission_one.mission_name}")
    print(f"ID: {mission_one.mission_id}")
    print(f"Destination: {mission_one.destination}")
    print(f"Duration: {mission_one.duration_days} days")
    print(f"Budget: ${mission_one.budget_millions}M")
    print(f"Crew size: {len(mission_one.crew)}")
    print("Crew member:")
    for member in mission_one.crew:
        print(f"- {member.name} ({member.rank.value})"
              f" - {member.specialization}")
    print("\n=========================================")

    print("Expected validation error:")
    try:
        crew_list_invalid = [
            CrewMember(
                member_id="C04",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=30,
                specialization="Navigation",
                years_experience=10,
                is_active=True,
            ),
            CrewMember(
                member_id="C05",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=28,
                specialization="Engineering",
                years_experience=3,
                is_active=True,
            ),
        ]
        SpaceMission(
            mission_id="M2025_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 9, 17, 14, 22),
            duration_days=900,
            crew=crew_list_invalid,
            budget_millions=2500.0,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
