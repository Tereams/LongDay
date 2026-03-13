import json
from dataclasses import asdict
from datetime import datetime

from core.schedule import Schedule
from core.task import Task
from core.constraint import Constraint, ConstraintType
from core.timeblock import TimeBlock


class StorageService:

    def save(self, schedule: Schedule, path: str):

        data = {
            "tasks": [self._task_to_dict(t) for t in schedule.tasks],
            "exceptions": [self._constraint_to_dict(e) for e in schedule.constraint],
            "assignments": [self._timeblock_to_dict(a) for a in schedule.assignments],
            "generated_at": schedule.generated_at.isoformat() if schedule.generated_at else None
        }

        with open(path, "w") as f:
            json.dump(data, f, indent=2)


    def load(self, path: str) -> Schedule:

        with open(path) as f:
            data = json.load(f)

        tasks = [self._dict_to_task(d) for d in data["tasks"]]
        exceptions = [self._dict_to_exception(d) for d in data["exceptions"]]
        assignments = [self._dict_to_timeblock(d) for d in data["assignments"]]

        generated_at = (
            datetime.fromisoformat(data["generated_at"])
            if data["generated_at"] else None
        )

        return Schedule(
            tasks=tasks,
            exceptions=exceptions,
            assignments=assignments,
            generated_at=generated_at
        )
    
    def _task_to_dict(self, t: Task):

        return {
            "id": t.id,
            "title": t.title,
            "window_start": t.window_start.isoformat(),
            "window_end": t.window_end.isoformat(),
            "estimate_hours": t.estimate_hours,
            "priority": t.priority
        }
    def _dict_to_task(self, d):
        return Task(
            id=d["id"],
            title=d["title"],
            window_start=datetime.fromisoformat(d["window_start"]),
            window_end=datetime.fromisoformat(d["window_end"]),
            estimate_hours=d["estimate_hours"],
            priority=d["priority"]
        )
    
    def _constraint_to_dict(self, e):

        return {
            "start": e.start.isoformat(),
            "end": e.end.isoformat(),
            "type": e.type.value,
            "task_id": e.task_id
        }
    
    def _dict_to_constraint(self, d):

        return Constraint(
            start=datetime.fromisoformat(d["start"]),
            end=datetime.fromisoformat(d["end"]),
            type=ConstraintType(d["type"]),
            task_id=d["task_id"]
        )
    
    def _timeblock_to_dict(self, b):

        return {
            "task_id": b.task_id,
            "start": b.start.isoformat(),
            "end": b.end.isoformat()
        }

    def _dict_to_timeblock(self, d):

        return TimeBlock(
            task_id=d["task_id"],
            start=datetime.fromisoformat(d["start"]),
            end=datetime.fromisoformat(d["end"])
        )