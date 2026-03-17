from datetime import datetime
from core.task import Task
from core.constraint import Constraint, ConstraintType

class MockController:

    def __init__(self):
        self.current_year = 2026
        self.current_month = 3
        self.tasks = [
            Task(
                id=1,
                title="Write report",
                window_start=datetime(2026, 3, 10, 9),
                window_end=datetime(2026, 3, 20, 18),
                estimate_hours=6,
                priority=1
            ),
            Task(
                id=2,
                title="Gym",
                window_start=datetime(2026, 3, 1, 6),
                window_end=datetime(2026, 3, 31, 22),
                estimate_hours=1,
                priority=2
            ),
        ]

        self.constraints = [
            Constraint(
                start=datetime(2026, 3, 12, 10),
                end=datetime(2026, 3, 12, 12),
                type=ConstraintType.BLOCK
            ),
            Constraint(
                start=datetime(2026, 3, 15, 14),
                end=datetime(2026, 3, 15, 16),
                type=ConstraintType.LOCK,
                task_id=1
            ),
        ]

    def get_current_year_month(self):
        return self.current_year, self.current_month
    
    def next_month(self):
        if self.current_month == 12:
            self.current_year += 1
            self.current_month = 1
        else:
            self.current_month += 1


    def prev_month(self):
        if self.current_month == 1:
            self.current_year -= 1
            self.current_month = 12
        else:
            self.current_month -= 1    
    
    def get_month_workload(self, year, month):

        return {
            3: 2,
            5: 6,
            8: 4,
            12: 7,
            15: 3,
            18: 5,
            20: 8,
            25: 1
        }

    def get_day_schedule(self, day):

        return [
            ("09:00", "11:00", "Task A"),
            ("13:00", "15:00", "Task B"),
            ("16:00", "17:00", "Task C"),
        ]
    
    def get_all_tasks(self):
        return self.tasks

    def get_all_constraints(self):
        return self.constraints

    def new_schedule(self):
        print("New schedule")

    def open_schedule(self):
        print("Open")

    def save_schedule(self):
        print("Save")

    def show_month_view(self):
        print("Month view")

    def show_week_view(self):
        print("Week view")

    def show_day_view(self):
        print("Day view")

    def show_about(self):
        print("About")