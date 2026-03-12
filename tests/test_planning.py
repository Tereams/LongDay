import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from services.planning_service import PlanningService
from core.task import Task
from core.exception import Exception
from core.timeblock import BlockStatus
from datetime import datetime

tasks = [
    Task(
        id=1,
        title="Write paper",
        window_start=datetime(2026,3,12,9,0),
        window_end=datetime(2026,3,15,18,0),
        estimate_hours=2,
        priority=1
    )
]

exceptions = []

service = PlanningService()
schedule = service.generate_schedule(tasks, exceptions)

for block in schedule.assignments:
    if block.status != BlockStatus.FREE:
        print(block)