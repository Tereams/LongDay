import tkinter as tk
from app.models.daily_plan import DailyPlan


class ResultView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self._build_ui()

    def _build_ui(self):
        title = tk.Label(self, text="Daily Plan", font=("Arial", 12, "bold"))
        title.pack(anchor="w", pady=(0, 5))

        self.listbox = tk.Listbox(self, height=8)
        self.listbox.pack(fill="both", expand=True)

    def show_plan(self, plan: list[DailyPlan]):
        self.clear()

        for day in plan:
            self.listbox.insert(
                tk.END,
                f"Day {day.day_index}: {day.hours:.1f} h"
            )

    def clear(self):
        self.listbox.delete(0, tk.END)
