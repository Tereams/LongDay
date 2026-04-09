import tkinter as tk

from gui.calendar_view import CalendarView
from gui.day_detail_view import DayDetailView
from gui.sidebar_view import Sidebar


class MainView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.on_prev_month_callback = None
        self.on_next_month_callback = None
        self.on_day_selected_callback = None
        self.on_task_clicked_callback = None

        self.build_layout()
        self.bind_events()

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
        self.input_view = Sidebar(self.input_container)
        self.input_view.pack(fill="both", expand=True, padx=10, pady=10)

        self.calendar = CalendarView(
            self.calendar_container,
            year=2000,
            month=1,
            day_click_callback=self.on_day_selected,
            prev_callback=self.on_prev_month,
            next_callback=self.on_next_month
        )
        self.calendar.grid(row=0, column=0, sticky="nsew")

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
        self.input_view.set_task_click_handler(self.on_task_clicked)

    def set_callbacks(
        self,
        on_prev_month=None,
        on_next_month=None,
        on_day_selected=None,
        on_task_clicked=None
    ):
        self.on_prev_month_callback = on_prev_month
        self.on_next_month_callback = on_next_month
        self.on_day_selected_callback = on_day_selected
        self.on_task_clicked_callback = on_task_clicked

    # =========================
    # Rendering
    # =========================
    def render_input(self, tasks, constraints):
        self.input_view.show_tasks(tasks)
        self.input_view.show_constraints(constraints)

    def render_calendar(self, year, month, workload):
        self.calendar.refresh(year, month)
        self.calendar.set_workload(workload)

    def render_day_detail(self, day, tasks):
        self.detail.show_day(day, tasks)

    # =========================
    # Interaction handlers
    # =========================
    def on_prev_month(self):
        if self.on_prev_month_callback:
            self.on_prev_month_callback()

    def on_next_month(self):
        if self.on_next_month_callback:
            self.on_next_month_callback()

    def on_day_selected(self, day):
        if self.on_day_selected_callback:
            self.on_day_selected_callback(day)

    def on_task_clicked(self, task):
        if self.on_task_clicked_callback:
            self.on_task_clicked_callback(task)