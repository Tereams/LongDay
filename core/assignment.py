from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Assignment:
    """
    Assignment: planned time interval
    """
    id: int
    task_id: int
    start: datetime
    end: datetime

    def __post_init__(self):
        if self.start >= self.end:
            raise ValueError("start must be earlier than end")