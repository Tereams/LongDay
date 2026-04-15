import tkinter as tk


class DayDetailView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.build_layout()
        self.bind_events()

    # =========================
    # Layout
    # =========================
    def build_layout(self):
        self.build_header()
        self.build_task_list()

    def build_header(self):
        self.title_label = tk.Label(
            self,
            text="Select a day",
            font=("Arial", 14)
        )
        self.title_label.pack(anchor="w", padx=10, pady=10)

    def build_task_list(self):
        self.list_frame = tk.Frame(self)
        self.list_frame.pack(fill="both", expand=True)

    # =========================
    # Event binding
    # =========================
    def bind_events(self):
        pass

    # =========================
    # Rendering
    # =========================
    def render_empty(self):
        self.title_label.configure(text="Select a day")
        self.clear_task_list()

    def render_day(self, day, tasks):
        self.title_label.configure(text=str(day))
        self.render_tasks(tasks)

    def render_tasks(self, tasks):
        self.clear_task_list()

        for start, end, name in tasks:
            task_label = tk.Label(
                self.list_frame,
                text=f"{start} - {end}  {name}",
                anchor="w"
            )
            task_label.pack(fill="x", padx=10, pady=2)

    # =========================
    # Helpers
    # =========================
    def clear_task_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()