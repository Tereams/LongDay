import tkinter as tk
from gui.menu_bar import MenuBar
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

        # menu bar 
        self.menu_bar = MenuBar(self.root, self.controller)

        # layout ratio
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)

        self.root.rowconfigure(0, weight=1)

        # left component
        left = tk.Frame(self.root, bg="lightblue")
        left.grid(row=0, column=0, sticky="nsew")

        # right component
        right = tk.Frame(self.root, bg="lightgreen")
        right.grid(row=0, column=1, sticky="nsew")

        left.rowconfigure(0, weight=1)
        left.columnconfigure(0, weight=1)

        right.rowconfigure(0, weight=1)
        right.columnconfigure(0, weight=1)

        year, month = self.controller.get_current_year_month()

        self.calendar = CalendarView(
            left,
            year,
            month,
            self.on_day_selected,
            self.on_prev_month,   
            self.on_next_month
        )
        self.calendar.grid(row=0, column=0, sticky="nsew")

        self.detail = DayDetailView(right)
        self.detail.grid(row=0, column=0, sticky="nsew")

        workload = self.controller.get_month_workload(2026, 3)
        self.calendar.set_workload(workload)

    def refresh_calendar(self):

        year, month = self.controller.get_current_year_month()

        # 1. refresh UI
        self.calendar.refresh(year, month)

        # 2. refresh data
        workload = self.controller.get_month_workload(year, month)
        self.calendar.set_workload(workload)

    def on_prev_month(self):
        self.controller.prev_month()
        self.refresh_calendar()

    def on_next_month(self):
        self.controller.next_month()
        self.refresh_calendar()

    def on_day_selected(self, day):

        tasks = self.controller.get_day_schedule(day)
        self.detail.show_day(day, tasks)

    def run(self):
        self.root.mainloop()

