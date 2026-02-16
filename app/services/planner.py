from datetime import date, timedelta
from app.models.task import Task
from app.models.daily_plan import DailyPlan


def generate_daily_plan(
    task: Task,
    daily_hours: float,
    start_date: date,
    working_days: set[int] | None = None
) -> list[DailyPlan]:
    """
    Generate a work plan starting from start_date.
    Only schedule on working_days (default: Mon–Fri).
    """

    if daily_hours <= 0:
        raise ValueError("daily_hours must be positive")

    if working_days is None:
        working_days = {0, 1, 2, 3, 4}  # Mon–Fri

    remaining = task.total_hours
    current_date = start_date
    day_index = 1
    plan: list[DailyPlan] = []

    while remaining > 0:
        if current_date.weekday() in working_days:
            hours_today = min(daily_hours, remaining)

            plan.append(
                DailyPlan(
                    day_index=day_index,
                    date=current_date,
                    hours=hours_today
                )
            )

            remaining -= hours_today
            day_index += 1

        current_date += timedelta(days=1)

    return plan