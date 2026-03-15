import tkinter as tk
from gui.calendar_view import CalendarView
from gui.day_detail_view import DayDetailView
from controller.mock_controller import MockController


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Scheduler")
        self.root.geometry("900x500")

        self.controller = MockController()

        self.build_layout()

    def build_layout(self):

        left = tk.Frame(self.root)
        left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        right = tk.Frame(self.root, width=250)
        right.pack(side="right", fill="y")

        self.calendar = CalendarView(
            left,
            2026,
            3,
            self.on_day_selected
        )
        self.calendar.pack()

        self.detail = DayDetailView(right)
        self.detail.pack(fill="both", expand=True)

        workload = self.controller.get_month_workload(2026, 3)
        self.calendar.set_workload(workload)

    def on_day_selected(self, day):

        tasks = self.controller.get_day_schedule(day)
        self.detail.show_day(day, tasks)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.run()