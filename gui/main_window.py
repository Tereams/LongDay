import tkinter as tk
from gui.menu_bar import MenuBar
from gui.calendar_view import CalendarView
from gui.day_detail_view import DayDetailView
from controller.mock_controller import MockController
from gui.sidebar_view import Sidebar


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
        self.root.columnconfigure(0, weight=1)  # sidebar
        self.root.columnconfigure(1, weight=3)  # calendar
        self.root.columnconfigure(2, weight=1)  # detail

        self.root.rowconfigure(0, weight=1)

        sidebar_frame = tk.Frame(self.root, bg="#f5f5f5")
        calendar_frame = tk.Frame(self.root, bg="lightblue")
        detail_frame = tk.Frame(self.root, bg="lightgreen")

        sidebar_frame.grid(row=0, column=0, sticky="nsew")
        calendar_frame.grid(row=0, column=1, sticky="nsew")
        detail_frame.grid(row=0, column=2, sticky="nsew")

        calendar_frame.rowconfigure(0, weight=1)
        calendar_frame.columnconfigure(0, weight=1)

        detail_frame.rowconfigure(0, weight=1)
        detail_frame.columnconfigure(0, weight=1)

        self.sidebar = Sidebar(sidebar_frame)
        self.sidebar.pack(fill="both", expand=True, padx=10, pady=10)

        year, month = self.controller.get_current_year_month()
        self.calendar = CalendarView(
            calendar_frame,
            year,
            month,
            self.on_day_selected,
            self.on_prev_month,   
            self.on_next_month
        )
        self.calendar.grid(row=0, column=0, sticky="nsew")

        self.detail = DayDetailView(detail_frame)
        self.detail.grid(row=0, column=0, sticky="nsew")

        workload = self.controller.get_month_workload(2026, 3)
        self.calendar.set_workload(workload)

        self.refresh_sidebar()

    def refresh_sidebar(self):
        tasks = self.controller.get_all_tasks()
        constraints = self.controller.get_all_constraints()

        self.sidebar.show_tasks(tasks)
        self.sidebar.show_constraints(constraints)

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

