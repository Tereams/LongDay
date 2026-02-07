from datetime import date, timedelta
from app.models.task import Task
from app.models.daily_plan import DailyPlan


def generate_daily_plan(
    task: Task,
    daily_hours: float,
    start_date: date
) -> list[DailyPlan]:
    """
    Generate a day-by-day work plan starting from start_date.
    """
    if daily_hours <= 0:
        raise ValueError("daily_hours must be positive")

    remaining = task.total_hours
    day = 0
    plan: list[DailyPlan] = []

    while remaining > 0:
        hours_today = min(daily_hours, remaining)
        plan.append(
            DailyPlan(
                day_index=day + 1,
                date=start_date + timedelta(days=day),
                hours=hours_today
            )
        )
        remaining -= hours_today
        day += 1

    return plan
