from pydantic import BaseModel
from datetime import datetime

class SpacceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool
    notes: str | None
