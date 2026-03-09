from core.task import Task
from core.exception import Exception
from core.schedule import Schedule
from datetime import datetime, time, timedelta

class PlanningService:

    def __init__(self):
        self.planning_start = time(9, 0)
        self.planning_end = time(18, 0)
        self.block_size = timedelta(minutes=30)
        self.window_past_days = 10
        self.window_future_days = 30

    def generate_schedule(
        self,
        tasks: list[Task],
        exceptions: list[Exception]
    ) -> Schedule:
        # this should be a global planning

        now = datetime.now()

        start = now - timedelta(days=self.window_past_days)
        end = now + timedelta(days=self.window_future_days)

        planning_tasks = self._filter_tasks(tasks, start, end)
        planning_exceptions = self._filter_exceptions(exceptions, start, end)
        blocks = self._generate_blocks(start, end)
        self._apply_exceptions(blocks, planning_exceptions)
        self._assign_tasks(blocks, planning_tasks)

        return Schedule(blocks)
        # the merge of the block will be applied at export and at GUI

    def replan_from_existing(
        self,
        existing_schedule: Schedule,
        tasks: list[Task],
        exceptions: list[Exception]
    ) -> Schedule:
        pass

    def _filter_tasks(self, tasks, start, end):
        result = []
        for task in tasks:
            if task.window_end >= start and task.window_start <= end:
                result.append(task)

        return result
    
    def _filter_exception(self, exceptions, start, end):
        result = []
        for exc in exceptions:
            if exc.end >= start and exc.start <= end:
                result.append(exc)

        return result

    def _generate_blocks(self, start, end):
        pass

    def _apply_exceptions(self, blocks, exceptions):
        pass

    def _assign_tasks(self, blocks, tasks):
        pass