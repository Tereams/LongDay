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

    def __post_init__(self):
        if self.window_start >= self.window_end:
            raise ValueError("window_start must be earlier than window_end")

        if self.estimate_hours <= 0:
            raise ValueError("estimate_hours must be positive")