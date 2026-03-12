from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from timeblock import TimeBlock


@dataclass
class Schedule:
    """
    Represents the full generated schedule.

    A Schedule contains all task assignments and metadata
    about when the schedule was generated.
    """

    assignments: List[TimeBlock] = field(default_factory=list)


    def get_task_assignments(self, task_id: int) -> List[TimeBlock]:
        """Return all assignments for a specific task."""
        return [a for a in self.assignments if a.task_id == task_id]

    def get_assignments_in_range(self, start: datetime, end: datetime) -> List[TimeBlock]:
        """Return assignments overlapping a given time range."""
        return [
            a for a in self.assignments
            if not (a.end <= start or a.start >= end)
        ]

    def clear(self):
        """Remove all assignments."""
        self.assignments.clear()