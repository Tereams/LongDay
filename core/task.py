from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

@dataclass
class Task:
    """
    Task: user-defined task
    """
    id: int
    title: str
    window_start: datetime
    window_end: datetime
    estimate_hours: float
    priority: Optional[int] = None