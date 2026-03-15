class MockController:

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