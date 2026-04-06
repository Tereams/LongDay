import tkinter as tk

from gui.calendar_view import CalendarView
from gui.day_detail_view import DayDetailView
from gui.sidebar_view import Sidebar
from gui.task_detail_window import TaskDetailWindow


class MainView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.build_layout()
        self.bind_events()
        self.render_initial_state()

    # =========================
    # Layout
    # =========================
    def build_layout(self):
        self.build_paned_layout()
        self.build_subviews()
        self.after(100, self.init_sash_positions)

    def build_paned_layout(self):
        self.paned = tk.PanedWindow(
            self,
            orient=tk.HORIZONTAL,
            sashwidth=6,
            bg="#dddddd"
        )
        self.paned.pack(fill="both", expand=True)

        self.input_container = tk.Frame(self.paned)
        self.calendar_container = tk.Frame(self.paned)
        self.detail_container = tk.Frame(self.paned)

        self.paned.add(self.input_container, minsize=150)
        self.paned.add(self.calendar_container, minsize=400)
        self.paned.add(self.detail_container, minsize=200)

        self.calendar_container.rowconfigure(0, weight=1)
        self.calendar_container.columnconfigure(0, weight=1)

        self.detail_container.rowconfigure(0, weight=1)
        self.detail_container.columnconfigure(0, weight=1)

    def build_subviews(self):
        self.build_input_view()
        self.build_calendar_view()
        self.build_day_detail_view()

    def build_input_view(self):
        self.sidebar = Sidebar(self.input_container)
        self.sidebar.pack(fill="both", expand=True, padx=10, pady=10)

    def build_calendar_view(self):
        year, month = self.controller.get_current_year_month()
        self.calendar = CalendarView(
            self.calendar_container,
            year,
            month,
            self.on_day_selected,
            self.on_prev_month,
            self.on_next_month
        )
        self.calendar.grid(row=0, column=0, sticky="nsew")

    def build_day_detail_view(self):
        self.detail = DayDetailView(self.detail_container)
        self.detail.grid(row=0, column=0, sticky="nsew")

    def init_sash_positions(self):
        try:
            self.paned.sash_place(0, 200, 0)
            self.paned.sash_place(1, 750, 0)
        except tk.TclError:
            pass

    # =========================
    # Event binding
    # =========================
    def bind_events(self):
        self.sidebar.set_task_click_handler(self.open_task_detail)

    # =========================
    # Rendering
    # =========================
    def render_initial_state(self):
        self.render_sidebar()
        self.render_calendar()
        self.render_empty_day_detail()

    def render_sidebar(self):
        tasks = self.controller.get_all_tasks()
        constraints = self.controller.get_all_constraints()

        self.sidebar.show_tasks(tasks)
        self.sidebar.show_constraints(constraints)

    def render_calendar(self):
        year, month = self.controller.get_current_year_month()

        self.calendar.refresh(year, month)

        workload = self.controller.get_month_workload(year, month)
        self.calendar.set_workload(workload)

    def render_empty_day_detail(self):
        # Optional: only if DayDetailView supports an empty/default state
        pass

    def render_selected_day(self, day):
        tasks = self.controller.get_day_schedule(day)
        self.detail.show_day(day, tasks)

    # =========================
    # Interaction handlers
    # =========================
    def on_prev_month(self):
        self.controller.prev_month()
        self.render_calendar()

    def on_next_month(self):
        self.controller.next_month()
        self.render_calendar()

    def on_day_selected(self, day):
        self.render_selected_day(day)

    def open_task_detail(self, task):
        TaskDetailWindow(
            self,
            task,
            on_save=self.on_task_updated
        )

    def on_task_updated(self):
        self.render_sidebar()
        self.render_calendar()