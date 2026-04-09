import tkinter as tk

from controller.mock_controller import MockController
from gui.main_view import MainView
from gui.menu_bar import MenuBar
from gui.task_detail_window import TaskDetailWindow


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scheduler")
        self.root.geometry("900x500")

        self.controller = MockController()

        self.menu_bar = MenuBar(self.root, self.controller)

        self.main_view = None

        self.build_layout()
        self.bind_events()
        self.render_initial_state()

    # =========================
    # Layout
    # =========================
    def build_layout(self):
        self.main_view = MainView(self.root)
        self.main_view.pack(fill="both", expand=True)

    # =========================
    # Event binding
    # =========================
    def bind_events(self):
        self.main_view.set_callbacks(
            on_prev_month=self.on_prev_month,
            on_next_month=self.on_next_month,
            on_day_selected=self.on_day_selected,
            on_task_clicked=self.on_task_clicked
        )

    # =========================
    # Rendering
    # =========================
    def render_initial_state(self):
        self.render_input()
        self.render_calendar()

    def render_input(self):
        tasks = self.controller.get_all_tasks()
        constraints = self.controller.get_all_constraints()
        self.main_view.render_input(tasks, constraints)

    def render_calendar(self):
        year, month = self.controller.get_current_year_month()
        workload = self.controller.get_month_workload(year, month)
        self.main_view.render_calendar(year, month, workload)

    def render_day_detail(self, day):
        tasks = self.controller.get_day_schedule(day)
        self.main_view.render_day_detail(day, tasks)

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
        self.render_day_detail(day)

    def on_task_clicked(self, task):
        TaskDetailWindow(
            self.root,
            task,
            on_save=self.on_task_updated
        )

    def on_task_updated(self):
        self.render_input()
        self.render_calendar()

    def run(self):
        self.root.mainloop()