from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class BlockStatus(Enum):
    FREE = "FREE"
    BLOCKED = "BLOCKED"
    ASSIGNED = "ASSIGNED"
    LOCKED = "LOCKED"


@dataclass
class TimeBlock:
    """
    Atomic time unit in the schedule (typically 30 minutes).

    A TimeBlock represents the smallest schedulable unit.
    """

    start: datetime
    end: datetime
    status: BlockStatus = BlockStatus.FREE
    task_id: Optional[int] = None

    def duration_minutes(self) -> int:
        """Return block duration in minutes."""
        delta = self.end - self.start
        return int(delta.total_seconds() // 60)

    def is_free(self) -> bool:
        """Check if the block is available for scheduling."""
        return self.status == BlockStatus.FREE

    def assign(self, task_id: int):
        """Assign this block to a task."""
        if self.status not in {BlockStatus.FREE, BlockStatus.ASSIGNED}:
            raise ValueError("Cannot assign to a blocked or locked block")
        self.status = BlockStatus.ASSIGNED
        self.task_id = task_id

    def block(self):
        """Mark this block as unavailable."""
        self.status = BlockStatus.BLOCKED
        self.task_id = None

    def lock(self, task_id: int):
        """Lock this block to a specific task."""
        self.status = BlockStatus.LOCKED
        self.task_id = task_id

    def __post_init__(self):
        if self.start >= self.end:
            raise ValueError("start must be earlier than end")