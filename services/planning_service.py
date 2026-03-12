from core.task import Task
from core.exception import Exception
from core.schedule import Schedule
from datetime import datetime, time, timedelta, date
from timeblock import TimeBlock

class PlanningService:

    def __init__(self):
        self.planning_start = time(9, 0)
        self.planning_end = time(18, 0)
        self.block_size = timedelta(minutes=5)
        self.window_past_days = 10
        self.window_future_days = 30

    def generate_schedule(
        self,
        tasks: list[Task],
        exceptions: list[Exception]
    ) -> Schedule:
        # this should be a global planning
        # datetime: full timestamp (date + time)
        today = date.today()

        date_start = today - timedelta(days=self.window_past_days)
        date_end = today + timedelta(days=self.window_future_days)

        planning_tasks = self._filter_tasks(tasks, date_start, date_end)
        planning_exceptions = self._filter_exceptions(exceptions, date_start, date_end)
        blocks = self._generate_blocks(date_start, date_end)
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

    def _filter_tasks(self, tasks, date_start, date_end):
        result = []
        for task in tasks:
            task_start = task.window_start.date()
            task_end = task.window_end.date()
            if task_end >= date_start and task_start <= date_end:
                result.append(task)
        return result
    
    def _filter_exceptions(self, exceptions, date_start, date_end):
        result = []
        for exc in exceptions:
            exc_start = exc.start.date()
            exc_end = exc.end.date()
            if exc_end >= date_start and exc_start <= date_end:
                result.append(exc)
        return result

    def _generate_blocks(self, date_start, date_end):
        blocks = []
        date_ptr = date_start

        while date_ptr <= date_end:

            day_start = datetime.combine(date_ptr, self.planning_start)
            day_end = datetime.combine(date_ptr, self.planning_end)

            block_start = day_start
            while block_start < day_end:
                block_end = block_start + self.block_size
                blocks.append(TimeBlock(start=block_start, end=block_end))
                block_start = block_end

            date_ptr += timedelta(days=1)

        return blocks

    def _apply_exceptions(self, blocks, exceptions):
        for exc in exceptions:
            for block in blocks:
                if exc.overlaps(block.start, block.end):
                    if exc.type.name == 'BLOCK':
                        block.status = 'BLOCKED'
                    elif exc.type.name == 'LOCK':
                        block.status = 'LOCKED'
                        block.task_id = exc.task_id

    def _assign_tasks(self, blocks, tasks):
        # 1 统计 LOCKED block
        locked_count = {}

        for block in blocks:
            if block.status == "LOCKED" and block.task_id is not None:
                locked_count[block.task_id] = locked_count.get(block.task_id, 0) + 1

        # 2 任务排序（简单按priority）
        tasks = sorted(tasks, key=lambda t: t.priority or 0)

        for task in tasks:

            needed_blocks = int(
                task.estimate_hours * 3600 / self.block_size.total_seconds()
            )

            already_locked = locked_count.get(task.id, 0)
            remaining = max(0, needed_blocks - already_locked)

            if remaining == 0:
                continue

            # 3 找候选block
            for block in blocks:

                if remaining == 0:
                    break

                if block.status != "FREE":
                    continue

                if block.start < task.window_start:
                    continue

                if block.end > task.window_end:
                    continue

                block.status = "ASSIGNED"
                block.task_id = task.id

                remaining -= 1