import tkinter as tk
from app.config import APP_TITLE, WINDOW_SIZE
from app.models.task import Task
from app.services.planner import allocate_evenly

class TaskPlannerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_SIZE)

        self._build_ui()

    def _build_ui(self):
        self.label = tk.Label(self.root, text="Task Planner v0.1")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(
            self.root,
            text="Test Allocate",
            command=self._on_test_click
        )
        self.button.pack(pady=10)

        self.result = tk.Label(self.root, text="")
        self.result.pack()

    def _on_test_click(self):
        task = Task(name="Demo Task", total_hours=10)
        days = allocate_evenly(task, daily_hours=3)
        self.result.config(text=f"Days needed: {days}")

    def run(self):
        self.root.mainloop()
