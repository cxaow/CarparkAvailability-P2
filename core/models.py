from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict

@dataclass
class Carpark:
    # Single HDB Carpark record.
    car_park_no: str
    address: str
    lat: Optional[float] = None
    lon: Optional[float] = None
    distance_km: float = 0.0
    total_lots: int = 0
    lots_available: int = 0
    availability_pct: float = 0.0
    car_park_type: str = "Unknown"
    parking_system: str = "Unknown"
    rank: int = 0
    status: str = "unknown"
    ai_insights: str = "No Insights Available"
    google_maps_link: str = ""

    @property
    def status_text(self) -> str:
        if self.availability_pct >= 25:
            return "Good Availability"
        elif self.availability_pct >= 10:
            return "Limited Spaces"
        return "Low Availability"

    def to_dict(self) -> Dict:
        return {
            "car_park_no": self.car_park_no,
            "address": self.address,
            "lat": self.lat,
            "lon": self.lon,
            "distance_km": self.distance_km,
            "total_lots": self.total_lots,
            "lots_available": self.lots_available,
            "availability_pct": self.availability_pct,
            "car_park_type": self.car_park_type,
            "parking_system": self.parking_system,
            "rank": self.rank,
            "status": self.status,
            "ai_insights": self.ai_insights,
            "google_maps_link": self.google_maps_link,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Carpark":
        return cls(**data)

@dataclass
class SearchRecord:
    # Completed search session.
    id: int
    destination: str
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    type_filter: str = "Not recorded"
    system_filter: str = "Not recorded"
    results: List[Dict] = field(default_factory=list)
