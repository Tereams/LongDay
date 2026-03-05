from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class ExceptionType(Enum):
    BLOCK = "BLOCK"
    LOCK = "LOCK"


@dataclass
class Exception:
    """
    Represents a user intervention on the timeline.

    BLOCK : prevent scheduler from assigning tasks in this period
    LOCK  : enforce a task to stay in this time period
    """

    start: datetime
    end: datetime
    type: ExceptionType
    task_id: Optional[int] = None

    def duration_minutes(self) -> int:
        """Return the duration of the exception in minutes."""
        delta = self.end - self.start
        return int(delta.total_seconds() // 60)

    def contains(self, time: datetime) -> bool:
        """Check if a given time is inside the exception interval."""
        return self.start <= time < self.end

    def overlaps(self, start: datetime, end: datetime) -> bool:
        """Check if a time range overlaps this exception."""
        return not (end <= self.start or start >= self.end)

    def __post_init__(self):
        if self.start >= self.end:
            raise ValueError("start must be earlier than end")

        if self.type == ExceptionType.LOCK and self.task_id is None:
            raise ValueError("LOCK exception must specify task_id")