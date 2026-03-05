from core.task import Task
from core.schedule import Schedule

class PlanningService:

    def generate_schedule(
        self,
        tasks: list[Task],
        exceptions: list[Exception]
    ) -> Schedule:
        pass

    def replan_from_existing(
        self,
        existing_schedule: Schedule,
        tasks: list[Task],
        exceptions: list[Exception]
    ) -> Schedule:
        pass