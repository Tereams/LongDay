from datetime import date, timedelta
from app.models.task import Task
from app.models.daily_plan import DailyPlan


def generate_daily_plan(
    task: Task,
    daily_hours,
    start_date: date,
    working_days: set[int] | None = None
) -> list[DailyPlan]:
    """
    Generate a work plan.
    
    daily_hours:
        - float: same hours every working day
        - dict[int, float]: hours per weekday (0=Mon ... 6=Sun)
    """

    if working_days is None:
        working_days = {0, 1, 2, 3, 4}

    if isinstance(daily_hours, (int, float)):
        daily_hours_map = {d: float(daily_hours) for d in working_days}
    elif isinstance(daily_hours, dict):
        daily_hours_map = daily_hours
    else:
        raise ValueError("daily_hours must be float or dict[int, float]")

    remaining = task.total_hours
    current_date = start_date
    day_index = 1
    plan: list[DailyPlan] = []

    while remaining > 0:
        weekday = current_date.weekday()

        if weekday in working_days:
            hours_today = daily_hours_map.get(weekday, 0)

            if hours_today > 0:
                hours_today = min(hours_today, remaining)

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
