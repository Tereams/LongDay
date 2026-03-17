class MockController:

    def __init__(self):
        self.current_year = 2026
        self.current_month = 3

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