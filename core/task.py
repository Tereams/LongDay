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

    def contains(self, time: datetime) -> bool:
        return self.window_start <= time < self.window_end

    def overlaps(self, start: datetime, end: datetime) -> bool:
        return not (end <= self.window_start or start >= self.window_end)

    def accepts(self, start: datetime, end: datetime) -> bool:
        return start >= self.window_start and end <= self.window_end

    def required_blocks(self, block_size: timedelta) -> int:
        minutes = self.estimate_hours * 60
        block_minutes = block_size.total_seconds() / 60
        return int(minutes / block_minutes)

    def __post_init__(self):
        if self.window_start >= self.window_end:
            raise ValueError("window_start must be earlier than window_end")

        if self.estimate_hours <= 0:
            raise ValueError("estimate_hours must be positive")