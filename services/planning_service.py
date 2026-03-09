from core.task import Task
from core.schedule import Schedule
from datetime import time, timedelta

class PlanningService:

    def __init__(self):
        self.planning_start = time(9, 0)
        self.planning_end = time(18, 0)
        self.block_size = timedelta(minutes=30)

    def generate_schedule(
        self,
        tasks: list[Task],
        exceptions: list[Exception]
    ) -> Schedule:
        # this should be a global planning

        start, end = self._determine_window(tasks)
        blocks = self._generate_blocks(start, end)
        self._apply_exceptions(blocks, exceptions)
        self._assign_tasks(blocks, tasks)

        return Schedule(blocks)
        # the merge of the block will be applied at export and at GUI

    def replan_from_existing(
        self,
        existing_schedule: Schedule,
        tasks: list[Task],
        exceptions: list[Exception]
    ) -> Schedule:
        pass

    def _determine_window(tasks):
        pass
    
    def _generate_blocks(start, end):
        pass

    def _apply_exceptions(blocks, exceptions):
        pass

    def _assign_tasks(blocks, tasks):
        pass