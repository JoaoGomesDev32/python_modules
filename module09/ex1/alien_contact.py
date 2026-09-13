from enum import Enum
from pydantic import model_validator, BaseModel, Field, ValidationError
from datetime import datetime


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at"
                             " least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals should include received messages")
        return self


def main() -> None:
    alien_one = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2026, 9, 13, 12, 30),
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    print(f"ID: {alien_one.contact_id}")
    print(f"Type: {alien_one.contact_type.value}")
    print(f"Location: {alien_one.location}")
    print(f"Signal: {alien_one.signal_strength}/10")
    print(f"Witnesses: {alien_one.witness_count}")
    print(f"Message: {alien_one.message_received}")
    print("\n======================================")
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2026, 9, 13, 12, 45),
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=6.9,
            duration_minutes=45,
            witness_count=2,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
