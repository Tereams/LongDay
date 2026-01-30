from dataclasses import dataclass

@dataclass
class DailyPlan:
    day_index: int        # Day 1, Day 2, ...
    hours: float          # Planned hours for this day
