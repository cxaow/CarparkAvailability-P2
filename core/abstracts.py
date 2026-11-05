from abc import ABC, abstractmethod
from typing import List, Dict, Optional

# INTERFACE — Data storage contract
class Storage(ABC):
    # Interface for all storage handlers: History, Favourites.
    @abstractmethod
    def load(self) -> List[Dict]:
        # Load records from storage.
        pass

    @abstractmethod
    def save(self, records: List[Dict]) -> None:
        # Save records atomically.
        pass

class AIProvider(ABC):
    # Abstract base class for AI insight providers.
    @abstractmethod
    def get_insights(self, carparks: List[Dict], destination: str) -> List[Dict]:
        # Return enriched carpark list with AI status & insights.
        pass