import tkinter as tk
from gui.calendar_view import CalendarView
from gui.day_detail_view import DayDetailView
from controller.mock_controller import MockController


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Scheduler")
        self.root.geometry("900x500")

        # layout ratio
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)

        self.root.rowconfigure(0, weight=1)

        self.controller = MockController()

        self.build_layout()

    def build_layout(self):

        # 左侧组件
        left = tk.Frame(self.root, bg="lightblue")
        left.grid(row=0, column=0, sticky="nsew")

        # 右侧组件
        right = tk.Frame(self.root, bg="lightgreen")
        right.grid(row=0, column=1, sticky="nsew")

        left.rowconfigure(0, weight=1)
        left.columnconfigure(0, weight=1)

        right.rowconfigure(0, weight=1)
        right.columnconfigure(0, weight=1)

        self.calendar = CalendarView(
            left,
            2026,
            3,
            self.on_day_selected
        )
        self.calendar.grid(row=0, column=0, sticky="nsew")

        self.detail = DayDetailView(right)
        self.detail.grid(row=0, column=0, sticky="nsew")

        workload = self.controller.get_month_workload(2026, 3)
        self.calendar.set_workload(workload)

    def on_day_selected(self, day):

        tasks = self.controller.get_day_schedule(day)
        self.detail.show_day(day, tasks)

    def run(self):
        self.root.mainloop()

