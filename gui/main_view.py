import tkinter as tk
from gui.calendar_view import CalendarView
from gui.day_detail_view import DayDetailView
from gui.sidebar_view import Sidebar
from gui.task_detail_window import TaskDetailWindow


class MainView(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        
        # self.root.title("Scheduler")
        # self.root.geometry("900x500")
        self.build_layout()
        self.load_initial_data()

    def build_layout(self):

        # menu bar 
        # self.menu_bar = MenuBar(self.root, self.controller)

        # PanedWindow (resizable layout)
        self.paned = tk.PanedWindow(
            self,
            orient=tk.HORIZONTAL,
            sashwidth=6,
            bg="#dddddd"
        )

        self.paned.pack(fill="both", expand=True)

        # three panels
        sidebar_frame = tk.Frame(self.paned)
        calendar_frame = tk.Frame(self.paned)
        detail_frame = tk.Frame(self.paned)

        self.paned.add(sidebar_frame, minsize=150)
        self.paned.add(calendar_frame, minsize=400)
        self.paned.add(detail_frame, minsize=200)

        # layout configs
        calendar_frame.rowconfigure(0, weight=1)
        calendar_frame.columnconfigure(0, weight=1)

        detail_frame.rowconfigure(0, weight=1)
        detail_frame.columnconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(sidebar_frame)
        self.sidebar.pack(fill="both", expand=True, padx=10, pady=10)
        self.sidebar.set_task_click_handler(self.open_task_detail)

        # Calendar
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

        # Detail
        self.detail = DayDetailView(detail_frame)
        self.detail.grid(row=0, column=0, sticky="nsew")

        # initial sash position
        self.after(100, self.init_sash)

    def init_sash(self):
        try:
            self.paned.sash_place(0, 200, 0)
            self.paned.sash_place(1, 750, 0)
        except:
            pass


    def open_task_detail(self, task):
        TaskDetailWindow(
            self,
            task,
            on_save=self.refresh_sidebar
        )
    # =========================
    # Data logic
    # =========================
    def load_initial_data(self):
        year, month = self.controller.get_current_year_month()

        workload = self.controller.get_month_workload(year, month)
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

    # def run(self):
    #     self.root.mainloop()

