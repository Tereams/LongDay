from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    name: str
    total_hours: float
    deadline: Optional[str] = None
