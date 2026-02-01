from app.models.task import Task
from app.models.daily_plan import DailyPlan


def generate_daily_plan(task: Task, daily_hours: float) -> list[DailyPlan]:
    """
    Generate a day-by-day work plan for a task.
    """
    if daily_hours <= 0:
        raise ValueError("daily_hours must be positive")

    remaining = task.total_hours
    day = 1
    plan: list[DailyPlan] = []

    while remaining > 0:
        hours_today = min(daily_hours, remaining)
        plan.append(
            DailyPlan(day_index=day, hours=hours_today)
        )
        remaining -= hours_today
        day += 1

    return plan
