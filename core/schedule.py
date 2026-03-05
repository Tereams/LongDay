from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from assignment import Assignment


@dataclass
class Schedule:
    """
    Represents the full generated schedule.

    A Schedule contains all task assignments and metadata
    about when the schedule was generated.
    """

    assignments: List[Assignment] = field(default_factory=list)
    generated_time: datetime = field(default_factory=datetime.utcnow)
    version: int = 1

    def add_assignment(self, assignment: Assignment):
        """Add a new assignment to the schedule."""
        self.assignments.append(assignment)

    def remove_assignment(self, assignment: Assignment):
        """Remove an assignment from the schedule."""
        self.assignments.remove(assignment)

    def get_task_assignments(self, task_id: int) -> List[Assignment]:
        """Return all assignments for a specific task."""
        return [a for a in self.assignments if a.task_id == task_id]

    def get_assignments_in_range(self, start: datetime, end: datetime) -> List[Assignment]:
        """Return assignments overlapping a given time range."""
        return [
            a for a in self.assignments
            if not (a.end <= start or a.start >= end)
        ]

    def clear(self):
        """Remove all assignments."""
        self.assignments.clear()